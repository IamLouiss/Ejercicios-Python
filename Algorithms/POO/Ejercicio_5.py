"""
Escribir la clase Fraccion que contenga los siguientes métodos:

  - Fraccion(N1,N2): Constructor que recibe valores enteros para el numerador(N1) y el denominador (N2).
  - Sumar(b): Sumar la fracción b a la fracción invocante.
  - Multiplicar(b): Multiplicar la fracción b a la fracción invocante.
  - Dividir(b): Dividir la fracción b a la fracción invocante.
  - Comparar(b): Retorna verdadero si la fracción invocante es igual a b, sino retorna falso.
  - Simplificar(): Simplificar la fracción.
  - aString(): Devuelve un String con la fracción llamante expresada en la forma N1/N2.

Escriba adicionalmente, un algoritmo principal que utilice la clase Fraccion
para almacenar tres fracciones dadas por el usuario (F1, F2, F3) y calcule
la suma de F1 + F2 + F3, la multiplicación de F1 * F3, la división de F2
entre F1 e imprima los tres resultados.
"""

class Fraccion:

  def __init__(self, numerador : int, denominador : int):
    if denominador == 0:
      raise ValueError("El denominador no puede ser cero")
    self.num = numerador
    self.den = denominador

  def mcd(self, a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

  def sumar(self, fraccion):
    if self.den == fraccion.den:
      return Fraccion(self.num + fraccion.num, self.den).simplificar()
    nuevo_den = self.den * fraccion.den
    nuevo_num = (((nuevo_den // self.den) * self.num) + (nuevo_den // fraccion.den) * fraccion.num)
    return Fraccion(nuevo_num, nuevo_den).simplificar()

  def multiplicar(self, fraccion):
    nuevo_num = self.num * fraccion.num
    nuevo_den = self.den * fraccion.den
    return Fraccion(nuevo_num, nuevo_den).simplificar()

  def dividir(self, fraccion):
    if fraccion.num == 0:
      raise ValueError("No se puede dividir por cero")
    nuevo_num = self.num * fraccion.den
    nuevo_den = self.den * fraccion.num
    return Fraccion(nuevo_num, nuevo_den).simplificar()

  def comparar(self, fraccion):
    return self.num == fraccion.num and self.den == fraccion.den
  
  def simplificar(self):
    mcd = self.mcd(self.num, self.den)
    nuevo_num = self.num // mcd
    nuevo_den = self.den // mcd
  
    if nuevo_den < 0:
      nuevo_num *= -1
      nuevo_den *= -1
    return Fraccion(nuevo_num, nuevo_den)

  def aString(self):
    return f"{self.num}/{self.den}"
  
def operaciones(F1, F2, F3):
  suma = F1.sumar(F2).sumar(F3)
  multiplicacion = F1.multiplicar(F3)
  division = F2.dividir(F1)

  print(f"Suma F1 + F2 + F3 = {suma.aString()}")
  print(f"Multiplicacion F1 * F3 = {multiplicacion.aString()}")
  print(f"Division F2 / F1 = {division.aString()}")