"""
Haga una función que tome como entrada una matriz cuadrada de N x M y
retorne la matriz traspuesta de M x N. Recuerde que la matriz traspuesta
es aquella en donde se intercambian filas por columnas. Por ejemplo,
si la matriz original es A = {{1, 5}, {2, 3}}, la función debe retornar
{{1, 2}{5, 3}}.
"""

def transposed_matrix(matrix : list[list[int]]) -> list[list[int]]:
  transposed = []
  for i in range(len(matrix)):
    row = []
    for j in range(len(matrix)):
      row.append(matrix[j][i])
    transposed.append(row)
  return transposed
  
matrix = [[1, 5], [2, 3]]
transposed = transposed_matrix(matrix)
print(transposed)