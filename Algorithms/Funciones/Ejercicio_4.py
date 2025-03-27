"""
Escriba una función o acción que reciba por parámetro 5 números y
determine el máximo y mínimo entre ellos"
"""

# Usando max y min con tuplas

def find_max_min(n1, n2, n3, n4, n5):
  """Encuentra el numero maximo y minimo usando funciones integradas"""
  max_number = max((n1, n2, n3, n4, n5))
  min_number = min((n1, n2, n3, n4, n5))
  print(f"El numero maximo es: {max_number}")
  print(f"El numero minimo es: {min_number}")

# Version manual con condicionales

def find_max_min_manual(n1, n2, n3, n4, n5):
  max_number = n1
  if n2 > max_number: max_number = n2
  if n3 > max_number: max_number = n3
  if n4 > max_number: max_number = n4
  if n5 > max_number: max_number = n5
  min_number = n1
  if n2 < min_number: min_number = n2
  if n3 < min_number: min_number = n3
  if n4 < min_number: min_number = n4
  if n5 < min_number: min_number = n5
  print(f"El numero maximo es {max_number}")
  print(f"El numero minimo es {min_number}")

find_max_min(1,2,3,4,5)
find_max_min_manual(1,2,3,4,5)