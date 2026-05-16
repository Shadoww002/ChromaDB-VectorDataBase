import chromadb
client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_collection(name="vehicles")     
print(collection)

## delete collection

collection.delete(
    ids=["boat"]
) 

print("Collection deleted successfully.")
record = collection.get(ids=["boat"])
print("Deleted record:")        
print(record)


data = collection.get() 
print("Data in collection:")
print(data)



for i , doc in enumerate(data['documents'] ):
    print(f"ID: {data['ids'][i]}, Document: {doc}")