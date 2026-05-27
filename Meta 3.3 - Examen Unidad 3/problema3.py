import pandas as pd

def problema3():
    df = pd.read_csv("ventas_procesadas.csv")

    # Tabla para comparar ingresos por ciudad y categoría
    tabla_categoria_ciudad = pd.pivot_table(
        df,
        values="ingreso_total",
        index="categoria",
        columns="ciudad",
        aggfunc="sum",
        fill_value=0
    )

    # Resumen general por categoría
    resumen_categoria = df.groupby("categoria").agg(
        ingreso_total=("ingreso_total", "sum"),
        precio_promedio=("precio", "mean"),
        cantidad_total=("cantidad", "sum"),
        productos=("producto", "nunique")
    ).reset_index()

    # Conteo de ventas por género y categoría
    tabla_genero_categoria = pd.pivot_table(
        df,
        values="id_venta",
        index="genero",
        columns="categoria",
        aggfunc="count",
        fill_value=0
    )

    # Resumen por ciudad
    resumen_ciudad = df.groupby("ciudad").agg(
        ventas=("id_venta", "count"),
        ingreso_total=("ingreso_total", "sum"),
        promedio_venta=("ingreso_total", "mean")
    ).reset_index()

    print("\nINGRESO POR CATEGORIA Y CIUDAD")
    print(tabla_categoria_ciudad)

    print("\nRESUMEN POR CATEGORIA")
    print(resumen_categoria)

    print("\nVENTAS POR GENERO Y CATEGORIA")
    print(tabla_genero_categoria)

    print("\nRESUMEN POR CIUDAD")
    print(resumen_ciudad)

    return tabla_categoria_ciudad, resumen_categoria, tabla_genero_categoria, resumen_ciudad

if __name__ == "__main__":
    problema3()