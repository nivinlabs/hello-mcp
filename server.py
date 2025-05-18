import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    # Run FastMCP server binding to 0.0.0.0 and correct port
    mcp.run(host="0.0.0.0", port=port)
