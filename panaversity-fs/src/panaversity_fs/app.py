"""FastMCP application instance for PanaversityFS.

This module holds the singleton FastMCP instance that both the server
and all tool modules import. This prevents the double-import issue
when running as `python -m panaversity_fs.server`.

Issue: When running with `-m`, Python loads the main module as `__main__`,
but when tools do `from panaversity_fs.server import mcp`, Python loads
it again as `panaversity_fs.server`, creating two different mcp instances.

Solution: Move the mcp instance to a separate module (this file) that both
server.py and tools import consistently.
"""

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with stateless HTTP transport
# This singleton is imported by all tool modules
mcp = FastMCP(
    "panaversity_fs",
    stateless_http=True,      # Enable Stateless Streamable HTTP (FR-004)
    json_response=True        # Disable SSE, use pure JSON responses
)
