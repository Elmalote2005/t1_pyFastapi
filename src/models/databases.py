from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

MONGO_URI = "mongodb+srv://santiagozapata5000_db_user:DdkohzqBJWhfyojp@cluster0.bvjdyrp.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
db = client.data_ap
collection = db.trainee

try:
    # Verificar conexión
    client.admin.command("ping")
    print("Conexión exitosa a MongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error al conectar MongoDB: {e}")