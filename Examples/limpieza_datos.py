import pandas as pd
# conversiones de tipo y limpieza de datos


def crear_df_sucio():
    data = {
        "cliente": [' Juan','maria ', ' PEDRO', ' rosA'],
        'edad': ["25","30 años", "veintiocho", "45"],
        'salario': ["$10000", "12355", "2605999mxn", "$12,000"],
        'fecha': ["10-03-26", "19/03/26", "March 17 2026", "invalid"],
        'pais': ["México", "mexico", "MX", " usa"],
        'activo': ["yes", "no", "yes", "no"]

    }
    df = pd.DataFrame(data)
    return df


def cadenas(df):
    df.cliente = df.cliente.str.strip().str.capitalize()
    df.pais = df.pais.str.strip().str.lower()
    df.pais = df.pais.replace({
        "méxico": "mx",
        "mexico": "mx"
    })



def numericos(df):
    df.edad = df.edad.str.replace("años","").str.strip()
    df.edad = pd.to_numeric(df.edad, errors='coerce')
    # df.edad = df.edad.astype(int)
    df.salario = df.salario.str.replace(r"[^\d.]","",regex=True)
    df.salario = pd.to_numeric(df.salario, errors='coerce')


def fechas(df):
    df.fecha = pd.to_datetime(df.fecha, errors='coerce', format = 'mixed')
    df["year"] = df.fecha.dt.year

def categoricos(df):
    df.pais = df.pais.astype("category")



if __name__ == '__main__':
    df = crear_df_sucio()

    cadenas(df)
    print("########################")
    numericos(df)
    print("########################")
    fechas(df)
    print("########################")
    categoricos(df)
    print("########################")
    print(df)
    print("########################")
    print(df.info())