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
    
    # Set environment variables BEFORE any FastMCP operations
    if railway_port := os.environ.get("PORT"):
        host = os.environ.get("FASTMCP_HOST", "0.0.0.0")
        port = int(railway_port)
        
        print(f"Railway deployment - port {port}")
        
        # Set multiple environment variables that different systems might read
        env_vars = {
            "UVICORN_HOST": host,
            "UVICORN_PORT": str(port),
            "HOST": host,
            "PORT": str(port),
            "FASTMCP_HOST": host,
            "FASTMCP_PORT": str(port)
        }
        
        for key, value in env_vars.items():
            os.environ[key] = value
            print(f"Set {key}={value}")
    
    # Always call mcp.run the same way
    if os.environ.get("PORT"):
        mcp.run(transport="sse")
    else:
        mcp.run()

if __name__ == "__main__":
    main()