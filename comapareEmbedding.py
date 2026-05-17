import numpy as np
import chromadb

def cosine_similarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors."""
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0  # Avoid division by zero
    
    return dot_product / (norm_vec1 * norm_vec2)

client = chromadb.PersistentClient(path="./my_chroma_db")
collection = client.get_collection(name="vehicles_embeddings")

# Get all records with embeddings
data = collection.get(include=["documents", "metadatas", "embeddings"]) 

# Example: Compare the embedding of "Car" with "Bike" and "Bus"
car_embedding = data["embeddings"][0]  # Assuming "Car" is the first document
bike_embedding = data["embeddings"][1]  # Assuming "Bike" is the second document
bus_embedding = data["embeddings"][2]  # Assuming "Bus" is the third document 

similarity_car_bike = cosine_similarity(car_embedding, bike_embedding)
print(f"Cosine similarity between 'Car' and 'Bike': {similarity_car_bike}")

similarity_car_bus = cosine_similarity(car_embedding, bus_embedding)
print(f"Cosine similarity between 'Car' and 'Bus': {similarity_car_bus}")
