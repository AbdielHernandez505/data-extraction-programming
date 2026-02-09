# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 08 de febrero de 2026
# Descripción: En este ejercicio, el personaje es un robot que
# debe recoger productos en un almacén. El almacén está representado como
# una cuadrícula (grid), donde cada celda puede estar vacía (.), contener un
# obstáculo (#), o contener un producto (P), el inicio siempre es la posición 0,0.
# El robot comienza en la esquina superior izquierda del almacén y puede
# moverse hacia la derecha (R), abajo (D), izquierda (L), arriba(U). El objetivo
# es recoger todos los productos siguiendo una secuencia de movimientos
# dados y luego retornar al punto de inicio.

def verificar_recogida_productos(almacen, movimientos):
    # contar P
    total = 0
    for fila in almacen:
        for c in fila:
            if c == 'P':
                total += 1

    x = 0
    y = 0
    recogidos = 0
    vistos = []

    if almacen[x][y] == '#':
        return False

    if almacen[x][y] == 'P':
        vistos.append((x, y))
        recogidos += 1

    for m in movimientos:
        if m == 'R':
            y += 1
        elif m == 'L':
            y -= 1
        elif m == 'U':
            x -= 1
        elif m == 'D':
            x += 1
        else:
            return False

        if x < 0 or y < 0 or x >= len(almacen) or y >= len(almacen[0]):
            return False

        if almacen[x][y] == '#':
            return False

        if almacen[x][y] == 'P' and (x, y) not in vistos:
            vistos.append((x, y))
            recogidos += 1

    if x != 0 or y != 0:
        return False

    return recogidos == total
