"""
Haga una acción que tome como entrada un arreglo de enteros A y un
elemento K y coloque K en las posiciones potencia de dos del arreglo (1,
2, 4, 8, . . .).
"""

def insert_in_power_two_positions(number_list : list[int], k : int):
  if not number_list: return
  power = 1
  for i in range(len(number_list)): # 1, 2, 4, 8, 16, 32
    if i == power:
      number_list[i] = k
      power *= 2
  
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
k = 10
insert_in_power_two_positions(number_list, k)
print(number_list)