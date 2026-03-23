from fastmcp import FastMCP
import json
import sys

from embeddings import generate_embedding
from vector_store import search_index
from database import users_by_faiss, get_user_by_id, init_db

from database import insert_user


mcp = FastMCP(name="MyAssistantServer")
init_db()


@mcp.tool
def create_user(name: str, email: str, description: str) -> dict:
    try:
        user_id = insert_user(name, email, description)

        return {"id": user_id, "name": name}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool
def search_users(query: str, top_k: int) -> json:
    query_embedding = generate_embedding(query)
    # pesquiso indice faiss
    faiss_indices = search_index(query_embedding, top_k)

    # retorno usuarios do sqlite correspondentes aos indices faiss
    similar_users = users_by_faiss(faiss_indices)

    return json.dumps(similar_users)


@mcp.tool
def get_user(user_id: int) -> dict:

    try:
        match_user = get_user_by_id(user_id)

        print(f"Retrieved user for ID {user_id}: {match_user}", file=sys.stderr)
        return match_user
    except Exception as e:
        print(f"Error retrieving user with ID {user_id}: {e}", file=sys.stderr)
        return {"error": str(e)}


mcp.run()

# Or use HTTP transport
# mcp.run(transport="http", host="127.0.0.1", port=9000)
