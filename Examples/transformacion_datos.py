import pandas as pd


def crear_ventas():
    data = {
        "id_venta": [1,2,3,4,5,6],
        "id_cliente": [101,102,103,104,102,101],
        "region": ["N","S","N","C","N","S"],
        "producto": ["Laptop", "Mouse", "Monitor","Bocina","Mouse","Teclado"],
        "precio": [1200,23,66,1000,30,256],
        "cantidad": [12,42,46,45,21,45],

    }
    df = pd.DataFrame(data)
    return df


def crear_ventas_online():
    data = {
        "id_venta": [1, 2],
        "id_cliente": [101, 104],
        "region": ["N", "S"],
        "producto": ["Laptop", "Mouse"],
        "precio": [1200, 23],
        "cantidad": [12, 42],

    }
    df = pd.DataFrame(data)
    return df


def crear_clientes():
    data = {
        "id_cliente": [101,102,103,104],
        "nombre": ["Ana", "Abdiel", "Daniela", "Wendy"],
        "ciudad": ["Tijuana", "Rosarito", "Tijuana", "Rosarito"],

    }
    df = pd.DataFrame(data)
    return df


def renombrar(ventas):
    ventas_modificado = ventas.rename(
        columns={"region": "region_codigo"
                 }

    )
    print(ventas_modificado)

def eliminar(ventas):
    pass
    # ventas_eliminado = ventas.drop(columns=["id_ventas", "id_cliente"])
    # print(ventas_eliminado)

def transformar_map(ventas):
    regiones = {
        "N": "North",
        "S": "South",
        "C": "Central",
    }
    ventas["region_nombre"] = ventas.region.map(regiones)
    print(ventas)
    return ventas

def calcular(fila):
    iva = 1.16
    if fila.region == "N":
        iva = 1.68
    return fila.precio * fila.cantidad * iva

def transformar_apply(ventas:pd.DataFrame):
    # ventas["ingreso"] = ventas["precio"] * ventas["cantidad"]
    # ventas.apply( lambda fila : fila.precio * fila.cantidad, axis="columns")
    ventas["ingreso_iva"] = ventas.apply(calcular, axis = "columns")
    print(ventas)

def formato_largo_ancho(ventas:pd.DataFrame):
    res = ventas.pivot(
        index="region",
        columns="producto",
        values="precio"
    )

    print(res)
    return  res

def formato_ancho_largo(res):
    res = res.reset_index()
    df = res.melt(
        id_vars="region",
        value_vars=["Laptop", "Mouse", "Monitor", "Bocina"],
        var_name="producto",
        value_name="precio"
    )
    print(df)


def unir_datos(ventas, clientes):
    result = pd.merge(
        ventas,
        clientes,
        on="id_cliente",

        # left_on="id_cliente",
        # right_on="id" --> Para cuando en una columa es id y en otra tabla es id_cliente
        # suffixes=("_venta", "_cliente")
        # how="left" --> igual que inner join, righ join o left join en MySQL
    )
    print(result)

def concatenar(ventas, ventas_online):
    res = pd.concat([ventas, ventas_online])
    print(res)


if __name__ == '__main__':
    ventas = crear_ventas()
    ventas_online = crear_ventas_online()
    clientes = crear_clientes()
    
    renombrar(ventas)
    print("#############################################")
    eliminar(ventas)
    print("#############################################")
    transformar_map(ventas)
    print("#############################################")
    transformar_apply(ventas)
    print("#############################################")
    res = formato_largo_ancho(ventas)
    print("#############################################")
    formato_ancho_largo(res)
    print("#############################################")
    unir_datos(ventas, clientes)
    print("#############################################")
    concatenar(ventas, ventas_online)
    print("#############################################")