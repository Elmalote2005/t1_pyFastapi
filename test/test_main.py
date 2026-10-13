from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

MONGO_URI = "mongodb+srv://santiagozapata5000_db_user:DdkohzqBJWhfyojp@cluster0.bvjdyrp.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

try:
    # Verificar conexión primero
    client.admin.command("ping")
    print("Conexión exitosa a MongoDB")

    # Seleccionar base de datos y colección
    db = client['amb703']
    collection = db['mesa']

    # Crear el documento con claves entre comillas
    nueva_mesa = {
        'name': 'Santiago Avedaño Zapata',
        'status': 'Alive',
        'species': 'Human',
        'gender': 'Male'
    }

    # Insertar el documento
    resultado = collection.insert_one(nueva_mesa)
    print(f"Documento insertado en la colección 'mesa' de la base de datos 'amb703'")
    print(f"ID del documento: {resultado.inserted_id}")

except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"Error al conectar MongoDB: {e}")
finally:
    client.close()
    print("Conexión cerrada")