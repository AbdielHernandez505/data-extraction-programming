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
    pass


def avg_price(df):
    pass


def qty_pivot(df):
    pass


def sales_pivot(df):
    pass


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
