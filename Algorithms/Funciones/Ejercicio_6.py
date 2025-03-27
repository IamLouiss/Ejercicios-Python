"""
Haga una función que utilice la función creada en el problema (5) para
crear otra función que tome como entrada dos fechas (día, mes y año)
y calcule el número de días transcurridos entre las fechas. Puede asumir
también que existe una función para determinar si un año es bisiesto
"""

def is_leap_year(year):
  return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

def days_elapsed(month : int, leap = False) -> int:
  days_per_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if leap: days_per_months[1] = 29
  elapsed_days = 0
  for i in range(month-1):
    elapsed_days += days_per_months[i]
  return elapsed_days

def get_month_days(month, leap = False):
  days_per_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if leap: days_per_months[1] = 29
  return days_per_months[month-1]

def days_between_dates(day1, month1, year1, day2, month2, year2):
  year1_in_days = 0
  year2_in_days = 0

  for i in range(1, year1):
    year1_in_days += 366 if is_leap_year(i) else 365
  for i in range(1, year2):
    year2_in_days += 366 if is_leap_year(i) else 365

  date1_to_days = year1_in_days + days_elapsed(month1, is_leap_year(year1)) + day1
  date2_to_days = year2_in_days + days_elapsed(month2, is_leap_year(year2)) + day2

  return abs(date1_to_days - date2_to_days)

day1, month1, year1 = input("Ingrese la primera fecha en el formato (dia mes año), separados por un espacio: ").split()
day2, month2, year2 = input("Ingrese la segunda fecha en el formato (dia mes año), separados por un espacio: ").split()

day1, month1, year1 = int(day1), int(month1), int(year1)
day2, month2, year2 = int(day2), int(month2), int(year2)

if (not 1 <= day1 <= get_month_days(month1, is_leap_year(year1))) or (not 1 <= day2 <= get_month_days(month2, is_leap_year(year2))):
  print("Introduzca dias validos")
  exit()
if (not 1 <= month1 <= 12) or (not 1 <= month2 <= 12):
  print("Introduzca meses validos")
  exit()

print(f"Dias transcurridos entre las dos fechas: {days_between_dates(day1, month1, year1, day2, month2, year2)} dias")