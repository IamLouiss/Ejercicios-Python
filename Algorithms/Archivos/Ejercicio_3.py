"""
Haga un algoritmo que lea todos los caracteres de un archivo
y cuente la frecuencia de cada letra del archivo
"""

def letter_frequency(text : str, letter : str):
  return text.count(letter)

file = open("textos_prueba\\texto_prueba.txt", "r")
text = file.read()
print(letter_frequency(text, "l"))
file.close()