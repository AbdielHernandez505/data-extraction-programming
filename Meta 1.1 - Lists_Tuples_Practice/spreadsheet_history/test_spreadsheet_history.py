# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 08 de febrero de 2026
# Descripción: Sirve para testear

from spreadsheet_history import hoja, registrar_cambio, deshacer

registrar_cambio('A1', 10)
registrar_cambio('B2', 20)
registrar_cambio('A1', 30)

print("Hoja:", hoja)

deshacer()
print("Deshacer:", hoja)

deshacer()
print("Deshacer otra vez:", hoja)
