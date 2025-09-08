"""
Dado un número entero positivo o nulo (en base decimal), construya
un algoritmo recursivo que tenga por resultado otro número entero
cuyo valor sea la representación en binario (en base 2) del valor dado.
Haga el mismo proceso para base 16.
"""

def to_binary(n : int):
  if n <= 1:
    return str(n)
  return to_binary(n // 2) + str(n % 2)

def to_hex(n : int):
  hex_digits = "0123456789ABCDEF"
  if n < 16:
    return hex_digits[n]
  return to_hex(n // 16) + hex_digits[n % 16]