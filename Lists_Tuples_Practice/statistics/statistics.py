# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 08 de febrero de 2026
# Descripción: Cree una clase llamada Estadística que contiene como
    # atributo una lista de números naturales la cual puede contener repetidos.
    # Debe contener los siguientes métodos:
    # a. Frecuencia de Números. Dada la lista, devuelve una lista de tuplas con el número de veces que aparece cada número en la lista. La tupla debe tener el número y la cantidad de veces que aparece.
    # b. Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
    # c. Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores.


class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros

    def frecuencia(self):
        # Para devolver la lista de tublas con (número, frecuencia)
        frecuencias = []
        num_usados = []
        for numero in self.numeros:
            if numero not in num_usados:
                num_usados.append(numero)
                contador = 0
                for i in self.numeros:
                    if i == numero:
                        contador += 1
                frecuencias.append((numero, contador))
        return frecuencias

    def moda(self):
        # Para devolver el número que mas se repite
        frec = self.frecuencia()
        mayor = 0
        moda = None

        for numero, frecuencia in frec:
            if frecuencia > mayor:
                mayor = frecuencia
                moda = numero

        return moda

    def histograma(self):
        # Para mostrar el histogrtama de la lista
        frecuencias = self.frecuencia()

        ordenar = sorted(frecuencias)
        for numero, frecuencia in ordenar:
            print(f"{numero} {'*' * frecuencia}")

