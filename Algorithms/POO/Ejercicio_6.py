"""
Especifique una clase que represente productos con las siguientes propiedades:

  • Tienen un código que los identifica de manera única y que se asigna
  automáticamente en el momento de la creación.
  • Guardan la descripción y el precio sin IVA.
  • Todos los productos comparten el mismo IVA (supongamos el 12%),
  que puede variar en función de las decisiones del gobierno.
  • Los productos se dan de alta en una fecha concreta (la fecha de
  creación) lo que nos servirá para conocer cuáles son los productos
  más novedosos o más recientes.

La clase Producto debe proporcionar los métodos adecuados:

  (a) Constructores
  (b) Métodos para consulta y modificación de los atributos
  (c) Método para calcular
"""

class Producto:

  num_productos = 0
  iva = 0.12

  def __init__(self, descripcion, precio_base, fecha_alta):
    self.codigo = Producto.num_productos
    self.desc = descripcion
    self.precio_base = precio_base
    self.fecha_alta = fecha_alta
    Producto.num_productos += 1

  def get_codigo(self):
    return self.codigo
  
  def get_desc(self):
    return self.desc
  
  def get_precio_base(self):
    return self.precio_base
  
  @classmethod
  def get_iva(cls):
    return cls.iva
  
  def get_fecha_alta(self):
    return self.fecha_alta
  
  def calcular_precio(self):
    return self.precio_base + (self.precio_base * self.iva)
  
  def modificar_descripcion(self, nueva_desc):
    self.desc = nueva_desc
  
  def asignar_precio(self, nuevo_precio):
    self.precio_base = nuevo_precio

  @classmethod
  def modificar_iva(cls, nuevo_iva):
    cls.iva = nuevo_iva

  def modificar_fecha_alta(self, nueva_fecha):
    self.fecha_alta = nueva_fecha