print("""
Acciones Disponibles, Selecciona una opcion:
    1 - Registrarse
    2 - Login
""")

accion = input("¿Qué acción desea hacer? ")
if accion == '1':
    print('\nPor favor ingresa los datos:')

    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    email = input('Ingresa tu email: ')
    password = input('Ingresa tu contraseña: ')