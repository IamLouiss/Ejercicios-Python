"""
Escriba una clase Corredor que contenga un atributo de tipo entero
denominado energia que indica el valor de la energía como un entero en
el rango [0, 100]. Al crear un corredor, se deberá indicar un valor para la
energía inicial. Se debe verificar que el valor de energía no esté fuera del
rango [0, 100] a través de un procedimiento llamado verificarEnergia().
Si la cantidad pasada por parámetro no es un número entero mayor o igual
a cero, verificarEnergia() mostrará un mensaje al respecto y dejará la
energía en 0; si la energía recargada pasa del valor 100 se deberá dejar
a 100. El corredor tendrá un método recargarEnergia() a la que se le
pasará por parámetro la cantidad que será sumada al atributo energía.
La clase tendrá un método correr() que cada vez que se llame restará
10 puntos de energía del corredor. El método energiaAgotada() debe
verificar si la energía del corredor era menor que 10 al momento de llamar
a correr. Si es menor a 10, la energía quedará en 0, se mostrará un mensaje
indicando que se llegó al mínimo de energía y se mostrará cuál es la energía
del corredor. La clase también tendrá un método entrenar que permitirá al
corredor recuperar energía. Cada vez que se llama a entrenar la energía
del corredor aumentará 15 puntos, teniendo en cuenta que nunca puede
pasar de 100.
"""

class Corredor:

  def __init__(self, energia_inicial):
    self.energia = self.verificar_energia(energia_inicial)

  def verificar_energia(self, energia):
    if energia < 0:
      print("Energia negativa. Se ajusta la energia en 0")
      return 0
    return min(energia, 100)
  
  def recargar_energia(self, energia):
    if energia < 0:
      raise ValueError("Ingrese una cantidad positiva")
    self.energia = self.verificar_energia(self.energia + energia)

  def energia_agotada(self):
    return self.energia < 10

  def correr(self):
    if self.energia_agotada():
      print(f"Energia agotada. Corredor con {self.energia} energia")
      self.energia = 0
      return
    self.energia -= 10

  def entrenar(self):
    self.energia = min(self.energia + 15, 100)