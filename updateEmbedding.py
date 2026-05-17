import chromadb

client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_collection(name="vehicles_embeddings")      

collection.update(
    ids=["1","2","3"],  # ID of the record to update (Car and Bike)
    documents=["Car has four wheels", "Bike has two wheels", "Bus has many wheels"],  # New document value
    metadatas=[{"type": "land", "fuel": "Diesel"}, {"type": "land", "fuel": "Petrol"}, {"type": "land", "fuel": "Diesel"} ]
)

print("Documents updated in the collection with new metadata and embeddings.")