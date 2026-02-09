def declarar():
    l = [1, 2, 3, 4, 5, 2,9]
    l2 = list()
    l3 = list("Hola")
    print(l)
    print(l2)
    print(l3)
    l[2] = 200
    l[-1] = "Nose"
    print(l)


def slicing():
    l = [10,20,30,40,50,60,70]
    s = l[1:3]
    s2 = l[::2]
    print(s)
    print(s2)


def recorrer():
    l = [10,20,30,40,50,60,70]
    l2 = [10, 20, 30, 40, 50, 60, 70]

    for item in l:
        print(item)

    print("\n================")

    for index in range(len(l)):
        print(index, " ------- ",l[index])

    print("\n================")

    for index, value in enumerate(l):
        print(index, " ------- ",value)

    print("\n================")

    for v1, v2 in zip(l, l2):
        print(v1, " ------- ", v2)

def funciones():
    print("\n================")

    l = []
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.insert(1, "Miguel")
    eliminado = l.pop()
    l.remove(5)
    index = l.index(3)

    print("Indice del valor 6: ", index)
    print("Eliminado = ", eliminado)
    print(l)


    print("\n================")

    #print(type(l))


if __name__ == '__main__':
    declarar()
    slicing()
    recorrer()
    funciones()
