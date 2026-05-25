import pandas as pd


def alumnos():
    d = {
        'matricula': [101, 102, 103, 104, 105, 106],
        'nombre': ["a1", "a2", "a3", "a4", "a5", "a6"],
        'carrera': ["LIN", "LC", "LAE", "LNI", "LIN", "LC"],
        'promedio': [90, 95, 100, 85, 80, 75]
    }
    df = pd.DataFrame(d)
    return df

def indices_numericos(df): # iloc, son funciones para hacer filtrado de informacion, modificar, para crear nuevas columnas. Hacer cambios especificos
    valores = df.iloc[0:3, [1,3]] # con coma puedes seleccionar columnas. Asi sera, # [filas, columnas]
    df.iloc[2 , 3] = 50
    print(valores) # para seleccionar conjuntos de datos especificos, se encierra en corchetes [posicion 1, posicion 2]
    print("=======================================")
    print(df)




def convertir_indices(df):
    df.set_index('carrera', inplace=True, drop=False) # drop=false no borra la columna que se convirtio en indice. Para usarla conjunto a reset_index, igual agregar drop=True, lo contrario a la linea anterior
    df.reset_index(inplace=True, drop=True) # Para resetear el indice a como era antes
    print(df)


# loc [indices, columnas] trabaja sobre indices, a diferencia de iloc que trabaja sobre filas. Esta funcion se puede utilizar en conjunto con la funcion anterior, casi siempre van de la mano
def indices_etiquetas(df):
    # valores = df.loc[1:3, ["nombre", "promedio"]]
    df.set_index('carrera', inplace=True)
    valores = df.loc[["LIN", "LC"], ["nombre", "promedio"]]
    df.loc[df.nombre == "a3", "promedio"] = 100 # Para cambiar valores. Modificar, por buscar. La persona a3 selecciona su columna promedio y cambiaselo a 100
    print(df)
    print("=======================================")
    print(valores)
    df.reset_index(inplace=True)
    # cuando es numerico, dentro de los [], basta con poner entre dos los ;. Asi marca un rango de uno a otro numero.
    # a diferencia de los textos, hay debe separarse por coma y debe ponerse
    # todo el indice no hay rango como los numericos
    # NO CONFUNDIR: iloc solo trabaja con posiciones, en cambio loc, si trabaja con el indice directo. NO CONFUNDIR

if __name__ == "__main__":
    df = alumnos()
    indices_numericos(df)
    print("=======================================")
    convertir_indices(df)
    print("=======================================")
    indices_etiquetas(df)
    print("=======================================")

    datos = df.describe() # funciona para ver todos los datos estadisticos.
    # print(datos.loc[["mean", "max", "min"]])
    print(datos.iloc[[1, 3, 7]])
    # Para mi, loc se puede entender mas facil, porque es mas expresivo, sus busqueda tiende a ser mejor porque no es por posiciones, sino, el nombre o valor directo de la columna