"""FastMCP server for PanaversityFS.

Main entry point for the MCP server with Stateless Streamable HTTP transport.
"""

from panaversity_fs.app import mcp  # Import from app.py to avoid double-import issue
from panaversity_fs.config import get_config

# Load and validate configuration
config = get_config()

streamable_http_app = mcp.streamable_http_app()

if __name__ == "__main__":
    """Run the MCP server.
    
    Usage:
        python -m panaversity_fs.server
    
    Server runs at http://0.0.0.0:8000/mcp by default.
    Configure via environment variables (PANAVERSITY_*).
    """
    import uvicorn
    
    print("PanaversityFS MCP Server")
    print(f"Storage Backend: {config.storage_backend}")
    print(f"Server: http://{config.server_host}:{config.server_port}/mcp")
    print(f"Auth: {'Enabled (API Key)' if config.api_key else 'Disabled (Dev Mode)'}")
    print(f"Tools: {len(mcp._tool_manager._tools)} registered")
    uvicorn.run("src.panaversity_fs.server:streamable_http_app", host="0.0.0.0", port=config.server_port, reload=True)