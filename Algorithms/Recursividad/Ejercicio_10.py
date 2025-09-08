"""
Elabore un algoritmo recursivo el cual dado un arreglo de enteros
ordenado en forma ascendente y sin elementos repetidos, haga una
búsqueda binaria de un elemento E indicando si éste existe en el mismo.
"""

def binary_search(arr, e, low=0, high=None):
  if high is None:
    high = len(arr) - 1
    
  if low > high:
    return False
  
  mid = (low + high) // 2
  
  if arr[mid] == e:
    return True
  elif arr[mid] > e:
    return binary_search(arr, e, low, mid - 1)
  else:
    return binary_search(arr, e, mid + 1, high)