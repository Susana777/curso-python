

tareas = []  


def agregar_tarea():
    
    nombre = input("Nombre de la tarea: ").strip()
    if not nombre:
        print("La tarea necesita un nombre\n")
        return "Intenta de nuevo"
    tareas.append({"nombre": nombre, "completada": False})
    print("Tarea agregada\n")


def listar_tareas():
    
    if not tareas:
        print("No hay tareas registradas\n")
        return
    print("\n#   Estado   Descripcion")
    for indice, tarea in enumerate(tareas, start=1):
        estado = "x" if tarea["completada"] else " "
        print(f"{indice}    [{estado}]    {tarea['nombre']}")
  


def completar_tarea():
    
    listar_tareas()
    if not tareas:
        return
    try:
        numero = int(input("Número de la tarea a marcar como completada: "))
    except ValueError:
        print("Numero invalido\n")
        return
    if 1 <= numero <= len(tareas):
        tareas[numero - 1]["completada"] = True
        print("Tarea marcada como completada\n")
    else:
        print("No existe una tarea con ese número\n")


def eliminar_tarea():
    
    listar_tareas()
    if not tareas:
        return
    try:
        numero = int(input("Numero de la tarea a eliminar: "))
    except ValueError:
        print("Numero inválido\n")
        return
    if 1 <= numero <= len(tareas):
        tareas.pop(numero - 1)
        print("Tarea eliminada\n")
    else:
        print("No existe una tarea con ese numero\n")


def mostrar_menu():
    print("----Gestor de Tareas----")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")



while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ").strip()

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("Opcion invalida, intenta de nuevo\n")


