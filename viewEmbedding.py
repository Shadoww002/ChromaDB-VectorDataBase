import chromadb
client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_collection(name="vehicles_embeddings")
print(collection)

data = collection.get(include=["documents", "metadatas", "embeddings"])

for doc, meta, emb in zip(data["documents"], data["metadatas"], data["embeddings"]):
    print(f"Document: {doc}")
    print(f"Metadata: {meta}")
    print(f"Embedding: {emb[:10]}")
    print("-" * 40) 