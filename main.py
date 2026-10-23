from src.templates.controllers import (
    create_trainee, get_all_trainees,
    get_trainee_by_id, update_trainee, delete_trainee
)
from src.models.model import TraineeModel, traineeUpdateModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI(
    title="Gestion de datos de los aprendices",
    description="API simple con FastAPI para consumir los datos de los aprendices",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "API simple con FastApi"}

@app.post(
    "/trainee/",
    response_description="Registrar un nuevo aprendiz",
    status_code=status.HTTP_201_CREATED
)
def create_trainee_api(trainee: TraineeModel):
    return create_trainee(trainee)

@app.get("/trainee/")
def get_all_trainees_api():
    return get_all_trainees()

@app.get("/trainee/{trainee_id}")
def get_trainee_by_id_api(trainee_id: str):
    return get_trainee_by_id(trainee_id)

@app.put("/trainee/{trainee_id}")
def update_trainee_api(trainee_id: str, trainee: traineeUpdateModel):
    return update_trainee(trainee_id, trainee)

@app.delete("/trainee/{trainee_id}")
def delete_trainee_api(trainee_id: str):
    return delete_trainee(trainee_id)