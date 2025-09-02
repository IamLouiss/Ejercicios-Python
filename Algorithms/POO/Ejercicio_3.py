"""
Una cátedra tiene como equipo docente un responsable y un conjunto
de entre 1 y 4 auxiliares. Para aprobar la materia, cada alumno debe
superar las 3 instancias de evaluación previstas: 1 parcial (que puede ser
recuperado), 1 trabajo práctico y examen final. La cátedra lleva un registro
de fecha y resultado de cada una de las evaluaciones realizadas por los
alumnos. Además de estos dos datos, para los trabajos prácticos se guarda
información respecto al retraso en la fecha de entrega (si lo hubiera) y para
los exámenes finales en qué mesa y en qué llamados el alumno rindió el
examen.
"""

class Persona:

  def __init__(self, nombre, rol):
    self.nombre = nombre
    self.rol = rol

class Alumno(Persona):

  def __init__(self, nombre, rol):
    super().__init__(nombre, 'alumno')
    self.notas = []

class Docente(Persona):

  def __init__(self, nombre, rol):
    super().__init__(nombre, rol) # Rol: docente o auxiliar

class Evaluacion:

  def __init__(self, tipo, fecha, aprobado):
    self.tipo = tipo
    self.fecha = fecha
    self.aprobado = aprobado

class Parcial(Evaluacion):

  def __init__(self, tipo, fecha, aprobado, es_recuperado = False):
    super().__init__('parcial', fecha, aprobado)
    self.es_recuperado = es_recuperado

class TrabajoPractico(Evaluacion):

  def __init__(self, tipo, fecha, dias_retraso = 0):
    super().__init__(tipo, fecha)
    self.dias_retraso = dias_retraso

class ExamenFinal(Evaluacion):

  def __init__(self, tipo, fecha, mesa, llamado):
    super().__init__(tipo, fecha)
    self.mesa = mesa
    self.llamado = llamado

class Catedra:

  def __init__(self, docente, auxiliares = None):
    self.docente = docente
    self.auxiliares = []
    self.alumnos = []