"""
Haga un algoritmo que lea números enteros almacenados en dos archivos
que contienen números enteros ordenados y genere un tercer archivo que
contiene los mismos elementos de los dos archivos ordenados. Por ejemplo, si
el primer archivo contiene los elementos 1 40 50 100 y el segundo contiene
los elementos 5 20 40 80, el archivo resultante tendría los elementos:
1 5 20 40 40 50 80 100
"""

def read_file(path : str) -> str:
  with open(path, "r") as file:
    return file.read()

def write_file(file_name : str, content : str):
  with open(file_name, "w") as file:
    file.write(content)

nums_1 = [int(num) for num in read_file("textos_prueba\\nums_1.txt").split()]
nums_2 = [int(num) for num in read_file("textos_prueba\\nums_2.txt").split()]
sorted_numbers = [str(num) for num in sorted(nums_1 + nums_2)]
text = " ".join(sorted_numbers)
write_file("textos_prueba\\nums_3.txt", text)