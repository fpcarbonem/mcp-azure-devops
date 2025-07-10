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
    parser = argparse.ArgumentParser(
        description="Run the Azure DevOps MCP server")
    parser.add_argument("--transport", default="stdio", 
                       choices=["stdio", "sse", "http"],
                       help="Transport method to use")
    parser.add_argument("--host", default="localhost",
                       help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000,
                       help="Port to bind to")
    
    args = parser.parse_args()
    
    # Check if running on Railway (or similar cloud platform)
    if railway_port := os.environ.get("PORT"):
        # Railway deployment - override with environment settings
        host = os.environ.get("FASTMCP_HOST", "0.0.0.0")
        port = int(railway_port)
        transport = "sse"  # Use SSE for Railway
        print(f"Detected Railway deployment - using SSE transport on {host}:{port}")
    else:
        # Use command line arguments or defaults
        host = args.host
        port = args.port
        transport = args.transport
        print(f"Local development - using {transport} transport")
    
    # Start the server with appropriate transport
    if transport == "sse":
        mcp.run(transport="sse", host=host, port=port)
    elif transport == "http":
        mcp.run(transport="http", host=host, port=port)
    else:
        # stdio transport (default for local development)
        mcp.run()

if __name__ == "__main__":
    main()