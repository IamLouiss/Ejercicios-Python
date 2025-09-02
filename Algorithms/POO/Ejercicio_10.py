"""
Una empresa dedicada a la venta de jugos, desea registrar la información de
sus vendedores, respecto a: cedula, nombre, zonaDeVenta, ventasMensuales,
totalAnual y comisión. Donde ventasMensuales representa las ventas realizadas
por el vendedor en cada uno de los doce meses del año, totalAnual
representa la suma de las ventas en un año y comisión un porcentaje que
depende del totalAnual. Además la variable nombre está asociada con una
clase Nombre cuyas instancias representan el apellido, el primerNombre y
el segundoNombre de cada vendedor.

(a) Definir la clase Vendedor y la clase Nombre
(b) Definir en la clase que corresponda los métodos que permitan los
siguientes requerimientos:

  - Crear una instancia de la clase Vendedor y solicitar al usuario
    los datos para inicializar sus variables, excepto las variables
    ventasMensuales, totalAnual y comisión que se inicializan con ceros.
  - Ingresar las ventas de un determinado mes.
  - Determinar la comisión del vendedor, teniendo en cuenta:
    • Si totalAnual < Bs. 50.000, la comisión es cero.
    • Si Bs. 50.000 ≤ totalAnual < Bs. 70.500, la comisión es del 15%.
    • Si Bs. 70.500 ≤ totalAnual < Bs. 100.000, la comisión es del 20%.
    • Si Bs. 100.000 ≤ totalAnual, la comisión es del 30%.
"""

class Nombre:

  def __init__(self, primer_nombre, segundo_nombre, apellido):
    self.pmr_nombre = primer_nombre
    self.seg_nombre = segundo_nombre
    self.apellido = apellido

  def __str__(self):
    return f"{self.pmr_nombre} {self.seg_nombre} {self.apellido}"

class Vendedor:

  def __init__(self, cedula, nombre : Nombre, zona_venta):
    self.cedula = cedula
    self.nombre = nombre
    self.zona_venta = zona_venta
    self.v_mensuales = {}
    self.total_anual = 0
    self.comision = 0

  def ingresar_ventas(self, mes, total):
    if mes < 1 or mes > 12:
      raise ValueError("El mes debe estar entre 1 y 12")
    self.v_mensuales[mes] = total
    self._calcular_total_anual()
    self.determinar_comision()

  def _calcular_total_anual(self):
    self.total_anual = sum(self.v_mensuales.values())

  def determinar_comision(self):
    if self.total_anual < 50000:
      self.comision = 0
    elif 50000 <= self.total_anual < 70500:
      self.comision = 0.15
    elif 70500 <= self.total_anual < 100000:
      self.comision = 0.20
    else:
      self.comision = 0.30