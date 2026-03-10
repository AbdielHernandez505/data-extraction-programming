#procesos null
import pandas as pd
import numpy as np


def crear_nulos():
    data={
        'nombre':["luis","ana","ana","pedro",None],
        'edad':[None,23,20,np.nan,25],
        'salario':[15000,20000,25000,28000,np.nan],
        'pais':["USA","MEX","MEX","MEX",None]
    }

    df=pd.DataFrame(data)
    return df


def detectar_nulos(df:pd.DataFrame):
    print(df.isnull())  # muestra true/false por celda
    print(df.isnull().sum())  # numero de nulos por columna
    print(df.isnull().sum().sum())  # total de nulos
    print(df.isnull().sum()/len(df))  # porcentaje de nulos


def eliminar_nulos(df:pd.DataFrame):
    df_sin_nulos=df.dropna()
    df_sin_nulos_salario=df.dropna(subset=["salario","nombre"])
    df_thresh=df.dropna(thresh=2)
    df_columnas=df.dropna(axis="columns", thresh=4)

    print(df_columnas)
     # print(df_sin_nulos)
    # df.dropna(inplace=True)
    # print(df)


  # promedio valores numeracion con distribucion normal o cercanos
  # mediana valores numericos con outliers
  # moda valores categoricos
  # Bfill, Ffill datos temporales (secuencia,tiempo,series temporales)

def inputar_nulos(df:pd.DataFrame):
    prom_edad=df.edad.mean()

    salario_mediana=df.salario.median()

    moda_pais=df.pais.mode()[0]
    df["new_edad"]=df.edad.fillna(value=prom_edad)
    df["new_pais"]=df.pais.fillna(value=moda_pais)
    df["ffill_edad"]=df.edad.ffil()
    df["fill_edad"]=df.edad.bfil()
    df["mix_edad"]=df.edad.ffill().bfill().fillna(prom_edad)
    print(df)


if __name__=="__main__":

    df=crear_nulos()
    print("=======================")
    detectar_nulos(df)
    print("=======================")
    eliminar_nulos(df)
    print("=======================")
    inputar_nulos(df)