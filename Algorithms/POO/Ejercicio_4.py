"""
Se quiere definir una clase que permita controlar un sintonizador digital
de emisoras FM; concretamente, lo que se desea es dotar al controlador
de una interfaz que permita subir (up) o bajar (down) la frecuencia (en
saltos de 0.5 MHz) y mostrar la frecuencia sintonizada en un momento
dado (display). Supondremos que el rango de frecuencias a manejar oscila
entre los 80 Mhz y los 108 MHz y que al inicio, el controlador sintoniza a
80 MHz. Si durante una operación de subida o bajada se sobrepasa uno de
los dos límites, la frecuencia sintonizada debe pasar a ser la del extremo
contrario.
"""

class Sintonizador:

  def __init__(self, frecuencia_inicial = 80.0):
    if not(80 <= frecuencia_inicial <= 108):
      raise ValueError("Frecuencia inicial fuera de rango (80 - 108 MHz)")
    self.frecuencia = frecuencia_inicial

  def display(self):
    print(f"{self.frecuencia} MHz")

  def up(self):
    self.frecuencia += 0.5
    if self.frecuencia > 108:
      self.frecuencia = 80

  def down(self):
    self.frecuencia -= 0.5
    if self.frecuencia < 80:
      self.frecuencia = 108