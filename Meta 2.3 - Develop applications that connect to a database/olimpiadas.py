# Ejercicios SQL - Python
# Hernandez Duran Jair Abdiel
# 29-03-2026
# Versión corregida sin cambiar la idea general del script

from mysql.connector import connect, Error


# -----------------------------
# Conexión
# -----------------------------
def conectar():
    try:
        db_conexion = connect(
            host="127.0.0.1",
            user="root",
            password="",  # Cambia esto si tu contraseña es otra
            database="olimpiadas",
            port=3306
        )
        print("Conexión exitosa")
        return db_conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None


def cerrar_conexion(cursor, conexion):
    if cursor:
        cursor.close()
    if conexion and conexion.is_connected():
        conexion.close()


# -----------------------------
# Ejercicio 1: Mostrar tablas
# -----------------------------
def mostrar_tablas():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            cursor.execute("SHOW TABLES")
            tablas = cursor.fetchall()

            print("\nTablas en la base de datos:")
            for tabla in tablas:
                print(f"- {tabla[0]}")
    except Error as e:
        print(f"Error al mostrar tablas: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


# -----------------------------
# Ejercicio 2: Crear tablas
# -----------------------------
def crear_tabla_olimpiada():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            sql = """
            CREATE TABLE IF NOT EXISTS Olimpiada (
                id INT AUTO_INCREMENT PRIMARY KEY,
                year_olimpiada INT NOT NULL,
                UNIQUE (year_olimpiada),
                CHECK (year_olimpiada > 0)
            )
            """
            cursor.execute(sql)
            conexion.commit()
            print("Tabla 'Olimpiada' creada o ya existente")
    except Error as e:
        print(f"Error al crear tabla Olimpiada: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def crear_tabla_pais():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            sql = """
            CREATE TABLE IF NOT EXISTS Pais (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(150) NOT NULL,
                UNIQUE (nombre)
            )
            """
            cursor.execute(sql)
            conexion.commit()
            print("Tabla 'Pais' creada o ya existente")
    except Error as e:
        print(f"Error al crear tabla Pais: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def crear_tabla_genero():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            sql = """
            CREATE TABLE IF NOT EXISTS Genero (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(150) NOT NULL,
                UNIQUE (nombre)
            )
            """
            cursor.execute(sql)
            conexion.commit()
            print("Tabla 'Genero' creada o ya existente")
    except Error as e:
        print(f"Error al crear tabla Genero: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def crear_tabla_resultados():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            sql = """
            CREATE TABLE IF NOT EXISTS Resultados (
                idOlimpiada INT NOT NULL,
                idPais INT NOT NULL,
                idGenero INT NOT NULL,
                oro INT NOT NULL CHECK (oro >= 0),
                plata INT NOT NULL CHECK (plata >= 0),
                bronce INT NOT NULL CHECK (bronce >= 0),
                PRIMARY KEY (idOlimpiada, idPais, idGenero),
                FOREIGN KEY (idOlimpiada) REFERENCES Olimpiada(id),
                FOREIGN KEY (idPais) REFERENCES Pais(id),
                FOREIGN KEY (idGenero) REFERENCES Genero(id)
            )
            """
            cursor.execute(sql)
            conexion.commit()
            print("Tabla 'Resultados' creada o ya existente")
    except Error as e:
        print(f"Error al crear tabla Resultados: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


# -----------------------------
# Funciones auxiliares para insertar sin duplicar
# -----------------------------
def obtener_o_insertar_olimpiada(cursor, year_olimpiada):
    cursor.execute("SELECT id FROM Olimpiada WHERE year_olimpiada = %s", (year_olimpiada,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]

    cursor.execute("INSERT INTO Olimpiada (year_olimpiada) VALUES (%s)", (year_olimpiada,))
    return cursor.lastrowid


def obtener_o_insertar_pais(cursor, nombre):
    cursor.execute("SELECT id FROM Pais WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]

    cursor.execute("INSERT INTO Pais (nombre) VALUES (%s)", (nombre,))
    return cursor.lastrowid


def obtener_o_insertar_genero(cursor, nombre):
    cursor.execute("SELECT id FROM Genero WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]

    cursor.execute("INSERT INTO Genero (nombre) VALUES (%s)", (nombre,))
    return cursor.lastrowid


# -----------------------------
# Ejercicio 3: Insertar registros
# -----------------------------
def insertar_registro_olimpiada():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            id_olimpiada = obtener_o_insertar_olimpiada(cursor, 2024)
            conexion.commit()
            print(f"Registro disponible en Olimpiada. ID: {id_olimpiada}")
    except Error as e:
        print(f"Error al insertar Olimpiada: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def insertar_registro_pais():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            id_pais = obtener_o_insertar_pais(cursor, "México")
            conexion.commit()
            print(f"Registro disponible en Pais. ID: {id_pais}")
    except Error as e:
        print(f"Error al insertar Pais: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def insertar_registro_genero():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            id_genero = obtener_o_insertar_genero(cursor, "Masculino")
            conexion.commit()
            print(f"Registro disponible en Genero. ID: {id_genero}")
    except Error as e:
        print(f"Error al insertar Genero: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def insertar_varios_olimpiada():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            years = [2020, 2016, 2012, 2008, 2004]

            for year in years:
                obtener_o_insertar_olimpiada(cursor, year)

            conexion.commit()
            print("Registros de Olimpiada insertados o ya existentes")
    except Error as e:
        print(f"Error al insertar varias Olimpiadas: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def insertar_varios_pais():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            paises = ["Estados Unidos", "China", "Japón", "Brasil", "Alemania"]

            for pais in paises:
                obtener_o_insertar_pais(cursor, pais)

            conexion.commit()
            print("Registros de Pais insertados o ya existentes")
    except Error as e:
        print(f"Error al insertar varios Países: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def insertar_varios_genero():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            generos = ["Femenino", "Mixto"]

            for genero in generos:
                obtener_o_insertar_genero(cursor, genero)

            conexion.commit()
            print("Registros de Genero insertados o ya existentes")
    except Error as e:
        print(f"Error al insertar varios Géneros: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def insertar_varios_resultados():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)

            datos = [
                (2024, "México", "Masculino", 39, 41, 33),
                (2024, "Estados Unidos", "Masculino", 38, 32, 18),
                (2024, "China", "Masculino", 27, 14, 17),
                (2020, "México", "Femenino", 25, 30, 20),
                (2020, "Estados Unidos", "Femenino", 20, 15, 12)
            ]

            sql = """
            INSERT INTO Resultados (idOlimpiada, idPais, idGenero, oro, plata, bronce)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                oro = VALUES(oro),
                plata = VALUES(plata),
                bronce = VALUES(bronce)
            """

            for year, pais, genero, oro, plata, bronce in datos:
                id_olimpiada = obtener_o_insertar_olimpiada(cursor, year)
                id_pais = obtener_o_insertar_pais(cursor, pais)
                id_genero = obtener_o_insertar_genero(cursor, genero)

                cursor.execute(sql, (id_olimpiada, id_pais, id_genero, oro, plata, bronce))

            conexion.commit()
            print("Registros de Resultados insertados o actualizados correctamente")
    except Error as e:
        print(f"Error al insertar Resultados: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


# -----------------------------
# Ejercicio 4: Consultas
# -----------------------------
def consultar_todos_olimpiada():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            cursor.execute("SELECT * FROM Olimpiada ORDER BY year_olimpiada DESC")
            resultados = cursor.fetchall()

            print("\n--- Todas las Olimpiadas ---")
            for registro in resultados:
                print(f"ID: {registro[0]}, Año: {registro[1]}")
    except Error as e:
        print(f"Error al consultar Olimpiada: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def consultar_todos_pais():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            cursor.execute("SELECT * FROM Pais ORDER BY nombre")
            resultados = cursor.fetchall()

            print("\n--- Todos los Países ---")
            for registro in resultados:
                print(f"ID: {registro[0]}, Nombre: {registro[1]}")
    except Error as e:
        print(f"Error al consultar Pais: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def consultar_todos_genero():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            cursor.execute("SELECT * FROM Genero ORDER BY nombre")
            resultados = cursor.fetchall()

            print("\n--- Todos los Géneros ---")
            for registro in resultados:
                print(f"ID: {registro[0]}, Nombre: {registro[1]}")
    except Error as e:
        print(f"Error al consultar Genero: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def consultar_olimpiadas_despues_2010():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            sql = "SELECT id, year_olimpiada FROM Olimpiada WHERE year_olimpiada > %s ORDER BY year_olimpiada DESC"
            cursor.execute(sql, (2010,))
            resultados = cursor.fetchall()

            print("\n--- Olimpiadas después del año 2010 ---")
            for registro in resultados:
                print(f"ID: {registro[0]}, Año: {registro[1]}")
    except Error as e:
        print(f"Error al consultar Olimpiadas después de 2010: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def consultar_resultados_completo():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            sql = """
            SELECT o.year_olimpiada, p.nombre, g.nombre, r.oro, r.plata, r.bronce
            FROM Resultados r
            JOIN Olimpiada o ON r.idOlimpiada = o.id
            JOIN Pais p ON r.idPais = p.id
            JOIN Genero g ON r.idGenero = g.id
            ORDER BY o.year_olimpiada DESC, r.oro DESC
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()

            print("\n--- Resultados completos ---")
            for registro in resultados:
                print(
                    f"Año: {registro[0]}, País: {registro[1]}, Género: {registro[2]}, "
                    f"Oro: {registro[3]}, Plata: {registro[4]}, Bronce: {registro[5]}"
                )
    except Error as e:
        print(f"Error al consultar Resultados completos: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def buscar_pais_por_nombre(nombre_buscar):
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            sql = "SELECT * FROM Pais WHERE nombre LIKE %s"
            cursor.execute(sql, (f"%{nombre_buscar}%",))
            resultados = cursor.fetchall()

            print(f"\n--- Países que contienen '{nombre_buscar}' ---")
            for registro in resultados:
                print(f"ID: {registro[0]}, Nombre: {registro[1]}")
    except Error as e:
        print(f"Error al buscar país: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


def ordenar_por_oro():
    conexion = conectar()
    cursor = None

    try:
        if conexion and conexion.is_connected():
            cursor = conexion.cursor(buffered=True)
            sql = """
            SELECT o.year_olimpiada, p.nombre, g.nombre, r.oro, r.plata, r.bronce
            FROM Resultados r
            JOIN Olimpiada o ON r.idOlimpiada = o.id
            JOIN Pais p ON r.idPais = p.id
            JOIN Genero g ON r.idGenero = g.id
            ORDER BY r.oro DESC
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()

            print("\n--- Resultados ordenados por medallas de oro ---")
            for registro in resultados:
                print(
                    f"Año: {registro[0]}, País: {registro[1]}, Género: {registro[2]}, "
                    f"Oro: {registro[3]}, Plata: {registro[4]}, Bronce: {registro[5]}"
                )
    except Error as e:
        print(f"Error al ordenar por oro: {e}")
    finally:
        cerrar_conexion(cursor, conexion)


if __name__ == "__main__":
    # Ejercicio 2: Crear tablas primero
    crear_tabla_olimpiada()
    crear_tabla_pais()
    crear_tabla_genero()
    crear_tabla_resultados()

    # Ejercicio 1: Mostrar tablas después de crearlas
    mostrar_tablas()

    # Ejercicio 3: Insertar registros
    insertar_registro_olimpiada()
    insertar_registro_pais()
    insertar_registro_genero()
    insertar_varios_olimpiada()
    insertar_varios_pais()
    insertar_varios_genero()
    insertar_varios_resultados()

    # Ejercicio 4: Consultas
    consultar_todos_olimpiada()
    consultar_todos_pais()
    consultar_todos_genero()
    consultar_olimpiadas_despues_2010()
    consultar_resultados_completo()
    buscar_pais_por_nombre("México")
    ordenar_por_oro()
