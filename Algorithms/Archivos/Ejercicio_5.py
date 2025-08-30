"""
Un consultorio médico realiza el diagnóstico de las posibles enfermedades
que sufren sus pacientes confrontando la información de los síntomas que
presenta el paciente con la información de los síntomas que caracterizan las
enfermedades por ellos registradas, Así, a un paciente se le diagnostica una
enfermedad si sus síntomas coinciden exactamente con los registrados para
esa enfermedad. Considerando que dicho consultorio tiene caracterizadas a
M enfermedades con a lo sumo N síntomas cada una, elabore un algoritmo
que dada una muestra de K pacientes (nombre, sexo, edad y síntomas)
indique:

  • La enfermedad más frecuente.
  • El porcentaje de cada enfermedad por sexo.
"""

class Paciente:

  def __init__(self, nombre, sexo, edad, sintomas):
    self.nombre = nombre
    self.sexo = sexo
    self.edad = edad
    self.sintomas = list(sintomas)

class Enfermedad:

  def __init__(self, nombre, sintomas = None):
    self.nombre = nombre
    self.sintomas = list(sintomas) if sintomas else []
    self.cant_enfermos_total = 0
    self.cant_enfermos_masc = 0
    self.cant_enfermos_fem = 0

enfermedades = [
  Enfermedad("Gripe", ["fiebre", "tos", "dolor cabeza"]),
  Enfermedad("COVID", ["fiebre", "tos", "perdida olfato"]),
  Enfermedad("Alergia", ["estornudos", "picor ojos"])
]

pacientes = [
  Paciente("Juan", "masculino", 25, ["fiebre", "tos", "dolor cabeza"]),
  Paciente("Maria", "femenino", 30, ["fiebre", "tos", "perdida olfato"]),
  Paciente("Carlos", "masculino", 40, ["fiebre", "tos", "dolor cabeza"]),
  Paciente("Ana", "femenino", 35, ["estornudos", "picor ojos"]),
  Paciente("Luis", "masculino", 28, ["fiebre", "tos", "perdida olfato"]),
  Paciente("Pedro", "masculino", 32, ["fiebre", "tos", "perdida olfato"])
]

for paciente in pacientes:
  for enfermedad in enfermedades:
    if paciente.sintomas == enfermedad.sintomas:
      enfermedad.cant_enfermos_total += 1
      if paciente.sexo == 'masculino':
        enfermedad.cant_enfermos_masc += 1
      else:
        enfermedad.cant_enfermos_fem += 1

enfermedad_frecuente = max(enfermedades, key=lambda x: x.cant_enfermos_total)

total_masculinos = sum(1 for paciente in pacientes if paciente.sexo == 'masculino')
total_femeninos = sum(1 for paciente in pacientes if paciente.sexo == 'femenino')

porc_masculinos = {}
porc_femeninos = {}

for enfermedad in enfermedades:
  porc_masculinos[enfermedad.nombre] = (enfermedad.cant_enfermos_masc / total_masculinos) * 100
  porc_femeninos[enfermedad.nombre] = (enfermedad.cant_enfermos_fem / total_femeninos) * 100

print(f"Enfermedad mas frecuente: {enfermedad_frecuente.nombre}")
print("Porcentaje de enfermedades en pacientes masculinos:")
for key, value in porc_masculinos.items():
  print(f"  {key} = {value}%")
print("Porcentaje de enfermedades en pacientes femeninos:")
for key, value in porc_femeninos.items():
  print(f"  {key} = {value}%")