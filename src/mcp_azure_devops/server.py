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

# Register all features
register_all(mcp)
register_all_prompts(mcp)

def main():
    """Entry point for the command-line script."""
    import os
    
    if railway_port := os.environ.get("PORT"):
        host = os.environ.get("FASTMCP_HOST", "0.0.0.0")
        port = int(railway_port)
        
        print(f"Railway deployment - starting server on {host}:{port}")
        
        # Run Uvicorn directly with FastMCP's app
        import uvicorn
        uvicorn.run(mcp.app, host=host, port=port, log_level="info")
    else:
        print("Local development mode")
        mcp.run()

if __name__ == "__main__":
    main()