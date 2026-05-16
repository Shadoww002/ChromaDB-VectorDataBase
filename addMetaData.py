import chromadb
client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_collection(name="vehicles")
print(collection)

## add metadata to collection
collection.update(
    documents=[
        "car runs on road",
        "boat runs on water",
        "plane runs in air",
        "bus is a public transport on road",
        "train runs on rail",
    ],
    ids=["car", "boat", "plane", "bus", "train"],
    metadatas=[
        {"type": "land","fuel": "petrol"},
        {"type": "water","fuel": "diesel"},
        {"type": "air","fuel": "kerosene"},
        {"type": "land","fuel": "electric"},
        {"type": "rail","fuel": "electric"},
    ]
)

print("\nData with metadata added to collection successfully.")

##view collection data with metadata
data = collection.get(include=["documents", "metadatas"])
print("\nData in collection with metadata:")
for doc , meta, id in zip(data['documents'], data['metadatas'], data['ids']):
    print(f"ID: {id} |   Document: {doc}  |   Metadata: {meta}")