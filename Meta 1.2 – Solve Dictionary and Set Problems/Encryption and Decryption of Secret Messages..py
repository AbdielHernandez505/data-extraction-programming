# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 15 de febrero de 2026
# Descripción: Tú y tu mejor amigo
# están creando un sistema secreto para enviar mensajes entre ustedes sin que nadie
# más pueda entenderlos. Deciden utilizar un metodo de encriptación y
# desencriptación basado en listas o diccionarios.

def encriptar_mensaje(mensaje, diccionario_encriptacion):


    resultado = ""
    for item in mensaje:
        resultado += diccionario_encriptacion[item]

    return resultado

def desencriptar_mensaje(mensaje, diccionario):

    desencriptar = {'$%3': 'a', '8@*': 'b', '2&9': 'c'}

    resultado = ""
    for item in range(0, len(mensaje), 3):
        bloque = mensaje[item:item+3]
        resultado+=desencriptar[bloque]
    return resultado


if __name__ == '__main__':
    diccionario_encriptacion = {'a': '$%3', 'b': '8@*', 'c': '2&9'}

    mensaje = encriptar_mensaje("abc", diccionario_encriptacion)
    print("Texto Encriptado: ", mensaje)
    print()
    desencriptar = desencriptar_mensaje(mensaje, diccionario_encriptacion)
    print("Texto Desencriptado: ", desencriptar)