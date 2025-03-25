"""
Haga un algoritmo que determine si un número es capicúa (palíndrome).
Un número es capicúa si se lee igual al derecho y a revés.
"""

n = int(input("Ingrese un numero: "))

reverse_n = 0
n_copy = abs(n)
print(n_copy)
while n_copy > 0:
  reverse_n *= 10
  reverse_n += n_copy % 10
  n_copy //= 10

print(f"El numero {n} es palindrome" if n == reverse_n or n == -reverse_n else f"El numero {n} no es palindrome")