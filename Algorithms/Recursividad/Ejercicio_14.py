"""
Sabiendo que 0 es par, es decir:

EsPar(0) = true 
EsImpar(0) = false

Y la paridad de cualquier otro entero positivo es la opuesta que la del entero anterior, desarrolle las funciones lógicas, 
mutuamente recursivas, EsPar y EsImpar, que se complementen a la hora de averiguar la paridad de un entero positivo.
"""

def es_par(n: int):
  if n == 0:
    return True
  return es_impar(n-1)
  
def es_impar(n: int):
  if n == 0:
    return False
  return es_par(n-1)