"""
Un punto en 3 dimensiones tiene tres coordenadas X, Y, Z. Defina
un registro para representarlos. Usando el registro definido anteriormente,
haga una función que calcule la distancia entre dos puntos. Recuerde
que la distancia D entre dos puntos P y Q viene dada por: 
d = √((Px - Qx)^2 + (Py - Qy)^2 + (Pz - Qz)^2)
"""

class PuntoTridimensional:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

def distancia_dos_puntos(P, Q):
  return ((P.x - Q.x)**2 + (P.y - Q.y)**2 + (P.z - Q.z)**2)**(1/2)

p1 = PuntoTridimensional(2, 3, 5)
p2 = PuntoTridimensional(7, 1, 9)

print(distancia_dos_puntos(p1, p2))