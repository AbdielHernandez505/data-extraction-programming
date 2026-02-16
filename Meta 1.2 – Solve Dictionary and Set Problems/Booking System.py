# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 15 de febrero de 2026
# Descripción: Desarrolla un sistema de reservas utilizando sets. Crea
# conjuntos para representar habitaciones disponibles y habitaciones reservadas en
# un hotel. Permite a los usuarios realizar reservas, liberar habitaciones y mostrar la
# disponibilidad actual. NOTA: No utilizar menú, solo las funciones a realizar las
# pruebas necesarias para verificar funcionamiento adecuado.

def crear():
    disponible = {101,102,103,104,105,106,107}
    reservado = set()

    return disponible, reservado


def reservar(disponibles, reservadas, habitacion):
    if habitacion in disponibles:
        disponibles.remove(habitacion)  
        reservadas.add(habitacion)  
        print("Habitación reservada correctamente")
    elif habitacion in reservadas:
        print("Habitación ocupada")
    else:
        print("La habitación no existe")

def mostrar(disponibles, reservadas):
    print("Disponible: ", disponibles)
    print("Reservadas: ", reservadas)

def liberar(disponibles, reservadas, habitacion):
    if habitacion in reservadas:
        reservadas.remove(habitacion)  
        disponibles.add(habitacion)  
        print("Habitación liberada correctamente")
    elif habitacion in disponibles:
        print("Esa habitación ya está disponible")
    else:
        print("La habitación no existe")

if __name__ == "__main__":
    disponibles, reservadas = crear()
    print("\nPrueba 1. Reservar habitacion")
    print()
    mostrar(disponibles, reservadas)
    print()
    reservar(disponibles, reservadas, 101)
    print()
    print("Prueba 2. Reservar habitacion que ya esta ocupada")
    print()
    reservar(disponibles, reservadas, 101)
    print("\nPrueba 3. Reservar habitacion que no existe")
    print()
    reservar(disponibles, reservadas, 10132)
    print()
    mostrar(disponibles, reservadas)
    print("\nPrueba 3. Liberar habitacion")
    liberar(disponibles, reservadas, 101)
    print()
    mostrar(disponibles, reservadas)

