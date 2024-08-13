# Ingrese una lista de compras: manzanas, plátanos, leche, pan
# Los productos en la lista de compras son: ['manzanas', 'plátanos', 'leche', 'pan']

compras = input("Ingrese una lista de compras: ")
productos = compras.split(", ")
print(f"Los productos en la lista de compras son: {productos}")

# Convertir la lista de compras en una tupla
def convertir_lista_a_tupla(lista):
    return tuple(lista)# Utiliza una función para convertir 

productos_tupla = convertir_lista_a_tupla(productos)

print(f"Los productos en la tupla de compra son: {productos_tupla}")