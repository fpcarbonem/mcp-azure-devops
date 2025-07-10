"""
Azure DevOps MCP Server

A simple MCP server that exposes Azure DevOps capabilities.
"""
import os
from mcp.server.fastmcp import FastMCP
from mcp_azure_devops.features import register_all
from mcp_azure_devops.utils import register_all_prompts

# Create a FastMCP server instance with a name
mcp = FastMCP("Azure DevOps")

# Register all features
register_all(mcp)
register_all_prompts(mcp)

# Expose the app for Uvicorn
app = mcp.app if hasattr(mcp, 'app') else mcp

def main():
    """Entry point for the command-line script - only for local development."""
    print("Local development mode")
    mcp.run()

if __name__ == "__main__":
    main()