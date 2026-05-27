import pandas as pd


def problema1():
    df = pd.read_csv("ventas.csv")

    # Limpieza básica de fechas, textos y datos vacíos
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", format="mixed", dayfirst=True)

    df["ciudad"] = df["ciudad"].str.strip().str.title()
    df["ciudad"] = df["ciudad"].replace({"Cdmx": "CDMX"})

    df["categoria"] = df["categoria"].str.strip().str.capitalize()
    df["categoria"] = df["categoria"].replace({"Tec": "Tecnologia"})
    df["categoria"] = df["categoria"].fillna("Desconocida")

    df["genero"] = df["genero"].str.strip().str.lower()
    df["genero"] = df["genero"].replace({
        "f": "Femenino",
        "m": "Masculino",
        "femenino": "Femenino",
        "masculino": "Masculino"
    })
    df["genero"] = df["genero"].fillna("No especificado")

    # La cantidad tenía textos como "2 piezas", por eso se extrae solo el número
    df["cantidad"] = df["cantidad"].astype(str).str.extract(r"(\d+)")
    df["cantidad"] = df["cantidad"].astype(float).fillna(1).astype(int)

    df["producto"] = df["producto"].fillna("Producto Desconocido")

    # Nuevas columnas para facilitar el análisis
    df["ingreso_total"] = df["precio"] * df["cantidad"]

    rangos = [0, 25, 35, 45, 100]
    nombres = ["18-25", "26-35", "36-45", "46+"]
    df["rango_edad"] = pd.cut(df["edad"], bins=rangos, labels=nombres)

    df["mes"] = df["fecha"].dt.month

    df.to_csv("ventas_procesadas.csv", index=False)
    print("Archivo ventas_procesadas.csv creado correctamente.")

    return df


if __name__ == "__main__":
    problema1()