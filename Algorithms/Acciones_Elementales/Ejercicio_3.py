"""
Escriba un algoritmo que transforme un número binario de cuatro bits a
un número decimal.
"""

#### Con funciones

# binary_number = input("Ingrese un numero binario de 4 bits: ")
# decimal_number = 0
# for indice, bit in enumerate(reversed(binary_number)):
#   decimal_number += (int(bit) * (2**indice))
# print(f"El numero en decimal es: {decimal_number}")

### Con operaciones matematicas

binary_number = int(input("Ingrese un numero binario de 4 bits: "))
decimal_number = 0
for i in range(4):
  decimal_number += (binary_number % 10) * (2**i)
  binary_number //= 10
print(f"El numero en decimal es: {decimal_number}")