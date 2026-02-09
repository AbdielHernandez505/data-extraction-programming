# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 08 de febrero de 2026
# Descripción: Este archivo sirve para testear.

from statistics import Estadistica


if __name__ == "__main__":
    # Creación de lista
    lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])

    # Probar frecuencia de números
    print(f"\nFrecuencia de números:\n{lista.frecuencia()}\n\n")


    # Probar moda
    print(f"Moda: \n{lista.moda()}\n\n")

    # Probar histograma
    print(f"Histograma: ")
    lista.histograma()