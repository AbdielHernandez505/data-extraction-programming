def declarar():
    d = {"nommbre": "Miguel",
         "edad": 30
         }
    d2 = dict()
    d3 = dict(nombre="Miguel", edad=30)
    lista = [("nombre", "Miguel"), ("edad", 30), ("dir", "asd")]

def recorrer():
    d = {"nommbre": "Miguel",
         "edad": 30,
         "dir": "asd"
         }

    for key in d:
        print(key, "--->", d[key])

    print("-----VALORES------")
    for item in d.values():
        print(item)

    print("-----ITEMS--------")
    for key, value in d.items():
        print(key, "-->", value)

def Funciones():
    d = {}
    d["Nombre"] = "Abdiel" # Si ese campo no existe lo agrega, si existe lo modifica
    d["Edad"] = 20
    d["Dir"] = "Universidad"
    eliminado = d.pop("Dir")
    print("Valor eliminado", eliminado)
    print("Nombre ", d["Nombre"]) # <-- se utiliza cuando estamos seguros que existe la llave
    print("Edad ", d.get("Nombre", "No existe el dato")) # <-- se utiliza cuando no estamos seguros que existe la llave
    print(d.keys())
    print(d.values())
    print(d.items())

    print(d)




if __name__ == '__main__':
    declarar()
    print("\n============")
    recorrer()
    print("\n============")
    Funciones()