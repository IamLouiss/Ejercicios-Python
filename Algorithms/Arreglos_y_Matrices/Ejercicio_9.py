"""
Dados dos arreglos ordenados de enteros A y B, haga una función que
permita obtener un tercer arreglo C que contenga todos los elementos de
A y B ordenados. Por ejemplo, si A = {1, 4, 9} y B = {2, 5, 10, 12}, el
resultado deberá ser C = {1, 2, 4, 5, 9, 10, 12}
"""

def merge_and_sort(list_1 : list[int], list_2 : list[int]) -> list[int]:
  list_3 = list_1 + list_2
  list_3.sort()
  return list_3

print(merge_and_sort([1, 4, 9], [2, 5, 10, 12]))