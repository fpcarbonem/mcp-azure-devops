"""
Azure DevOps MCP Server

A simple MCP server that exposes Azure DevOps capabilities.
"""
import argparse
import os

from mcp.server.fastmcp import FastMCP

from mcp_azure_devops.features import register_all
from mcp_azure_devops.utils import register_all_prompts

# Create a FastMCP server instance with a name
mcp = FastMCP("Azure DevOps")

# Adjust host and port when deployed on platforms like Railway
if port := os.environ.get("PORT"):
    # Railway provides the desired port in the PORT env var
    mcp.settings.port = int(port)
    # Bind to all interfaces if the host has not been overridden
    mcp.settings.host = os.environ.get("FASTMCP_HOST", "0.0.0.0")

# Register all features
register_all(mcp)
register_all_prompts(mcp)

def main():
    import argparse
    import os
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--transport", default="stdio")
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    # Override with Railway environment variables if present
    if os.getenv("PORT"):
        host = os.getenv("FASTMCP_HOST", "0.0.0.0")
        port = int(os.getenv("PORT"))
        transport = "sse"
    else:
        host = args.host
        port = args.port
        transport = args.transport
    
    if transport == "sse":
        mcp.run(transport=transport, host=host, port=port)
    else:
        mcp.run(transport=transport)

if __name__ == "__main__":
    main()  # Keep this line unchanged
