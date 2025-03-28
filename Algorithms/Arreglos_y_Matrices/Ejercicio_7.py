"""
Dado un arreglo con valores entre 0 y 100 haga una función para determinar
el valor que mas se repite.
"""

def most_repeated_value(values_list : list[int]) -> int:
  most_repeated = None
  max_count = 0
  for i in range(len(values_list)):
    current_count = 0
    for j in range(len(values_list)):
      if values_list[i] == values_list[j]: current_count += 1
    if current_count > max_count:
      most_repeated = values_list[i]
      max_count = current_count
  return most_repeated

# Usando count()

def most_repeated_value_count(values_list : list[int]) -> int:
  most_repeated = None
  max_count = 0
  for value in values_list:
    current_count = values_list.count(value)
    if current_count > max_count:
      max_count = current_count
      most_repeated = value
  return most_repeated

number_list = [1, 2, 2, 2, 3, 3, 3, 3, 4]
print(most_repeated_value(number_list))
print(most_repeated_value_count(number_list))