from fastmcp import FastMCP
from server import search_users, create_user, get_user
import sys

mcp = FastMCP(name="MyServer")

if __name__ == "__main__":
    # Defaults to STDIO transport
    """     users = [
        ("João Silva", "joao@email.com", "backend developer with Python expertise"),
        ("Maria Santos", "maria@email.com",
         "frontend developer with React and TypeScript"),
        ("Pedro Oliveira", "pedro@email.com",
         "data scientist with machine learning experience"),
        ("Ana Costa", "ana@email.com", "backend developer focused on AI and LLMs"),
        ("Lucas Ferreira", "lucas@email.com",
         "devops engineer with Kubernetes and Docker"),
    ]

    for name, email, description in users:
        create_user(name, email, description) """

    get_Similar_users = search_users("backend", top_k=5)
    print("Search users by query 'backend':",
          get_Similar_users, file=sys.stderr)

    get_user_id = get_user(user_id=2)
    print("Get user by ID:", get_user_id, file=sys.stderr)

    # mcp.run()

    # Or use HTTP transport
    # mcp.run(transport="http", host="127.0.0.1", port=9000)
