from usuarios import acciones

print("""
Acciones Disponibles, Selecciona una opcion:
    1 - Registrarse
    2 - Login
""")

acc = acciones.Acciones()

accion = input("¿Qué acción desea hacer? ")
if accion == '1':
    acc.registro()

else:
    acc.login()
    