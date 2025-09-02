"""
Defina una clase Monedero que permita gestionar la cantidad de dinero
que una persona dispone en un momento dado. La clase deberá tener un
constructor que permitirá crear un monedero con una cantidad de dinero
inicial y deberá definir un método para meter dinero en el monedero, otro
para sacarlo y finalmente, otro para consultar el disponible; solo podrá
conocerse la cantidad de dinero del monedero a través de este último
método. Por supuesto, no se podrá sacar más dinero del que haya en un
momento dado en el monedero.
"""

class Monedero:

  def __init__(self, monto_inicial):
    if monto_inicial < 0:
      raise ValueError("El monto inicial no debe ser negativo")
    self._monto = monto_inicial # Con '_' indicamos que el atributo es privado

  def consultar(self):
    print(f"Posee ${self._monto}")

  def retirar(self, cantidad):
    if cantidad < 0:
      raise ValueError("El monto a retirar debe ser positivo")
    
    if cantidad <= self.monto:
      self.monto -= cantidad
    else:
      print("Fondos insuficientes")

  def depositar(self, cantidad):
    if cantidad < 0:
      raise ValueError("El monto a depositar debe ser positivo")
    self.monto += cantidad