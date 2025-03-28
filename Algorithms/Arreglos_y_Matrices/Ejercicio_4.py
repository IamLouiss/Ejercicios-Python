"""
Haga una acción que tome como entrada un arreglo de enteros y retorne
(usando parámetros por referencia) el número de elementos pares e impares
del arreglo.
"""

def odd_and_even(number_list : list[int]) -> tuple[int, int]:
  even_count = 0
  odd_count = 0
  for number in number_list:
    if number % 2 == 0: even_count += 1
    else: odd_count += 1
  return odd_count, even_count

number_list = [1, 2, 3, 4]
odd_elements, even_elements = odd_and_even(number_list)
print(f"En la lista de numeros {number_list} hay {odd_elements} impares y {even_elements} pares")