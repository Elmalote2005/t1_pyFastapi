from bson import ObjectId
from ..models.databases import collection
from ..models.model import TraineeModel, traineeUpdateModel

def helper_trainee(trainee) -> dict:
    return {
        "id": str(trainee["_id"]),
        "document": trainee["document"],
        "name": trainee["name"],
        "lastname": trainee["lastname"],
        "email": trainee["email"],
        "age": trainee["age"],
        "program": trainee["program"],
        "record_number": trainee["record_number"]
    }

# Crear datos de un Aprendiz
def create_trainee(trainee: TraineeModel):
    trainee_dict = trainee.model_dump()
    result = collection.insert_one(trainee_dict)
    new_trainee = collection.find_one({"_id": result.inserted_id})
    return {
        "mensaje": "Aprendiz creado correctamente",
        "datos": helper_trainee(new_trainee)
    }

# Obtener todos los Aprendices
def get_all_trainees():
    trainees = []
    for trainee in collection.find():
        trainees.append(helper_trainee(trainee))
    return {
        "mensaje": "Lista de aprendices obtenida correctamente",
        "total": len(trainees),
        "datos": trainees
    }

# Obtener datos del aprendiz por ID
def get_trainee_by_id(id: str):
    trainee = collection.find_one({"_id": ObjectId(id)})
    if trainee:
        return {
            "mensaje": "Aprendiz encontrado",
            "datos": helper_trainee(trainee)
        }
    return {"mensaje": "Aprendiz no encontrado", "datos": None}

# Actualizar datos del aprendiz
def update_trainee(id: str, data: traineeUpdateModel):
    data_update = {
        k: v for k, v in data.model_dump().items() if v is not None
    }
    if data_update:
        collection.update_one({"_id": ObjectId(id)}, {"$set": data_update})
    traineeUpdated = collection.find_one({"_id": ObjectId(id)})
    if traineeUpdated:
        return {
            "mensaje": "Datos actualizados correctamente",
            "datos": helper_trainee(traineeUpdated)
        }
    return {"mensaje": "Aprendiz no encontrado o sin cambios", "datos": None}

# Eliminar datos del aprendiz
def delete_trainee(id: str):
    trainee = collection.find_one({"_id": ObjectId(id)})
    if trainee:
        collection.delete_one({"_id": ObjectId(id)})
        return {"mensaje": "Aprendiz eliminado correctamente"}
    return {"mensaje": "Aprendiz no encontrado"}