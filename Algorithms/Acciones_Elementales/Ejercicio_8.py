"""
José y Pedro son dos ranas. José puede dar saltos de J centímetros y
Pedro puede dar saltos de P centímetros. Suponiendo que ambas ranas
comienzan a saltar en el mismo punto (y en la misma dirección), haga
un algoritmo que determine si las ranas coincidirán en el mismo punto en
algún momento antes de que José de K saltos.
"""

def mcd(a : int, b : int) -> int:
  if b == 0: return a
  return mcd(b, a % b)


j = float(input("Ingrese los centimetros en los que salta Jose: "))
p = float(input("Ingrese los centimetros en los que salta Pedro: "))
k = int(input("Ingrese la cantidad de saltos que dará Jose: "))

mcm = (j * p) // mcd(j, p)
total_distance_jose = j * k
print(f"Coinciden a los {mcm} cm" if mcm <= total_distance_jose
       else "No coinciden")