#instalar paqueteria mysql-connector-python
from mysql.connector import connect, Error

def conectar():
    try:
        db_conexion = connect(host="127.0.0.1", user="root", password="danielacastillo22", databases="school_management", port=3306)
        #para conectarse con mysql    #el puerto es opcional, pero se puede poner cuando se camnia el puerto de mysql
        print(db_conexion)
        return db_conexion
    except Error as e:
        print(e)


def insertar():
    conexion = conectar()
    if conexion.is_connected():
          cursor = conexion.cursor()
          sql = "INSERT into nombre de la tabla(lo que quieres de la tabla) VALUES (%s,%s,%s)" #%s es para mostrar las variables de la tabla
          valores = ("valores") #esto es una tupla
          cursor.execute(sql, valores)
          cursor.commit()
          cursor.close()
          conexion.close()



def insertar_muchos():
    conexion = conectar()
    if conexion.is_connected():
        cursor = conexion.cursor()
        sql = "INSERT into nombre de la tabla(lo que quieres de la tabla) VALUES (%s,%s,%s)"
        valores = [("Pedro", 19,38),("Luisa", 45,34)]     #tener los valores construidos
        cursor.excutemany(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()


def consultar():
    conexion = conectar()
    if conexion.is_connected():
        cursor = conexion.cursor()
        sql = "select * from nombre"
        cursor.execute(sql)
        resultado = cursor.fetchall() #para retornar
        for registro in resultado:
            print(resultado[1], "-------", registro[95])
        cursor.close()
        conexion.close()


if __name__ == "__main__":
    conectar()
    insertar()
    insertar_muchos()
    consultar()