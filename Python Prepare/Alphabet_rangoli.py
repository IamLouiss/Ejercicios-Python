def print_rangoli(size):
  
  al = "abcdefghijklmnopqrstuvwxyz"
  start = size - 1
  max_numbers_letters = size + (size - 1)

  for i in range(size + (size - 1)):
    lista = al[size-1:start:-1] + al[start:size]
    cadena = "-".join(lista)
    print(cadena.center(max_numbers_letters + (max_numbers_letters - 1), "-"))
    if i < (size + (size - 1)) // 2: start -= 1
    else: start += 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)