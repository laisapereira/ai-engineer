from fastmcp import FastMCP
from database import init_db, insert_user
import sys

mcp = FastMCP(name="MyServer")
init_db()


@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Defaults to STDIO transport

    user_id = insert_user("Lila Teste", "li4era.teste@example.com",
                          "A software developer with a passion for AI.")

    # mcp.run()

    # Or use HTTP transport
    # mcp.run(transport="http", host="127.0.0.1", port=9000)
