from fastmcp import FastMCP
import json

from embeddings import generate_embedding
from vector_store import search_index
from database import users_by_faiss

from database import insert_user


mcp = FastMCP(name="MyAssistantServer")
mcp.enable(tags={"public"}, only=True)


mcp_with_instructions = FastMCP(
    name="MCP-CRM",
    instructions="""
        This server provides data analysis tools.
        Call get_average() to analyze numerical data.
    """,
)


@mcp.tool
def create_user(name: str, email: str, description: str) -> dict:
    try:
        user_id = insert_user(name, email, description)

        return {"id": user_id, "name": name}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool
def search_user(query: str, top_k: int) -> json:
    query_embedding = generate_embedding(query)
    # pesquiso indice faiss
    faiss_indices = search_index(query_embedding, top_k)

    # retorno usuarios do sqlite correspondentes aos indices faiss
    similar_users = users_by_faiss(faiss_indices)

    return json.dumps(similar_users)
