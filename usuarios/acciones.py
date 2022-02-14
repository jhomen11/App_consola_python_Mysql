import usuarios.usuarioModel as model

class Acciones:

    def registro(self):
        print('\nPor favor ingresa los datos:')

        nombre = input('Ingresa tu nombre: ')
        apellidos = input('Ingresa tus apellidos: ')
        email = input('Ingresa tu email: ')
        password = input('Ingresa tu contraseña: ')

        #Creacion de un objeto usuario
        usuario = model.Usuario(nombre,apellidos, email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Usuario registrado correctamente")
        else:
            print(f"Registro Fallido")

    def login(self):
        print('\nIngresa tus datos para iniciar sesión')
        email = input('Ingresa tu email: ')
        password = input('Ingresa tu contraseña: ')