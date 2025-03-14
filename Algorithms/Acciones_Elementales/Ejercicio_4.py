"""
Escriba un algoritmo que dadas las longitudes de los catetos de un triángulo
rectángulo calcule la longitud de su hipotenusa.
"""

print("Calculo de la hipotenusa de un triangulo")
a = float(input("Ingrese el valor del cateto a: "))
b = float(input("Ingrese el valor del cateto b: "))

c = (a**2 + b**2)**(1/2)
print(f"La longitud de la hipotenusa es: {c}")