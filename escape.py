#La velocidad de escape de un planeta se define como la mínima velocidad necesaria para salir de un planeta venciendo la gravedad.
#Ve = raizcuadrada(2*g*r)

import math

r = float(input("Ingrese el radio en metros: "))
g = float(input("Ingrese la constante g: "))

ve = math.sqrt(2*g*r)

print(f"La velocidad de escape es de {ve:.1f}[m/s]")

#Ingrese el radio en metros: 6371000
#Ingrese la constante g: 9.8
#La velocidad de escape es de 11174.6[m/s]
