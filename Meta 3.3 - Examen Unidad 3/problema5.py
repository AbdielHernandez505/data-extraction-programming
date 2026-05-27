import pandas as pd

def problema5():
    df = pd.read_csv("ventas_procesadas.csv")

    # iloc sirve para seleccionar por posición
    primeras_filas = df.iloc[0:5, 0:6]

    # loc sirve para seleccionar por etiquetas o condiciones
    ventas_monterrey = df.loc[
        df["ciudad"] == "Monterrey",
        ["cliente", "producto", "ingreso_total"]
    ]

    # Índice por ciudad
    df_ciudad = df.set_index("ciudad")
    ventas_cdmx = df_ciudad.loc["CDMX"]

    # Índice con ciudad y categoría
    df_multi = df.set_index(["ciudad", "categoria"]).sort_index()
    ventas_tecnologia_monterrey = df_multi.loc[("Monterrey", "Tecnologia")]

    # Subconjunto con iloc
    subconjunto = df.iloc[10:20, -4:]

    print("\nPRIMERAS FILAS CON ILOC")
    print(primeras_filas)

    print("\nVENTAS EN MONTERREY CON LOC")
    print(ventas_monterrey)

    print("\nVENTAS EN CDMX USANDO INDICE")
    print(ventas_cdmx)

    print("\nVENTAS DE TECNOLOGIA EN MONTERREY")
    print(ventas_tecnologia_monterrey)

    print("\nSUBCONJUNTO DEL DATASET")
    print(subconjunto)

    return primeras_filas, ventas_monterrey, ventas_cdmx, ventas_tecnologia_monterrey, subconjunto

if __name__ == "__main__":
    problema5()