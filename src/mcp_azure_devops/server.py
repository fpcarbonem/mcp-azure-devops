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
    
    # Check if running on Railway
    if os.environ.get("PORT"):
        # Railway deployment - use SSE transport
        print(f"Detected Railway deployment - using SSE transport on port {os.environ.get('PORT')}")
        mcp.run(transport="sse")
    else:
        # Local development - use stdio transport
        print("Starting MCP server for local development with stdio transport")
        mcp.run()

if __name__ == "__main__":
    main()