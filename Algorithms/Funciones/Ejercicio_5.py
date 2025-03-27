"""
Haga una función que reciba como entrada un mes del año y determine el
número de días transcurridos desde el comienzo del año hasta el primer
día del mes
"""

def days_elapsed(month : int) -> int:
  days_per_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  elapsed_days = 0
  for i in range(month-1):
    elapsed_days += days_per_months[i]
  return elapsed_days

month = int(input("Ingrese un mes del año: "))
if not 1 <= month <= 12:
  print("Debe introducir un mes valido")
  exit()
print(f"Han transcurrido {days_elapsed(month)} desde el inicio del año hasta el mes {month}")