"""
Escriba un algoritmo que reciba como entrada una fecha (día y mes) del
año actual e imprima por pantalla el número de días transcurridos desde
el 1ro de Enero.
"""

day = int(input("Ingrese el dia: "))
month = int(input("Ingrese el mes: "))

days_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_days = 0
if month == 1:
  total_days += day
else:
  for i in range(0, month-1):
    total_days += days_months[i]
  total_days += day
print(f"Dias trascurridos en el año: {total_days}")