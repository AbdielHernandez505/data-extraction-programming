def declarar():
    t =()
    t2 = (1, 2, "Jose",3.4,4)
    t3 = tuple([1,2,3,4,5])
    print(t)
    print(t2)
    print(t3)

def slicing():
    print("\n============")

    t = (20, 30, 40, 50)
    s = t[1:3]
    print(s)


def recorrer():
    l = (10, 20, 30, 40, 50, 60, 70)
    l2 = (10, 20, 30, 40, 50, 60, 70)

    for item in l:
        print(item)

    print("\n================")

    for index in range(len(l)):
        print(index, " ------- ", l[index])

    print("\n================")

    for index, value in enumerate(l):
        print(index, " ------- ", value)

    print("\n================")

    for v1, v2 in zip(l, l2):
        print(v1, " ------- ", v2)


def funciones():
    print("\n================")
    t = (20, 30, 40, 50, 60, 70, 20)
    repetido = t.count(20)
    print("20 aparece", repetido)


if __name__ == '__main__':
    declarar()
    slicing()
    recorrer()
    funciones()