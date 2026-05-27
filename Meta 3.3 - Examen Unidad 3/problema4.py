import pandas as pd

def problema4():
    df = pd.read_csv("ventas_procesadas.csv")

    # Filtro por rango de edad
    filtro_edad = df[(df["edad"] >= 25) & (df["edad"] <= 35)]

    # Filtro por ciudades
    filtro_ciudades = df[df["ciudad"].isin(["Monterrey", "Guadalajara"])]

    # Filtro por categoría
    filtro_categoria = df[df["categoria"] == "Tecnologia"]

    # Búsqueda por texto en producto
    filtro_producto = df[df["producto"].str.contains("Laptop", case=False, na=False)]

    # Combinación de condiciones
    filtro_combinado = df[
        (df["genero"] == "Femenino") &
        (df["ciudad"] == "CDMX") &
        (df["ingreso_total"] > 3000)
    ]

    # Consulta usando query
    filtro_query = df.query("edad < 25 and precio > 1000")

    print("\nCLIENTES ENTRE 25 Y 35 AÑOS")
    print(filtro_edad[["cliente", "edad", "ciudad", "producto", "ingreso_total"]])

    print("\nVENTAS EN MONTERREY Y GUADALAJARA")
    print(filtro_ciudades[["cliente", "ciudad", "categoria", "ingreso_total"]])

    print("\nVENTAS DE TECNOLOGIA")
    print(filtro_categoria[["cliente", "producto", "precio", "cantidad", "ingreso_total"]])

    print("\nPRODUCTOS QUE CONTIENEN LAPTOP")
    print(filtro_producto[["cliente", "producto", "precio", "ciudad"]])

    print("\nBUSQUEDA CON VARIAS CONDICIONES")
    print(filtro_combinado[["cliente", "genero", "ciudad", "producto", "ingreso_total"]])

    print("\nBUSQUEDA CON QUERY")
    print(filtro_query[["cliente", "edad", "producto", "precio"]])

    return filtro_edad, filtro_ciudades, filtro_categoria, filtro_producto, filtro_combinado, filtro_query

if __name__ == "__main__":
    problema4()