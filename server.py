import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo", port=8080, host="0.0.0.0")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
