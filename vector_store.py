import faiss
import numpy as np
import os

dimensions = 1536

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "faiss_index", "index.bin")
os.makedirs(os.path.join(BASE_DIR, "faiss_index"), exist_ok=True)

if os.path.exists(INDEX_PATH):
    index_faiss = faiss.read_index(INDEX_PATH)
else:
    index_faiss = faiss.IndexFlatL2(dimensions)


def add_embedding_to_index(embedding):

    embedding_array = np.array([embedding]).astype(
        'float32')  # shape (1, 1536)
    index_faiss.add(embedding_array)

    faiss.write_index(index_faiss, INDEX_PATH)

    real_index = index_faiss.ntotal - 1

    return real_index
