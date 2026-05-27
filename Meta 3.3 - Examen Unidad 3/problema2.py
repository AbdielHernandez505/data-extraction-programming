import pandas as pd

def problema2():
    df = pd.read_csv("ventas_procesadas.csv")

    # Ventas por ciudad
    ventas_ciudad = df.groupby("ciudad").agg(
        ventas=("id_venta", "count"),
        ingreso_total=("ingreso_total", "sum"),
        promedio_venta=("ingreso_total", "mean")
    ).reset_index().sort_values("ingreso_total", ascending=False)

    # Ventas por categoría
    ventas_categoria = df.groupby("categoria").agg(
        ventas=("id_venta", "count"),
        ingreso_total=("ingreso_total", "sum"),
        precio_promedio=("precio", "mean")
    ).reset_index().sort_values("ingreso_total", ascending=False)

    # Segmentación sencilla por edad y género
    perfil_clientes = df.groupby(["rango_edad", "genero"]).agg(
        compras=("id_venta", "count"),
        ingreso_total=("ingreso_total", "sum")
    ).reset_index()

    # Clientes con más ingreso
    top_clientes = df.groupby("cliente").agg(
        compras=("id_venta", "count"),
        ingreso_total=("ingreso_total", "sum")
    ).reset_index().sort_values("ingreso_total", ascending=False).head(5)

    print("\nVENTAS POR CIUDAD")
    print(ventas_ciudad)

    print("\nVENTAS POR CATEGORIA")
    print(ventas_categoria)

    print("\nPERFIL DE CLIENTES")
    print(perfil_clientes)

    print("\nTOP CLIENTES")
    print(top_clientes)

    return ventas_ciudad, ventas_categoria, perfil_clientes, top_clientes

if __name__ == "__main__":
    problema2()