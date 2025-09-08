"""
Escribir un programa recursivo que ordene un arreglo de enteros por el
método de Mezcla: se va dividiendo el arreglo sucesivamente en dos mitades
y cuando la longitud de cada mitad sea 2 se comparan los elementos y se
ordenan. Después de ordenadas las dos mitades, ambas se mezclan ordenadamente
en un solo arreglo aprovechando el hecho de que las mitades ya están ordenadas. 
"""

def merge_sort(arr):
  """Merge sort dividiendo hasta subarreglos de dos elementos"""
  if len(arr) <= 1:
    return arr
  if len(arr) == 2:
    if arr[0] > arr[1]:
      return [arr[1], arr[0]]
    return arr
  
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  print(right)

  return merge(left, right)

def merge(left, right):
  result = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result