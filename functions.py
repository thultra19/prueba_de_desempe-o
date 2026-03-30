import csv

def registrar_estudiante(lista_de_estudiantes, nombre, id, edad, programa, estado):
    
    lista_de_estudiantes.append({
        "id": id,
        "name": nombre,
        "age": edad,
        "program": programa,
        "status" : estado, 
    })


def mostrar_estudiantes(lista_de_estudiantes):
    
    if not lista_de_estudiantes:
        print("Empty student list. ")
        return

    for p in lista_de_estudiantes:
        print(f"ID: {p['id']} - Name: {p['name']} - Age: {p['age']} - Academic program: {p['program']} - Status: {p['status']}")


def buscar_estudiante(lista_de_estudiantes, nombre):
    
    for p in lista_de_estudiantes:
        if p["name"].lower() == nombre.lower():
            return p
    return None


def actualizar_estudiante(lista_de_estudiantes, nuevo_nombre = None, nueva_id =None, nueva_edad = None, nuevo_programa =None, nuevo_estado =None):

    estudiante = buscar_estudiante(lista_de_estudiantes, nuevo_nombre)

    if estudiante:
        if nuevo_nombre is not None:
            estudiante["name"] = nuevo_nombre
        if nueva_edad is not None:
            estudiante["age"] = nueva_edad
        if nueva_id is not None:
            estudiante["id"] = nueva_id
        if nuevo_programa is not None:
            estudiante["program"] = nuevo_programa
        if nuevo_estado is not None:
            estudiante["status"] = nuevo_estado
        return True
    return False


def eliminar_estudiante(lista_de_estudiantes, nombre):
    
    estudiante = buscar_estudiante(lista_de_estudiantes, nombre)

    if estudiante:    
        lista_de_estudiantes.remove(estudiante)
        return True
    return False




def guardar_csv(lista_de_estudiantes, ruta, incluir_header=True):

    if not lista_de_estudiantes:
        print("Empty student list, saving not possible. ")
        return

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["id", "name", "age", "program", "status"])

            for p in lista_de_estudiantes:
                writer.writerow([p["id"], p["name"], p["age"], p["program"], p["status"]])

        print(f"Student list saved at: {ruta}")

    except Exception as e:
        print(f"There was an error while saving file: {e}")


def cargar_csv(ruta):
    
    lista_de_estudiantes = []
    errores = 0

    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            header = next(reader)

            if header != ["id", "name", "age", "program", "status"]:
                print("Invalid header.")
                return []

            for fila in reader:
                try:
                    if len(fila) != 5:
                        raise ValueError

                    id = fila[0]
                    nombre = fila[1]
                    edad = fila [2]
                    programa = fila[3]
                    estado= fila [4]


                    lista_de_estudiantes.append({
                    "id": id,
                    "name": nombre,
                    "age": edad,
                    "program": programa,
                    "status" : estado, 
                })

                except:
                    errores += 1

        print(f"File loaded. invalid rows: {errores}")
        return lista_de_estudiantes

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error while loading file: {e}")

    return []