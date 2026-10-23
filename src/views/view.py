import requests

BASE_URL = "http://127.0.0.1:8000"

def menu_principal():
    print("=" * 50)
    print("       GESTION DE APRENDICES (CONSOLA)")
    print("=" * 50)
    print("1. Registrar nuevo aprendiz")
    print("2. Listar todos los aprendices")
    print("3. Buscar aprendiz por ID")
    print("4. Actualizar aprendiz")
    print("5. Eliminar aprendiz")
    print("6. Salir")
    print("=" * 50)

def registrar_aprendiz():
    print("\n--- Registrar nuevo aprendiz ---")
    doc = input("Documento: ")
    nom = input("Nombre: ")
    ape = input("Apellido: ")
    corr = input("Email: ")
    edad = input("Edad: ")
    prog = input("Programa: ")
    ficha = input("Numero de ficha: ")

    datos = {
        "document": doc, "name": nom, "lastname": ape,
        "email": corr, "age": int(edad), "program": prog,
        "record_number": int(ficha)
    }
    try:
        res = requests.post(f"{BASE_URL}/trainee/", json=datos)
        respuesta = res.json()
        print(respuesta.get("mensaje", "Operacion completada"))
        if respuesta.get("datos"):
            print(f"ID: {respuesta['datos'].get('id')}")
    except Exception as e:
        print(f"Error: {e}")

def listar_aprendices():
    print("\n--- Lista de Aprendices ---")
    try:
        res = requests.get(f"{BASE_URL}/trainee/")
        respuesta = res.json()
        print(respuesta.get("mensaje", ""))
        aprendices = respuesta.get("datos", [])
        if not aprendices:
            print("No hay aprendices registrados")
            return
        for t in aprendices:
            print(f"ID: {t.get('id')} | {t.get('name')} {t.get('lastname')} | {t.get('program')}")
        print(f"Total: {respuesta.get('total', len(aprendices))}")
    except Exception as e:
        print(f"Error: {e}")

def buscar_por_id():
    print("\n--- Buscar Aprendiz por ID ---")
    aid = input("Ingrese el ID: ")
    try:
        res = requests.get(f"{BASE_URL}/trainee/{aid}")
        respuesta = res.json()
        print(respuesta.get("mensaje", ""))
        if respuesta.get("datos"):
            t = respuesta["datos"]
            print(f"ID: {t.get('id')}")
            print(f"Documento: {t.get('document')}")
            print(f"Nombre: {t.get('name')} {t.get('lastname')}")
            print(f"Email: {t.get('email')}")
            print(f"Edad: {t.get('age')}")
            print(f"Programa: {t.get('program')}")
            print(f"Ficha: {t.get('record_number')}")
    except Exception as e:
        print(f"Error: {e}")

def actualizar_aprendiz():
    print("\n--- Actualizar Aprendiz ---")
    aid = input("Ingrese el ID: ")
    print("Deje vacio si no desea cambiar\n")
    nom = input("Nuevo nombre: ").strip()
    ape = input("Nuevo apellido: ").strip()
    corr = input("Nuevo email: ").strip()
    edad = input("Nueva edad: ").strip()
    prog = input("Nuevo programa: ").strip()

    datos = {}
    if nom: datos["name"] = nom
    if ape: datos["lastname"] = ape
    if corr: datos["email"] = corr
    if edad: datos["age"] = int(edad)
    if prog: datos["program"] = prog
    if not datos:
        print("Nada que actualizar")
        return
    try:
        res = requests.put(f"{BASE_URL}/trainee/{aid}", json=datos)
        respuesta = res.json()
        print(respuesta.get("mensaje", ""))
        if respuesta.get("datos"):
            t = respuesta["datos"]
            print(f"Actualizado: {t.get('name')} {t.get('lastname')}")
    except Exception as e:
        print(f"Error: {e}")

def eliminar_aprendiz():
    print("\n--- Eliminar Aprendiz ---")
    aid = input("Ingrese el ID: ")
    if input("Seguro? (s/n): ").lower() != "s":
        print("Cancelado")
        return
    try:
        res = requests.delete(f"{BASE_URL}/trainee/{aid}")
        respuesta = res.json()
        print(respuesta.get("mensaje", ""))
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        menu_principal()
        op = input("\nSeleccione una opcion: ")
        if op == "1": registrar_aprendiz()
        elif op == "2": listar_aprendices()
        elif op == "3": buscar_por_id()
        elif op == "4": actualizar_aprendiz()
        elif op == "5": eliminar_aprendiz()
        elif op == "6":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()