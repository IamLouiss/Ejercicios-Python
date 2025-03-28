"""
Haga una acción que tome como entrada un arreglo A y un entero N y
retorne (usando parámetros por referencia) el número de elementos de A
mayores a N y su promedio.
"""

def greater_than_N(arr : list, n):
  count = 0
  total = 0.0
  for element in arr:
    if element > n:
      count += 1
    total += element
  average = total / count if count > 0 else 0.0
  return count, average

number_list = [1, 2, 3, 4, 5]
n = 10
count, average = greater_than_N(number_list, n)
print(f"Elementos mayores que {n} en {number_list}: {count}. Promedio: {average}")