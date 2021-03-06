from unittest import result
import mysql.connector
import datetime
import hashlib

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "master_python",
    port = 3306
)

#Cursor para realizar varias consultas
cursor = db.cursor(buffered=True)


class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    
    def registrar(self):

        #cifrado  de contraseña
        passCifrada = hashlib.sha256()
        passCifrada.update(self.password.encode('utf8'))
        fecha = datetime.datetime.now()

        sql = "INSERT INTO usuarios VALUES (null,%s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, passCifrada.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            db.commit()

            #Guardamos en una lista con la cantidad de registros que se halla modificado
            #y el objeto
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result


    def identificar(self):
        return self.nombre

