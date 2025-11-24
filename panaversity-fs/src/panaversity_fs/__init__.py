"""PanaversityFS - Agent-Native Multi-Book Storage System.

This package provides a Python MCP server for unified storage operations
across multiple backends (Local, R2, S3, Supabase) using OpenDAL abstraction.

Architecture:
- FastMCP server with Stateless Streamable HTTP transport
- OpenDAL AsyncOperator for storage abstraction
- Pydantic models for validation
- JSONL audit logging with eventual consistency

MCP Tools (14 total):
- Content: read_content, write_content, delete_content
- Assets: upload_asset, get_asset, list_assets
- Summaries: add_summary, update_summary, get_summary, list_summaries
- Bulk: get_book_archive
- Registry: list_books
- Search: glob_search, grep_search
- Audit: get_audit_log (deferred to post-MVP per tasks.md)
"""

__version__ = "0.1.0"
__author__ = "Panaversity"
__license__ = "MIT"

from panaversity_fs.config import Config
from panaversity_fs.storage import get_operator

__all__ = ["Config", "get_operator", "__version__"]
