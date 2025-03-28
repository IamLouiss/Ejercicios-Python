"""
Haga una función que tome como entrada una matriz cuadrada y retorne
la suma de los elementos de la diagonal secundaria.
"""

def secondary_diagonal_sum(matrix : list[list[int]]) -> int:
  sum = 0
  for i in range(len(matrix)):
    sum += matrix[len(matrix) - 1 - i][i]
  return sum

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]
print(secondary_diagonal_sum(matrix))