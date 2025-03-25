"""
Utilice ciclos para calcular el valor de la expresión: ∑i=1-n(∏j=1-i j^2)
"""

n = int(input("Ingrese el valor de n: "))
result = 0

for i in range(1, n+1):
  product = 1
  for j in range(1, i+1):
    product *= j ** 2
  result += product
print(result)