"""
Escriba un algoritmo que dados la distancia recorrida por un objeto y el
tiempo que tomó el objeto en recorrer esa distancia, calcule su velocidad.
"""

print("Calculo de la velocidad de un objeto dado la distancia y el tiempo")
distance = int(input("Ingrese la distancia recorrida en metros: "))
time = int(input("Ingrese el tiempo tardado en segundos: "))
velocity = distance / time
print(f"Velocidad: {velocity:.2f} m/s")