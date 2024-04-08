import sys

class Pizza():
    ingredientes = 3
    precio = 10000
    tamaño = "familiar"

delgada = Pizza()
tradicional = Pizza()

ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
ingredientes_proteinas = ["pollo" , "vacuno", "carne vegetal"]

print(Pizza.precio)
print(Pizza.tamaño)

@staticmethod
def tipo_masa(masa):
    if masa == "delgada":
        return 'Has escogido masa delgada.'
    elif masa == "tradicional":
        return 5, 'Has escogido masa tradicional'

""""
print("Bienvenido a nuestra Pizzería")

pedido = input("elija el tipo de pizza que quiere ordenar, tradicional o delgada")

if pedido == "delgada": 
    pedido = delgada
    print("Elegiste una pizza delgada")
elif pedido == "tradicional":
    pedido = tradicional
    print("Elegiste una pizza tradicional")
else: ()

input("Ahora elige un ingrediente proteico (pollo, vacuno o carne vegetal)")

print(pedido)
"""
