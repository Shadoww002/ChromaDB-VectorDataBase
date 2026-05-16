import chromadb

client = chromadb.PersistentClient(path="./my_chroma_db")

collection = client.get_or_create_collection(name="vehicles")
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

print("Data added to collection successfully.")

data = collection.get() 
print("Data in collection:")
print(data)



for i , doc in enumerate(data['documents'] ):
    print(f"ID: {data['ids'][i]}, Document: {doc}")