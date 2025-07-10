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

print("FastMCP instance created")

# Register all features
register_all(mcp)
print("Features registered")

register_all_prompts(mcp)
print("Prompts registered")

def main():
    """Entry point for the command-line script."""
    port = int(os.environ.get("PORT", 8080))
    host = os.environ.get("FASTMCP_HOST", "0.0.0.0")
    
    print(f"Starting FastMCP server on {host}:{port}")
    
    # Let FastMCP handle the server itself
    mcp.run(transport="sse")

if __name__ == "__main__":
    main()