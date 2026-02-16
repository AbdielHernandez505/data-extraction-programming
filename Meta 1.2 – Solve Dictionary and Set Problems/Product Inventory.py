# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 15 de febrero de 2026
# Descripción: Gestiona un inventario de productos en una tienda
# utilizando diccionarios. Las claves pueden ser los códigos de producto y los valores
# pueden ser diccionarios con información como el nombre, precio y cantidad en stock.
# Debe tener funciones para agregar, editar, eliminar producto, además de funciones
# para realizar venta e imprimir inventario.


def agregar(inventario, codigo, nombre, precio, stock):
    if codigo in inventario:
        print("Ya existe")
        return
    inventario[codigo] = {"nombre": nombre, "precio": precio, "stock": stock}


def editar(inventario, codigo, nombre, precio, stock):
    if codigo not in inventario:
        print("No existe")
        return
    inventario[codigo] = {"nombre": nombre, "precio": precio, "stock": stock}


def eliminar(inventario, codigo):
    if codigo in inventario:
        del inventario[codigo]
    else:
        print("No existe")


def vender(inventario, codigo, cantidad):
    if codigo not in inventario:
        print("No existe")
        return
    if inventario[codigo]["stock"] < cantidad:
        print("Sin stock")
        return
    inventario[codigo]["stock"] -= cantidad


def mostrar(inventario):
    for codigo, datos in inventario.items():
        print(codigo, datos["nombre"], datos["precio"], datos["stock"])


if __name__ == "__main__":
    inv = {}

    agregar(inv, "P1", "Coca", 18, 10)
    agregar(inv, "P2", "Sabritas", 20, 5)
    mostrar(inv)

    vender(inv, "P1", 3)
    mostrar(inv)

    editar(inv, "P2", "Sabritas", 22, 5)
    mostrar(inv)

    eliminar(inv, "P1")
    mostrar(inv)
