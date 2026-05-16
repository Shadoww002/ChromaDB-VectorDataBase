import chromadb
client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_collection(name="vehicles")
print(collection)   

## filter by metadata

##filter by trasnport type

transport = collection.get(
    where={"type": "land"}      
)
print("Land transport records:")
print(transport)     

##filter by fuel type
fuel = collection.get(
    where={"fuel": "electric"}      
)       
print("Electric fuel records:")
print(fuel)