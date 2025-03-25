"""
Escriba un algoritmo que imprima los valores de todas las fichas de dominó
sin repetir.
"""

for i in range(7):
  for j in range(i, 7):
    print(f"[{i}:{j}]", end=" ")
  print()