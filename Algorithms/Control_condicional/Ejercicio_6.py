"""
El IMC resulta de la división de la masa del individuo (en kilogramos)
entre el cuadrado de la estatura (en metros). El índice de masa corporal es
un indicador del peso de una persona en relación con su altura.
Clasificación del IMC de acuerdo con la OMS de la ONU:
(a) Menor a 16: Criterio de ingreso.
(b) 16 a 16.9: infrapeso.
(c) 17 a 18.4: bajo peso.
(d) 18.5 a 24.9: peso normal.
(e) 25 a 29.9: sobrepeso.
(f) 30 a 34.9: obesidad premórbida.
(g) 40 a 45: obesidad mórbida.
(h) Mayor a 45: obesidad hipermórbida.
Escriba un algoritmo que dado el peso de una persona en libras (1 libra =
0, 453592 Kg) y su estatura en centímetros, calcule su IMC e indique como
salida el peso en kilogramos, el valor de IMC de la persona y la categoría
en la cual fue clasificado.
"""

weight = float(input("Ingrese su peso en libras: "))
height = float(input("Ingrese su estatura en centimetros: "))

kg_weight = weight * 0.453592
meters_height = height / 100

imc = kg_weight / (meters_height**2)
print(f"Peso en kg: {kg_weight:.2f}")
print(f"IMC: {imc:.2f}")
print("Categoria: ", end="")
if imc < 16: print("Criterio de ingreso")
elif 16 <= imc <= 16.9: print("Infrapeso")
elif 17 <= imc <= 18.4: print("Bajo peso")
elif 18.5 <= imc <= 24.9: print("Peso normal")
elif 25 <= imc <= 29.9: print("Sobrepeso")
elif 30 <= imc <= 34.9: print("Obesidad premorbida") # El enunciado no cubre el rango de 35 a 39.9
elif 35 <= imc <= 45: print("Obesidad morbida")      # asi que coloque el rango de 35 a 45
else: print("Obesidad hipermorbida")