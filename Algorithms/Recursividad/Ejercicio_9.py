"""
Dado un arreglo de N números enteros, diseñar algoritmos recursivos que calculen:
● El mayor elemento del arreglo. 
● La suma de los elementos del arreglo. 
● La media de todos los elementos del arreglo. 
● Verificar si el arreglo está ordenado. 
"""

def max_element(numbers: list, i = 0):
  if i == len(numbers) - 1:
    return numbers[i]
  return max(numbers[i], max_element(numbers, i+1))

def sum_elements(numbers: list, i = 0):
  if i == len(numbers) - 1:
    return numbers[i]
  return numbers[i] + sum_elements(numbers, i+1)

def average_elements(numbers: list, i = 0):
  if i == len(numbers) - 1:
    return numbers[i] / len(numbers)
  return numbers[i] / len(numbers) + sum_elements(numbers, i+1)

def is_sorted(numbers: list, i = 0):
  if i == len(numbers) - 2:
    return numbers[i] <= numbers[i+1]
  return numbers[i] <= numbers[i+1] and is_sorted(numbers, i+1)