# Nombre: Hernandez Duran Jair Abdiel
# Grupo: 951
# Fecha: 15 de marzo de 2026
# Descripción: Ejercicios de procesamiento de datos: manejo de duplicados
#              y valores nulos utilizando pandas DataFrames.

import pandas as pd
import numpy as np


# DataFrame de prueba para correr los ejercicios
def crear_df():
    data = {
        'nombre':  ["luis", "ana", "ana", "pedro", None],
        'edad':    [None, 23, 20, np.nan, 25],
        'salario': [15000, 20000, 25000, 28000, np.nan],
        'pais':    ["USA", "MEX", "MEX", "MEX", None]
    }
    df = pd.DataFrame(data)
    return df


# =============================================================================
# Ejercicio 1
# =============================================================================
def porcentaje_nulos(df: pd.DataFrame):
    porcentaje = df.isnull().sum() / len(df)
    print(porcentaje)
    return porcentaje


# =============================================================================
# Ejercicio 2
# =============================================================================
def numero_duplicados(df: pd.DataFrame):
    duplicados = df.duplicated().sum()
    print(duplicados)
    return duplicados


# =============================================================================
# Ejercicio 3
# =============================================================================
def eliminar_columnas_nulos(df: pd.DataFrame, max_porcentaje: float):
    if not (0 <= max_porcentaje <= 1):
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1.")

    porcentaje = df.isnull().sum() / len(df)
    columnas_eliminar = porcentaje[porcentaje >= max_porcentaje].index.tolist()
    df.drop(columns=columnas_eliminar, inplace=True)

    print(columnas_eliminar)
    return columnas_eliminar


# =============================================================================
# Ejercicio 4
# =============================================================================
def sustituir_nulos(df: pd.DataFrame, columnas: list, metodo: str):
    if metodo not in ['mean', 'bfill', 'ffill']:
        raise ValueError(f"Método inválido: '{metodo}'. Debe ser mean, bfill o ffill.")

    for columna in columnas:
        if metodo == 'mean':
            df[columna] = df[columna].fillna(df[columna].mean())
        elif metodo == 'bfill':
            df[columna] = df[columna].bfill()
        elif metodo == 'ffill':
            df[columna] = df[columna].ffill()

    print(df)
    return df


# =============================================================================
# Ejercicio 5
# =============================================================================
def eliminar_duplicados(df: pd.DataFrame):
    renglones_antes = len(df)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    eliminados = renglones_antes - len(df)

    print(eliminados)
    return eliminados


# =============================================================================
if __name__ == "__main__":

    df = crear_df()
    print("=== DataFrame original ===")
    print(df)

    print("=== Ejercicio 1: Porcentaje de nulos ===")
    porcentaje_nulos(df)

    print("=== Ejercicio 2: Número de duplicados ===")
    numero_duplicados(df)

    print("=== Ejercicio 3: Eliminar columnas con >= 50% de nulos ===")
    df_ej3 = df.copy()
    eliminar_columnas_nulos(df_ej3, 0.5)
    print(df_ej3)

    print("=== Ejercicio 4: Sustituir nulos en 'edad' con mean ===")
    df_ej4 = df.copy()
    sustituir_nulos(df_ej4, ['edad'], 'mean')

    print("=== Ejercicio 5: Eliminar renglones duplicados ===")
    df_ej5 = df.copy()
    eliminar_duplicados(df_ej5)
    print(df_ej5)
