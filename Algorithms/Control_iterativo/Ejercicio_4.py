"""
Dada una secuencia de números terminada en cero, elaborar un algoritmo
para calcular el porcentaje y la suma de los números impares, el porcentaje
y la suma de los números pares, y la suma de todos los números, y cuántos
números fueron ingresados.
"""

sum_even = 0
sum_odd = 0
total_sum = 0
count_even = 0
count_odd = 0
count = 0

while True:
  current_number = int(input("Ingrese un numero o 0 para finalizar: "))
  if current_number == 0: break
  if current_number % 2 == 0:
    sum_even += current_number
    count_even += 1
  else:
    sum_odd += current_number
    count_odd += 1
  total_sum += current_number
  count += 1

if count > 0:
  print(f"La secuencia tiene {count} numeros",
        f"El porcentaje de numeros pares es {(count_even/count)*100}% y su suma es: {sum_even}",
        f"El porcentaje de numeros impares es {(count_odd/count)*100}% y su suma es: {sum_odd}",
        f"La suma total de los numeros es: {total_sum}", sep="\n")
else:
  print("Debe ingresar una secuencia valida")