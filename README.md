# API de Gestión de Aprendices — FastAPI

Proyecto académico con FastAPI, MongoDB y Python para administrar datos de aprendices.

## 🔗 Enlaces del Proyecto
- **Despliegue en Render:** https://t1-pyfastapi.onrender.com
- **Documentación:** https://t1-pyfastapi.onrender.com/docs
- **Repositorio:** https://github.com/Elmalote2005/t1_pyFastapi

## 📂 Estructura
t1_pyFastapi/
├── main.py
├── requirements.txt
└── src/
├── models/ # Esquemas Pydantic + conexión MongoDB
├── templates/ # Lógica CRUD
└── views/ # Interfaz de consola
plaintext

## ⚙️ Ejecución Local
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
📡 Endpoints
Table
Método	Ruta	Función
GET	/	Verificar estado
POST	/trainee/	Registrar aprendiz
GET	/trainee/	Listar todos
GET	/trainee/{id}	Consultar por ID
PUT	/trainee/{id}	Actualizar datos
DELETE	/trainee/{id}	Eliminar registro
🗄️ Base de Datos
MongoDB — Base: data_ap — Colección: trainee
👤 Autor
Santiago Zapata — SENA
