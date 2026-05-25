import pandas as pd


def crear_alumnos():
    d = {
        'nombre': ["a1", "a2", "a3", "a4", "a5"],
        'edad': [20, 19, 18, 20, 19],
        'carrera': ["LIN", "LC", "LAE", "LIN", "LIN"],
        'promedio': [90, 85, 70, 100, 90]
    }
    df = pd.DataFrame(d)
    return df

def busqueda_boleana():
    # c1 = df.promedio >=90
    # AND = &
    # OR = |
    c2 = (df.promedio >= 95) & (df.carrera == "LIN")
    c3 = (df.carrera == "LC") | (df.carrera == "LAE")
    c4 = df.carrera.isin(["LC", "LAE"])
    print(df[c4])

def texto():
    c = df.carrera.str.contains("a", case=False)  # case=False --> no importa si tiene mayusculas o minusculas.

    print(df[c])

def query():
    prom = 80
    sql = "promedio > @prom"
    sql2 = "promedio > @prom and carrera == 'LIN'"
    # se puede poner arroba el nombre de la variable para numeros, pero no es necesario, puedes poner el numero directo
    sql3 = "carrera.isin(['LC', 'LAE'])"
    res = df.query(sql3)
    print(res)



def valores_unicos():
    unicos = df.carrera.unique() # retorna unaicamente una vez los valores
    # print(unicos)
    print(df.carrera.value_counts()) # cuenta cuantas veces aparece cada variable. Cuenta


def tops():
    top3_promedio =df.nlargest(3, columns="promedio")
    top3_menor_promedio = df.nsmallest(3, columns="promedio")
    print(top3_menor_promedio)


if __name__ == '__main__':
    df = crear_alumnos()
    busqueda_boleana()
    print("###############################################")
    texto()
    print("###############################################")
    query()
    print("###############################################")
    valores_unicos()
    print("###############################################")
    tops()
