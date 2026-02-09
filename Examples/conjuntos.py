def declarar():
    s = {1, 2, 3, 4, 2}
    s2 = set()
    s3 = set([1, 2, 3, 3, 4])
    print(s)
    print(s2)
    print(s3)
    # PARA SABER CUANTOS DATOS DIFERENTES HAY, UTILIZAR SET Y LUEGO LEN, Y AUTOMATICAMENTE LA RESPUESTA LLEGA
    print("\n===============")


def recorrer():
    l = {10, 20, 30, 40, 50, 60, 70}
    l2 = {10, 20, 30, 40, 50, 60, 70}

    for item in l:
        print(item)

    print("\n================")

    for index, value in enumerate(l):
        print(index, " ------- ", value)

    print("\n================")

    for v1, v2 in zip(l, l2):
        print(v1, " ------- ", v2)


def funciones():
    print("\n================")
    s = {20, 30, 40, 50, 60}
    s2 = {10, 30, 50, 90}
    res = s.union(s2)
    res2 = s.intersection(s2)
    res3 = s.difference(s2)
    res4 = s2.difference(s)

    print(res)
    print(res2)
    print(res3)
    print(res4)


if __name__ == '__main__':
    declarar()
    recorrer()
    funciones()