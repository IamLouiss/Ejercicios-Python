def print_formatted(number):
  width = len(bin(number)[2:]) + 1
  for i in range(1, number+1):
    Decimal = str(i)
    Octal = oct(i)[2:]
    Hexadecimal = hex(i)[2:].upper()
    Binary = bin(i)[2:]
    print(Decimal.rjust(width-1) + Octal.rjust(width) + Hexadecimal.rjust(width) + Binary.rjust(width))

if __name__ == '__main__':
        n = int(input())
        print_formatted(n)