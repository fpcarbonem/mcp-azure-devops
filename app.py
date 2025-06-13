import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mcp.server.fastmcp import FastMCP
from mcp_azure_devops.features import register_all
from mcp_azure_devops.utils import register_all_prompts

# Create server
mcp = FastMCP("Azure DevOps")
register_all(mcp)
register_all_prompts(mcp)

@mcp.get("/health")
async def health():
    return {"status": "healthy"}

@mcp.get("/")
async def root():
    return {"message": "Azure DevOps MCP Server"}

# Export app
app = mcp._mcp_server