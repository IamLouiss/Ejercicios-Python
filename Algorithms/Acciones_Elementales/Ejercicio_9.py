"""
Dadas las ecuaciones de dos rectas no paralelas y = m1x+b1 y y = m2x+b2,
escribir un algoritmo que calcule su punto de intersección.
"""

print("Calculo de la interseccion entre dos curvas")
print("Para las ecuaciones y = m1x+b1, y = m2x+b2")
m1, b1 = input("Ingres los valores de m1 y b1 separados por un espacio: ").split()
m1 , b1 = float(m1), float(b1)
m2, b2 = input("Ingres los valores de m2 y b2 separados por un espacio: ").split()
m2 , b2 = float(m2), float(b2)

if m1 == m2:
  if b1 == b2: print("Las rectas son iguales, por lo que se intersectan en infinitos puntos")
  else: print("Las rectas son paralelas, por lo que nunca se intersectan")
else:
  x = (b2 - b1) / (m1 - m2)
  print(f"Las rectan se intersectan en el punto ({x:.2f},{(m1 * x) + b1:.2f})")