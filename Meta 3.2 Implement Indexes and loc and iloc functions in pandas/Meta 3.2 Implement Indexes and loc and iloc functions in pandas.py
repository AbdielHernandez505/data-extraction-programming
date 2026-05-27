# Name: Hernandez Duran Jair Abdiel
# Group: 951
# Date: 26 de mayo de 2026
# Description: This activity involves creating a sales DataFrame and selecting data using loc and iloc,
# including modifying a specific value in the DataFrame.

import pandas as pd
import random


def crear_ventas():
    data = {
        "Producto A": [
            random.randint(100, 1000),
            random.randint(100, 1000),
            random.randint(100, 1000)
        ],
        "Producto B": [
            random.randint(100, 1000),
            random.randint(100, 1000),
            random.randint(100, 1000)
        ],
        "Producto C": [
            random.randint(100, 1000),
            random.randint(100, 1000),
            random.randint(100, 1000)
        ]
    }

    ventas = pd.DataFrame(data, index=["Enero", "Febrero", "Marzo"])
    return ventas


# Seleccionar datos usando loc
def seleccionar_loc(ventas):
    print("Ventas del Producto A en Enero:")
    print(ventas.loc["Enero", "Producto A"])

    print("=============================")

    print("Ventas de todos los productos en Febrero:")
    print(ventas.loc["Febrero"])

    print("=============================")

    print("Ventas de todos los productos en el primer y tercer mes:")
    print(ventas.loc[["Enero", "Marzo"]])


# Seleccionar datos usando iloc
def seleccionar_iloc(ventas):
    print("Ventas del primer mes para todos los productos:")
    print(ventas.iloc[0])

    print("=============================")

    print("Ventas del segundo producto en todos los meses:")
    print(ventas.iloc[:, 1])

    print("=============================")

    print("Ventas del segundo y tercer mes para el primer producto:")
    print(ventas.iloc[1:3, 0])


# Cambiar valor de un producto en un mes específico
def cambiar_venta(ventas, mes, producto, nuevo_valor):
    ventas.loc[mes, producto] = nuevo_valor

    print(f"Se cambió la venta de {producto} en {mes} a {nuevo_valor}")
    print(ventas)


if __name__ == "__main__":
    ventas = crear_ventas()

    print("DataFrame original:")
    print(ventas)

    print("=============================")
    print("Selección con loc:")
    seleccionar_loc(ventas)

    print("=============================")
    print("Selección con iloc:")
    seleccionar_iloc(ventas)

    print("=============================")
    print("Cambio de valor:")
    cambiar_venta(ventas, "Marzo", "Producto B", 1200)