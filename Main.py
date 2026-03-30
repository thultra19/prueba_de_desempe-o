from functions import *

print('Welcome to the student registry system!')

def menu():

    print("\n--- MENU ---")
    print("1. Register a student. ")
    print("2. Consult students. ")
    print("3. Search for a student. ")
    print("4. Update student info. ")
    print("5. Delete a student from file")
    print("6. Save CSV file")
    print("7. Load CSV file")
    print("8. Exit")



lista_de_estudiantes = []
sw = True 

while sw:

    menu()

    opcion = input('Please choose an option from the ones above!\n').strip().lower()

    match opcion:
    

        case "1" | "registrar" | "register" | "add":

            nombre = input("Type in the name of the student: ")
            id = (input("Type the ID: "))
            edad = (input("Type the age of the student: "))
            programa = (input("Type down the program the student will be part of: "))
            estado = input("Please type the student's status (active/inactive): ")

            registrar_estudiante(lista_de_estudiantes, nombre, id, edad, programa, estado)

        case "2" | "consultar" | "consult":

            mostrar_estudiantes(lista_de_estudiantes)

        case "3" | "buscar" | "search" | "find":
            
            nombre = input("Type the name of the student you wish to look for: ")
            p = buscar_estudiante(lista_de_estudiantes, nombre)
            print(p if p else "Student not found")

        case "4" | "actualizar" | "update":
            
            id = input("new id (hit the enter key to skip): ")
            nombre = input("New name (hit the enter key to skip):  ")
            edad = input("New age (hit the enter key to skip):  ")
            programa = input("New program (hit the enter key to skip): ")
            estado = input("New status (hit the enter key to skip): ")

            actualizado = actualizar_estudiante(

                lista_de_estudiantes,
                
                str(nombre) if nombre else None,
                int(id) if id else None,
                int(edad) if edad else None,
                str(programa) if programa else None,
                str(estado) if estado else None
            )

        case "5" | "eliminar" | "delete":

            nombre = input("Write the name of the Student you wish to delete from file: ")
            eliminado = eliminar_estudiante(lista_de_estudiantes, nombre)
            print("Student deleted" if eliminado else "Student not found")

        case "6" | "guardar" | "save":
            ruta = input("File route: ")
            guardar_csv(lista_de_estudiantes, ruta)

        case "7" | "cargar" | "load":
            
            ruta = input("File route: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                opcion_merge = input("¿Overwrite? (Y/N): ").upper()

                if opcion_merge == "Y":
                    inventario = nuevos
                    print("list replaced.")
                else:
                    for nuevo in nuevos:
                        existente = buscar_estudiante(lista_de_estudiantes, nuevo["nombre"])
                        if existente:
                            existente["id"] += nuevo["id"]
                            existente["nombre"] = nuevo["nombre"]
                            existente["edad"] = nuevo["edad"]
                            existente["programa"] = nuevo["programa"]
                            existente["estado"] = nuevo["estado"]
                            
                        else:
                            inventario.append(nuevo)

                    print("list merged.")

        case "8" | "salir" | "exit":
            print('Thank you for using the software!')
            print('Exiting...')
            sw = False
