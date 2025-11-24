"""Content operation tools for PanaversityFS.

Implements 3 MCP tools for lesson content management:
- read_content: Read lesson markdown with metadata
- write_content: Upsert with conflict detection (file_hash)
- delete_content: Delete lesson file
"""

from panaversity_fs.server import mcp
from panaversity_fs.models import ReadContentInput, WriteContentInput, DeleteContentInput, ContentMetadata
from panaversity_fs.storage import get_operator
from panaversity_fs.storage_utils import compute_sha256, validate_path
from panaversity_fs.errors import ContentNotFoundError, ConflictError, InvalidPathError
from panaversity_fs.audit import log_operation
from panaversity_fs.models import OperationType, OperationStatus
from panaversity_fs.config import get_config
from datetime import datetime, timezone
import json


@mcp.tool(
    name="read_content",
    annotations={
        "title": "Read Lesson Content",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def read_content(params: ReadContentInput) -> str:
    """Read lesson markdown content with metadata (FR-009).

    Returns lesson content plus metadata: file_size, last_modified, storage_backend, file_hash.

    Args:
        params (ReadContentInput): Validated input containing:
            - book_id (str): Book identifier (e.g., 'ai-native-python')
            - path (str): Lesson path relative to book root (e.g., 'lessons/part-1/chapter-01/lesson-01.md')

    Returns:
        str: JSON-formatted response with content and metadata

    Example:
        ```
        Input: {"book_id": "ai-native-python", "path": "lessons/part-1/chapter-01/lesson-01.md"}
        Output: {
          "content": "# Lesson 1\\n\\nIntroduction...",
          "file_size": 1234,
          "last_modified": "2025-11-24T12:00:00Z",
          "storage_backend": "fs",
          "file_hash_sha256": "a591a6d40bf420404a011733cfb7b190..."
        }
        ```
    """
    start_time = datetime.now(timezone.utc)

    try:
        # Validate path
        if not validate_path(params.path):
            raise InvalidPathError(params.path, "Path contains invalid characters or traversal attempts")

        # Build full path
        full_path = f"books/{params.book_id}/{params.path}"

        # Get operator
        op = get_operator()
        config = get_config()

        # Read content
        content_bytes = await op.read(full_path)
        content = content_bytes.decode('utf-8')

        # Get metadata
        metadata = await op.stat(full_path)

        # Compute hash
        file_hash = compute_sha256(content_bytes)

        # Build response
        response = ContentMetadata(
            file_size=metadata.content_length,
            last_modified=metadata.last_modified,
            storage_backend=config.storage_backend,
            file_hash_sha256=file_hash,
            content=content
        )

        # Log success
        execution_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
        await log_operation(
            operation=OperationType.READ_CONTENT,
            path=full_path,
            agent_id="system",  # TODO: Get from auth context
            status=OperationStatus.SUCCESS,
            execution_time_ms=execution_time
        )

        return response.model_dump_json(indent=2)

    except FileNotFoundError:
        # Log error
        await log_operation(
            operation=OperationType.READ_CONTENT,
            path=f"books/{params.book_id}/{params.path}",
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message="Content not found"
        )

        raise ContentNotFoundError(f"books/{params.book_id}/{params.path}")

    except Exception as e:
        # Log error
        await log_operation(
            operation=OperationType.READ_CONTENT,
            path=f"books/{params.book_id}/{params.path}",
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message=str(e)
        )

        return f"Error reading content: {type(e).__name__}: {str(e)}"


@mcp.tool(
    name="write_content",
    annotations={
        "title": "Write Lesson Content (Upsert)",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def write_content(params: WriteContentInput) -> str:
    """Write lesson content with upsert semantics and conflict detection (FR-007, FR-008).

    Supports two modes:
    - Update mode (file_hash provided): Verify hash matches before write, detect conflicts
    - Create mode (file_hash omitted): Create new file or overwrite existing

    Args:
        params (WriteContentInput): Validated input containing:
            - book_id (str): Book identifier
            - path (str): Lesson path relative to book root
            - content (str): Markdown content with YAML frontmatter
            - file_hash (str | None): SHA256 hash for conflict detection (optional)

    Returns:
        str: Success message with file metadata

    Example:
        ```
        # Create new file
        Input: {
          "book_id": "ai-native-python",
          "path": "lessons/part-1/chapter-01/lesson-01.md",
          "content": "# Lesson 1\\n\\nContent..."
        }

        # Update with conflict detection
        Input: {
          "book_id": "ai-native-python",
          "path": "lessons/part-1/chapter-01/lesson-01.md",
          "content": "# Lesson 1 (Updated)\\n\\nNew content...",
          "file_hash": "a591a6d40bf420404a011733cfb7b190..."
        }
        ```
    """
    start_time = datetime.now(timezone.utc)

    try:
        # Validate path
        if not validate_path(params.path):
            raise InvalidPathError(params.path, "Path contains invalid characters or traversal attempts")

        # Build full path
        full_path = f"books/{params.book_id}/{params.path}"

        # Get operator
        op = get_operator()

        # If file_hash provided, verify it matches (conflict detection)
        if params.file_hash:
            try:
                existing_content = await op.read(full_path)
                existing_hash = compute_sha256(existing_content)

                if existing_hash != params.file_hash:
                    # Conflict detected
                    await log_operation(
                        operation=OperationType.WRITE_CONTENT,
                        path=full_path,
                        agent_id="system",
                        status=OperationStatus.CONFLICT,
                        error_message=f"Hash mismatch: expected {params.file_hash}, got {existing_hash}"
                    )

                    raise ConflictError(full_path, params.file_hash, existing_hash)

            except FileNotFoundError:
                # File doesn't exist, can't verify hash - treat as create
                pass

        # Write content
        content_bytes = params.content.encode('utf-8')
        await op.write(full_path, content_bytes)

        # Get metadata of written file
        metadata = await op.stat(full_path)
        new_hash = compute_sha256(content_bytes)

        # Log success
        execution_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
        await log_operation(
            operation=OperationType.WRITE_CONTENT,
            path=full_path,
            agent_id="system",
            status=OperationStatus.SUCCESS,
            execution_time_ms=execution_time
        )

        # Build response
        response = {
            "status": "success",
            "path": full_path,
            "file_size": metadata.content_length,
            "file_hash": new_hash,
            "mode": "updated" if params.file_hash else "created"
        }

        return json.dumps(response, indent=2)

    except ConflictError:
        raise  # Re-raise ConflictError as-is

    except Exception as e:
        # Log error
        await log_operation(
            operation=OperationType.WRITE_CONTENT,
            path=f"books/{params.book_id}/{params.path}",
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message=str(e)
        )

        return f"Error writing content: {type(e).__name__}: {str(e)}"


@mcp.tool(
    name="delete_content",
    annotations={
        "title": "Delete Lesson Content",
        "readOnlyHint": False,
        "destructiveHint": True,
        "idempotentHint": True,
        "openWorldHint": False
    }
)
async def delete_content(params: DeleteContentInput) -> str:
    """Delete lesson content file.

    Idempotent: Deleting non-existent file returns success.

    Args:
        params (DeleteContentInput): Validated input containing:
            - book_id (str): Book identifier
            - path (str): Lesson path to delete

    Returns:
        str: Success confirmation message

    Example:
        ```
        Input: {"book_id": "ai-native-python", "path": "lessons/part-1/chapter-01/lesson-01.md"}
        Output: {"status": "success", "path": "books/ai-native-python/...", "existed": true}
        ```
    """
    start_time = datetime.now(timezone.utc)

    try:
        # Validate path
        if not validate_path(params.path):
            raise InvalidPathError(params.path, "Path contains invalid characters or traversal attempts")

        # Build full path
        full_path = f"books/{params.book_id}/{params.path}"

        # Get operator
        op = get_operator()

        # Check if file exists
        existed = True
        try:
            await op.stat(full_path)
        except:
            existed = False

        # Delete file (idempotent)
        await op.delete(full_path)

        # Log success
        execution_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
        await log_operation(
            operation=OperationType.DELETE_CONTENT,
            path=full_path,
            agent_id="system",
            status=OperationStatus.SUCCESS,
            execution_time_ms=execution_time
        )

        # Build response
        response = {
            "status": "success",
            "path": full_path,
            "existed": existed,
            "message": f"File {'deleted' if existed else 'did not exist (idempotent delete)'}"
        }

        return json.dumps(response, indent=2)

    except Exception as e:
        # Log error
        await log_operation(
            operation=OperationType.DELETE_CONTENT,
            path=f"books/{params.book_id}/{params.path}",
            agent_id="system",
            status=OperationStatus.ERROR,
            error_message=str(e)
        )

        return f"Error deleting content: {type(e).__name__}: {str(e)}"
