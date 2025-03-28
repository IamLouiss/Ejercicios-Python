"""
Haga una acción que tome como entrada una matriz (con cantidad par
de filas) e intercambie las filas pares y las impares. Por ejemplo, si la
matriz es {{4, 2}, {1, 2}, {6, -1}, {3, 5}}, la matriz resultante debería ser
{{1, 2}, {4, 2}, {3, 5}, {6, -1}}
"""

def swap_rows(matrix : list[list[int]]) -> None:
  if len(matrix) % 2 != 0:
    print("La matrix debe tener una cantidad par de filas")
    return
  for i in range(len(matrix) - 1):
    if i % 2 == 0:
      matrix[i], matrix[i+1] = matrix[i+1], matrix[i]

# Usando slicing

def swap_rows_slicing(matrix: list[list[int]]) -> None:
    matrix[::2], matrix[1::2] = matrix[1::2], matrix[::2]

matrix = [
  [4, 2],
  [1, 2],
  [6, -1],
  [3, 5]
]

swap_rows_slicing(matrix)