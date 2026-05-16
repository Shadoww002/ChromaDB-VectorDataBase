import chromadb
client = chromadb.PersistentClient(path="./my_chroma_db")   
collection = client.get_collection(name="vehicles")
print(collection)   

## update collection

collection.update(
    ids=["bus"],
    documents=["bus is a public transport on road and it can carry more than 50 passengers"]
)

print("Collection updated successfully.")

record = collection.get(ids=["bus"])
print("Updated record:")
print(record)