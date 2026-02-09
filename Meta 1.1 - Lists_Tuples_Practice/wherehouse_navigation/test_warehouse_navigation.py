# Nombre: Hernández Duran Jair Abdiel
# Grupo: 951
# Fecha: 08 de febrero de 2026
# Descripción: Sirve para testear

from warehouse_navigation import verificar_recogida_productos

almacen = [
    ['.', '.', '#', 'P'],
    ['.', '#', '.', '.'],
    ['P', '.', 'P', '.'],
    ['#', '.', '#', '.']
]

movimientos = ['D','D','R','R','U','R','U','D','L','D','L','L','U','U']
print(verificar_recogida_productos(almacen, movimientos))
