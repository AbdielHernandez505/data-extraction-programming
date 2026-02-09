# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 08 de febrero de 2026
# Descripción: Simula el historial de
# cambios en una hoja de cálculo, donde los usuarios pueden realizar cambios
# en las celdas. Usa una lista como pila para almacenar los cambios y permite a los usuarios deshacer múltiples cambios.

hoja = {}
historial = []

def registrar_cambio(celda, valor):
    if celda in hoja:
        historial.append((celda, hoja[celda]))
    else:
        historial.append((celda, 0))
    hoja[celda] = valor

def deshacer():
    if len(historial) == 0:
        print("No hay cambios")
        return

    celda, ant = historial.pop()

    if ant == 0:
        del hoja[celda]
    else:
        hoja[celda] = ant
