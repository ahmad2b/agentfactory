"""MCP tools for PanaversityFS.

This package contains all MCP tool implementations organized by category:
- content.py: Content operations (read/write/delete)
- assets.py: Asset management (upload/get/list)
- summaries.py: Summary operations (add/update/get/list)
- bulk.py: Bulk operations (get_book_archive)
- registry.py: Registry operations (list_books)
- search.py: Search operations (glob/grep_search)

Each tool module imports the shared FastMCP instance from server.py
and registers tools using @mcp.tool decorator.
"""

__all__ = []
