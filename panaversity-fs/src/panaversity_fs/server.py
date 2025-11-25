"""FastMCP server for PanaversityFS.

Main entry point for the MCP server with Stateless Streamable HTTP transport.
"""

from panaversity_fs.app import mcp  # Import from app.py to avoid double-import issue
from panaversity_fs.config import get_config
import sys


def main():
    """Run the MCP server.

    Usage:
        python -m panaversity_fs.server

    Server runs at http://0.0.0.0:8000/mcp by default.
    Configure via environment variables (PANAVERSITY_*).
    """
    try:
        # Load and validate configuration
        config = get_config()

        print(f"PanaversityFS MCP Server", file=sys.stderr)
        print(f"Storage Backend: {config.storage_backend}", file=sys.stderr)
        print(f"Server: http://{config.server_host}:{config.server_port}/mcp", file=sys.stderr)
        print(f"Auth: {'Enabled (API Key)' if config.api_key else 'Disabled (Dev Mode)'}", file=sys.stderr)
        print(f"", file=sys.stderr)
        # Import all tool modules to register tools (10 tools total)
        # This must happen after mcp is created (which is now in app.py)
        from panaversity_fs.tools import content    # read, write, delete (also handles summaries)
        from panaversity_fs.tools import assets     # upload, get, list
        from panaversity_fs.tools import registry   # list_books
        from panaversity_fs.tools import search     # glob, grep
        from panaversity_fs.tools import bulk       # get_book_archive

        print(f"Tools: {len(mcp._tool_manager._tools)} registered", file=sys.stderr)
        print(f"Starting server...", file=sys.stderr)

        # Run server with streamable HTTP transport
        mcp.run(transport="streamable-http")

    except Exception as e:
        print(f"ERROR: Failed to start server: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
