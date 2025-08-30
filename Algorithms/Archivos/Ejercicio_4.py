"""
Dado un archivo personas.txt con información sobre personas, se desea
que usted haga un algoritmo que lea el archivo y lo cargue en un arreglo
de registros. Luego, debe almacenar en otro archivo únicamente las cédulas
y edades de las personas que tengan más de 18 años. La primera línea del
archivo personas.txt contiene el número N de personas almacenadas en
el archivo. Por cada persona habrá una línea con su cédula, luego una línea
con su nombre completo, luego una línea con su edad, y finalmente una
línea con su sexo. A lo sumo habrán 100 personas en el archivo. El registro
para almacenar la información de una persona es el siguiente:

struct Persona
{
  int cedula;
  string nombre;
  int edad;
  char sexo;
};
"""

class Persona:

  def __init__(self, cedula, nombre, edad, sexo):
    self.cedula = int(cedula)
    self.nombre = nombre
    self.edad = int(edad)
    self.sexo = sexo

with open("textos_prueba\\personas.txt", "r") as file:
  archivo = file.read().splitlines()

num_personas = int(archivo.pop(0))
personas = []

for i in range(num_personas):
  personas.append(Persona(*archivo[4*i:4*(i+1)]))

with open("textos_prueba\\mayores_18_años.txt", "w") as file:
  contenido = ""
  for persona in personas:
    if persona.edad > 18:
      contenido += f"{persona.cedula}\n{persona.edad}\n"
  file.write(contenido.rstrip("\n")) # --> Eliminar el ultimo salto de linea