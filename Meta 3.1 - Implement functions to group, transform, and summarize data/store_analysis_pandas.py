# Name: Hernandez Duran Jair Abdiel
# Group: 951
# Date: 25 de abril de 2026
# Description: This activity involves analyzing store data by applying grouping, transformation, and summarization techniques using pandas,
# including the creation of pivot tables and calculated metrics
import pandas as pd

def crear_df():
    data = {
        "Tienda": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
        "Producto": ["Manzana", "Plátano", "Naranja",
                     "Manzana", "Plátano", "Naranja",
                     "Manzana", "Plátano", "Naranja"],
        "Categoría": ["Fruta"] * 9,
        "Precio": [30, 20, 35, 25, 30, 45, 35, 20, 25],
        "Cantidad Vendida": [50, 30, 20, 60, 25, 35, 55, 20, 30],
        "Calificación": ["A", "B", "C", "A", "B", "A", "C", "B", "A"]
    }
    df = pd.DataFrame(data)
    return df

def map_codes(df):
    store_map = {"A": 1, "B": 2, "C": 3}
    raiting_map = {"A": 3, "B": 2, "C": 1}

    df["Código de Tienda"] = df["Tienda"].map(store_map)
    df["Calificación Númerica"] = df["Calificación"].map(raiting_map)
    return df


def total_sales(df):
    df["Venta Total"] = df["Precio"] * df["Cantidad Vendida"]

    ventas_tienda = df.groupby("Tienda").agg(
        total_ventas=("Venta Total", "sum")
    )

    print("Total de ventas por tienda:")
    print(ventas_tienda)
    print("=========================================================================")


def avg_price(df):
    precio_promedio = df.groupby("Tienda").agg(
        precio_promedio=("Precio", "mean")
    )

    print("Precio promedio por tienda:")
    print(precio_promedio)
    print("=========================================================================")


def qty_pivot(df):
    tabla_cantidad = pd.pivot_table(
        df,
        values="Cantidad Vendida",
        index="Producto",
        columns="Tienda",
        aggfunc="sum"
    )

    print("Cantidad vendida por producto y tienda:")
    print(tabla_cantidad)
    print("=========================================================================")


def sales_pivot(df):
    df["Venta Total"] = df["Precio"] * df["Cantidad Vendida"]

    tabla_ventas = pd.pivot_table(
        df,
        values="Venta Total",
        index="Producto",
        columns="Tienda",
        aggfunc="sum"
    )

    print("Total de ventas por producto y tienda:")
    print(tabla_ventas)
    print("=========================================================================")


if __name__ == "__main__":
    df = crear_df()
    print(f"Original Data: \n{df}")
    print("=========================================================================")
    map_codes(df)
    print(f"Mapped data: \n{df}")
    total_sales(df)
    avg_price(df)
    qty_pivot(df)
    sales_pivot(df)