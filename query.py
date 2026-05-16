import chromadb 
client = chromadb.Client()

#create collection
collection = client.create_collection(name="vehicles")
print(collection)

## add data to collection

collection.add(
    documents=[
        "car runs on road",
        "boat runs on water",
        "plane runs in air",
        "bus is a public transport on road",
        "train runs on rail",
    ],
    ids=["car", "boat", "plane", "bus", "train"]
    
)
## query collection
results = collection.query(
    query_texts=["which will carry more passengers?"],
    n_results=2
)
print(results)
print("-----------------------------")
print(results.keys())