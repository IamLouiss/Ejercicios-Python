"""
Escriba un algoritmo lea una secuencia de dígitos entre 0 y 9 terminada en
-1 que representan un número decimal e imprima el número decimal. Por
ejemplo, si la secuencia de entrada es 5 0 3 8 -1 debe imprimir 5038.
"""
number = 0
while True:
  entry = int(input("Ingrese un numero entre 0 y 9 o -1 para finalizar: "))
  if entry == -1: break
  if entry < 0 or entry > 9:
    print("El numero debe estar en el rango indicado")
    continue
  else:
    number = (number * 10) + entry
print("No se ingresaron datos" if number == 0
      else f"El numero construido a partir de la secuencia es: {number}")