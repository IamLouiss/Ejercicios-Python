"""
Cree un algoritmo que tome como entrada la hora exacta (horas, minutos,
segundos y AM/PM) e indique el número de segundos transcurridos durante
ese día.
"""

hour = int(input("Ingrese la hora: "))
minutes = int(input("Ingrese los minutos: "))
seconds = int(input("Ingrese los segudos: "))
pm = bool(int(input("Ingrese 0 si es AM o 1 si es PM: ")))

if not (1 <= hour <= 12) or not (0 <= minutes <= 59) or not (0 <= seconds <= 59):
  print("La hora no debe ser mayor a 12 y los minutos y segundos no deben ser mayores a 59")
else:
  total_seconds = 0
  if pm and hour != 12: total_seconds += (12 * 3600)
  total_seconds += (hour * 3600) + (minutes * 60) + seconds
  print(total_seconds)