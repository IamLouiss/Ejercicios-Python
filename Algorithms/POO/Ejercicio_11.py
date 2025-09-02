"""
Un centro comercial desea administrar toda la información de sus locales.
Cada local tiene: nombre, RIF, horario, dueño, encargado, tamaño (m^2) y
una lista de empleados. Los locales que pertenecen al centro comercial se
clasifican en:

  • Tiendas de ropas, pudiendo ser estas tiendas para mujeres, hombres o mixtas.
  • Locales de comida, estos pueden ser restaurantes o de comida rápida.
  • Librerías.
  • Una farmacia.

Determinar:

  • La cantidad de librerías del centro comercial.
  • La cantidad de empleados, por sexo, de la farmacia.
  • La cantidad de metros cuadrados que ocupan los locales del centro
  comercial.
"""

class Empleado:

  def __init__(self, nombre, cedula, sexo):
    self.nombre = nombre
    self.cedula = cedula
    self.sexo = sexo

class Local:

  def __init__(self, nombre, rif, horario, dueño, encargado, tamaño, empleados = None):
    self.nombre = nombre
    self.rif = rif
    self.horario = horario
    self.dueño = dueño
    self.encargado = encargado
    self.tamaño = tamaño
    self.empleados = empleados if empleados else []

class TiendaRopa(Local):

  def __init__(self, nombre, rif, horario, dueño, encargado, tamaño, publico, empleados=None):
    super().__init__(nombre, rif, horario, dueño, encargado, tamaño, empleados)
    self.publico = publico

class LocalComida(Local):

  def __init__(self, nombre, rif, horario, dueño, encargado, tamaño, especialidad, empleados=None):
    super().__init__(nombre, rif, horario, dueño, encargado, tamaño, empleados)
    self.especialidad = especialidad

class Libreria(Local):

  def __init__(self, nombre, rif, horario, dueño, encargado, tamaño, empleados=None):
    super().__init__(nombre, rif, horario, dueño, encargado, tamaño, empleados)

class Farmacia(Local):
  
  def __init__(self, nombre, rif, horario, dueño, encargado, tamaño, empleados=None):
    super().__init__(nombre, rif, horario, dueño, encargado, tamaño, empleados)

class CentroComercial:

  def __init__(self, nombre, locales):
    self.nombre = nombre
    self.locales = locales if locales else []

  def agregar_local(self, local : Local):
    self.locales.append(local)

  def cant_librerias(self):
    n = sum(1 for local in self.locales if isinstance(local, Libreria))
    return n

  def cant_empleados_farmacia(self):
    contador = {'masculinos': 0, 'femeninos': 0}
    for local in self.locales:
      if isinstance(local, Farmacia):
        for empleado in local.empleados:
          contador[empleado.sexo] += 1
    return contador

  def metros_cuadrados_totales(self):
    return sum(local.tamaño for local in self.locales)