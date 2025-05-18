import os
import logging
from mcp.server.fastmcp import FastMCP

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("mcp_server")

# Initialize the FastMCP server
# Using 0.0.0.0 to listen on all interfaces
host = os.environ.get("HOST", "0.0.0.0")
port = int(os.environ.get("PORT", 8080))

logger.info(f"Starting FastMCP server on {host}:{port}")
mcp = FastMCP("Demo", port=port, host=host)

@mcp.tool()
def add(a: int, b: int) -> int:
    logger.info(f"Processing add request: {a} + {b}")
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    logger.info(f"Processing greeting request for {name}")
    return f"Hello, {name}!"

if __name__ == "__main__":
    try:
        logger.info("Server starting...")
        mcp.run()
    except Exception as e:
        logger.error(f"Server error: {e}")