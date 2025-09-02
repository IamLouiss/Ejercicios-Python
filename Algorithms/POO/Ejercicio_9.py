"""
Defina una clase punto que tendrá dos atributos, de tipo Real x e y,
que representarán las coordenadas del punto dentro del plano. Defina un
método que tenga como argumento otro objeto de la clase punto y que
calcule la distancia entre los dos puntos. Un punto puede estar ubicado en
cualquier parte del sistema de coordenada. Puede definir otros métodos
que considere necesarios.
"""

class Punto:

  def __init__(self, x : float, y : float):
    self.x = x
    self.y = y

  def dist_dos_puntos(self, punto):
    return ((self.x - punto.x)**2 + (self.y - punto.y)**2)**(1/2)
  
  def __str__(self):
    return f"Punto: ({self.x}, {self.y})" # Redefinimos la representacion del objeto como str