"""
Escriba un algoritmo que tome como entrada un número N e imprima
la secuencia de Fibonacci hasta N. La secuencia de Fibonacci comienza
con los números 0 y 1 y se calcula en cada paso sumando los últimos dos
números de la secuencia. Por ejemplo, los primeros números de la secuencia
de Fibonacci son 0, 1, 1, 2, 3, 5, 8, 13, ...
"""

n = int(input("Ingrese un numero N mayor o igual que cero: "))

if n < 0:
  print("Debe ingresar un numero positivo")
else:
  f_0, f_1 = 0, 1
  print(f_0, end = " ")
  if n >= 1:
    print(f_1, end = " ", sep=" ")
    for i in range(1, n):
      next_fibonacci = f_0 + f_1
      f_0, f_1 = f_1, next_fibonacci
      print(next_fibonacci, end=" ")