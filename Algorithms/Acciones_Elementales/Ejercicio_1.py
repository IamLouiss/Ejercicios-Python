""""
Escriba un algoritmo que lea un número de cuatro dígitos y muestre en
pantalla el número escrito en reverso. Por ejemplo, si el número es 4678, la
salida debería ser 8764.
"""

#### Forma alternativa

num = int(input("Ingrese un numero: ")[::-1])
print(num)

### Forma manual

# num = int(input("Ingrese un numero: "))
# reverse_num = 0
# while num > 0:
#   reverse_num *= 10
#   reverse_num += num % 10
#   num //= 10

# print(reverse_num)