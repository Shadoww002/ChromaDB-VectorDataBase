import chromadb

client = chromadb.PersistentClient(path="./my_chroma_db")

collection = client.get_collection(name="vehicles")
print(collection)


data = collection.get() 
print("Data in collection:")
print(data)


for i , doc in enumerate(data['documents'] ):
    print(f"ID: {data['ids'][i]}, Document: {doc}")