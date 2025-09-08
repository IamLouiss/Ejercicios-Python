"""
Elabore una función recursiva la cual dado un arreglo  de caracteres que forman una palabra retorne verdadero si 
ésta es capicúa. Ejemplos palabras capicúas: salas, oro, arepera. 
"""

def capicua(chars : list, i = 0):
  if i == len(chars) // 2:
    return True
  if chars[i] == chars[len(chars) - 1 - i]:
    return capicua(chars, i+1)
  else:
    return False