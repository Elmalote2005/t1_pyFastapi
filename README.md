# API de Gestión de Aprendices — FastAPI

> Proyecto académico desarrollado con FastAPI, MongoDB y Python para la administración de datos de aprendices.

---

## 📋 Descripción
API RESTful que permite gestionar el registro, consulta, actualización y eliminación de información de aprendices. Incluye validación de datos, documentación interactiva y una interfaz de consola para gestión local.

---

## 🚀 Enlaces del Proyecto
- **API en producción:** https://t1-pyfastapi.onrender.com
- **Documentación interactiva:** https://t1-pyfastapi.onrender.com/docs
- **Repositorio GitHub:** https://github.com/Elmalote2005/t1_pyFastapi

---

## 📂 Estructura del Proyecto
t1_pyFastapi/
├── main.py # Punto de entrada de la API
├── requirements.txt # Dependencias del proyecto
├── README.md # Documentación
└── src/
├── models/
│ ├── model.py # Esquemas y validaciones con Pydantic
│ └── databases.py # Conexión a MongoDB
├── templates/
│ └── controllers.py # Lógica de negocio (CRUD)
└── views/
└── view.py # Interfaz de consola
plaintext

---

## ⚙️ Instalación y Ejecución Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/Elmalote2005/t1_pyFastapi.git
cd t1_pyFastapi
2. Crear y activar entorno virtual
bash
python -m venv venv
venv\Scripts\activate
3. Instalar dependencias
bash
pip install -r requirements.txt
4. Configurar conexión a MongoDB
La cadena de conexión se encuentra en src/models/databases.py. Si es necesario, actualiza el valor de MONGO_URI con tus credenciales.
5. Iniciar la API
bash
uvicorn main:app --reload
La API estará disponible en: http://127.0.0.1:8000
6. Ejecutar la interfaz de consola (en otra terminal)
bash
python src/views/view.py
El menú permite registrar, listar, buscar, actualizar y eliminar aprendices.
📡 ¿Cómo funciona la API? — Endpoints y Ejemplos
Ruta Raíz
GET / → Devuelve mensaje de confirmación de funcionamiento
json
{
  "message": "API simple con FastApi"
}
1. Registrar un Aprendiz
POST /trainee/
Cuerpo de la solicitud:
json
{
  "document": "123456789",
  "name": "María",
  "lastname": "López",
  "email": "maria@ejemplo.com",
  "age": 20,
  "program": "Análisis y Desarrollo de Software",
  "record_number": 549428
}
Respuesta: Mensaje de confirmación y datos registrados con ID generado
2. Listar Todos los Aprendices
GET /trainee/
Devuelve lista completa con mensaje, total de registros y arreglo de datos
3. Consultar Aprendiz por ID
GET /trainee/{trainee_id}
Reemplaza {trainee_id} por el ID del registro
Devuelve los datos del aprendiz o mensaje de no encontrado
4. Actualizar Datos
PUT /trainee/{trainee_id}
Solo envía los campos que deseas modificar:
json
{
  "email": "nuevo@ejemplo.com",
  "program": "Ingeniería de Software"
}
5. Eliminar Registro
DELETE /trainee/{trainee_id}
Elimina el aprendiz y devuelve mensaje de confirmación
🗄️ Base de Datos
Motor: MongoDB
Base de datos: data_ap (se crea automáticamente al primer registro)
Colección: trainee
La conexión es compartida por la API y la consola → todo se guarda en la misma base de datos
📝 Historial de Cambios
fear → Se corrigieron archivos que no permitían la funcionalidad de la API
👤 Autor
Nombre: Santiago Zapata
Institución: SENA — Servicio Nacional de Aprendizaje
Proyecto: Formación en Desarrollo de Software
