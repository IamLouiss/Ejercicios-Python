"""
Haga una acción que tome como entrada un arreglo A de enteros y un
número entero K y realice K desplazamientos circulares de A hacia la
izquierda. Por ejemplo, si A = {4, 6, -1, 2} y K = 2, el valor final de A
debe ser {-1, 2, 4, 6}.
"""

# Usando slicing (mas optimizado)

def circular_displacement_slicing(number_list : list[int], k : int) -> None:
  k = k % len(number_list)
  number_list[:] = number_list[k:] + number_list[:k]

# Usando bucles 

def circular_displacement(number_list : list[int], k : int) -> None:
  for i in range(k):
    aux = number_list[0]
    for j in range(len(number_list) - 1):
      number_list[j] = number_list[j+1]
    number_list[len(number_list) - 1] = aux

number_list = [1, 2, 3, 4]
k = 4
circular_displacement_slicing(number_list, k)
print(f"Lista desplazada circularmente a la izquierda {k} posiciones: {number_list}")