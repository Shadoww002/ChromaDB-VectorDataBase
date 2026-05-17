import chromadb

client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_or_create_collection(name="vehicles_embeddings")
print(collection)

# Adding some records with metadata and embeddings

collection.add(
    documents=["Car", "Bike", "Bus"],   
    metadatas=[
        {"type": "land", "fuel": "gasoline"},
        {"type": "land", "fuel": "electric"},
        {"type": "land", "fuel": "diesel"}
    ],
    ids=["1", "2", "3"],
    # embeddings=[
    #     [0.1, 0.2, 0.3],  # Embedding for Car
    #     [0.4, 0.5, 0.6],  # Embedding for Bike
    #     [0.7, 0.8, 0.9]   # Embedding for Bus
    # ]
)   

print("Documents added to the collection with metadata and embeddings.")
