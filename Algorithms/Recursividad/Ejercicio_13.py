"""
Suponga que solo cuenta con un lenguaje cuyas operaciones aritméticas
son +, -, /; diseñe una función recursiva la cual, dados dos reales A y
B, retorne como resultado la evaluación de A * B. 
"""

def multiply(a: float, b: float) -> float:
  if a == 0 or b == 0:
    return 0
  if b == 1:
    return a
  
  signo = 1
  if (a < 0) != (b < 0):
    signo = -1
  
  a_abs = -a if a < 0 else a
  b_abs = -b if b < 0 else b
  
  if b_abs > 1:
    resultado = a_abs + multiply(a_abs, b_abs - 1)
  else:
    resultado = a_abs
  
  return resultado / signo