from openai import OpenAI
import sys

from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1536 dimensõe

def generate_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )

    generated_embedding = response.data[0].embedding
    print(f"Generated embedding for text: {text}", file=sys.stderr)
    return generated_embedding
