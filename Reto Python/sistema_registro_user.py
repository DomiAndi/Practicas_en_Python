print("""
     ######################################################### 
     ###            Sistema de Registro de Usuarios         ###  
     #########################################################""")

# Lista para almacenar los usuarios como diccionarios
lista_usuarios = []

# Función para registrar nuevos usuarios
def new_user():
    numero_usuarios = int(input("¿Cuántos Usuarios Desea Registrar?: "))
    
    for i in range(1, numero_usuarios + 1):
        usuario = {}
        id_unico = i
        usuario['id'] = id_unico
        usuario['nombres'] = input("Ingrese su Nombre o Nombres (entre 5 y 50 caracteres): ")
        usuario['apellidos'] = input("Ingrese sus Apellidos (entre 5 y 50 caracteres): ")
        
        while True:
            telefono_usuario = input("Ingrese su Número de Teléfono (10 dígitos): ")
            if telefono_usuario.isdigit() and len(telefono_usuario) == 10:
                usuario['telefono'] = int(telefono_usuario)
                break
            else:
                print("Error: El número de teléfono debe contener 10 dígitos.")
        
        while True:
            correo_usuario = input("Ingrese su Correo Electrónico (entre 5 y 50 caracteres): ")
            if 5 <= len(correo_usuario) <= 50 and "@" in correo_usuario:
                usuario['correo'] = correo_usuario
                break
            else:
                print("Error: La longitud del correo electrónico debe estar entre 5 y 50 caracteres y debe contener '@'.")
        
        lista_usuarios.append(usuario)

    print("Registro de usuarios completado.")
    list_users()

# Función para mostrar todos los IDs de usuarios
def list_users():
    print("Lista de IDs únicos:")
    for usuario in lista_usuarios:
        print(f"ID: {usuario['id']}")

# Función para mostrar información de un usuario por su ID
def show_user():
    id_a_buscar = int(input("Ingrese el ID del usuario: "))
    for usuario in lista_usuarios:
        if usuario['id'] == id_a_buscar:
            print(f"Información del Usuario con ID {id_a_buscar}:")
            print(f"Nombre: {usuario['nombres']} {usuario['apellidos']}")
            print(f"Número de Teléfono: {usuario['telefono']}")
            print(f"Correo Electrónico: {usuario['correo']}")
            return
    print(f"No se encontró ningún usuario con el ID {id_a_buscar}.")

# Función para editar información de un usuario por su ID
def edit_user():
    id_a_buscar = int(input("Ingrese el ID del usuario que desea editar: "))
    for i, usuario in enumerate(lista_usuarios):
        if usuario['id'] == id_a_buscar:
            print(f"Editando la información del Usuario con ID {id_a_buscar}:")
            
            while True:
                nombres_usuario = input("Ingrese su Nombre o Nombres (entre 5 y 50 caracteres): ")
                if 5 <= len(nombres_usuario) <= 50:
                    break
                else:
                    print("Error: La longitud del nombre debe estar entre 5 y 50 caracteres.")
            
            while True:
                apellidos_usuario = input("Ingrese sus Apellidos (entre 5 y 50 caracteres): ")
                if 5 <= len(apellidos_usuario) <= 50:
                    break
                else:
                    print("Error: La longitud de los apellidos debe estar entre 5 y 50 caracteres.")
            
            while True:
                telefono_usuario = input("Ingrese su Número de Teléfono (10 dígitos): ")
                if telefono_usuario.isdigit() and len(telefono_usuario) == 10:
                    usuario['telefono'] = int(telefono_usuario)
                    break
                else:
                    print("Error: El número de teléfono debe contener 10 dígitos.")
            
            while True:
                correo_usuario = input("Ingrese su Correo Electrónico (entre 5 y 50 caracteres): ")
                if 5 <= len(correo_usuario) <= 50 and "@" in correo_usuario:
                    usuario['correo'] = correo_usuario
                    break
                else:
                    print("Error: La longitud del correo electrónico debe estar entre 5 y 50 caracteres y debe contener '@'.")
            
            print(f"Información actualizada para el Usuario con ID {id_a_buscar}.")
            return
    print(f"No se encontró ningún usuario con el ID {id_a_buscar}.")

# Función para eliminar un usuario por su ID
def delete_user():
    id_a_eliminar = int(input("Ingrese el ID del usuario que desea eliminar: "))
    for i, usuario in enumerate(lista_usuarios):
        if usuario['id'] == id_a_eliminar:
            del lista_usuarios[i]
            print(f"Usuario con ID {id_a_eliminar} eliminado.")
            return
    print(f"No se encontró ningún usuario con el ID {id_a_eliminar}.")

# Función para finalizar el programa
def finalizar_programa():
    print("Programa finalizado.")
    exit()

while True:
    print("\nMenú de opciones:")
    print("A.-) Registrar nuevos usuarios")
    print("B.-) Listar usuarios")
    print("C.-) Mostrar/editar usuario")
    print("D.-) Eliminar usuario")
    print("E.-) Finalizar programa")
    
    opcion_menu = input("Seleccione una opción (A/B/C/D/E): ").upper()

    if opcion_menu == 'A':
        new_user()

    elif opcion_menu == 'B':
        list_users()

    elif opcion_menu == 'C':
        show_edit_option = input("¿Desea ver (V) o editar (E) la información de un usuario? ").upper()
        if show_edit_option == 'V':
            show_user()
        elif show_edit_option == 'E':
            edit_user()

    elif opcion_menu == 'D':
        delete_user()

    elif opcion_menu == 'E':
        finalizar_programa()