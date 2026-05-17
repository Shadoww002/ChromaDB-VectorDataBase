import chromadb
client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_or_create_collection(name="vehicles_semantic_search")
print(collection)

collection.add(
    ids=["Car", "Bike","bicycle","Bus","Boat"],
    documents=[
        "A car is a four-wheeled vehicle that is used for transportation.it uses Diesel or Petrol as fuel.",
        "A bike is a two-wheeled vehicle that is powered by engine.it uses Petrol or Electric as fuel.",
        "A bicycle is a two-wheeled vehicle that is powered by pedaling.it does not use any fuel.",
        "A bus is a large vehicle that is used for public transportation.it uses Diesel as fuel.",
        "A boat is a watercraft that is used for transportation on water.it uses Diesel as fuel."
    ],
)

print("Documents added to the collection for semantic search.") 

#search Query
query = "What is a vehicle that does not use fuel"
results = collection.query(
    query_texts=[query],
    n_results=3
)   

print("Search results for the query:")
for doc ,dist in zip(results['documents'][0], results['distances'][0]):
    print(f"Document: {doc}, Distance: {dist}") 