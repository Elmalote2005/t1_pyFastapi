from bson import ObjectId
from src.models.databases import collection
from src.models.model import TraineeModel, traineeUpdateModel

def helper_trainee(trainee)->dict:
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