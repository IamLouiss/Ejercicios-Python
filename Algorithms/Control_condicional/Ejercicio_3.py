"""
Haga un algoritmo que tome como entrada 2 números distintos e imprima
el segundo número mayor.
"""

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

if n1 == n2: print("Son iguales")
elif n1 < n2: print(n1)
else: print(n2)