from fastmcp import FastMCP

from database import insert_user


mcp = FastMCP(name="MyAssistantServer")
mcp.enable(tags={"public"}, only=True)


mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
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
