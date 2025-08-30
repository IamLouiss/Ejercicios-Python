"""
En una tienda se tienen diferentes tipos de productos. Cada producto tiene
un código, una descipción, un nombre y un precio. Existen varios tipos
de productos. Cada tipo de producto tiene un nombre, un código y 10
productos.

(a) Se desea que define las estructuras de datos para almacenar un producto
y un tipo de producto.

(b) Supongamos ahora que tenemos un arreglo con 5 tipos de productos
y deseamos aumentar en un 10% el precio de todos los productos que
sean de un tipo con código C.

(c) Haga una función que dado un código de producto P busque el
producto en toda la estructura de datos y retorne verdadero si el
prodcuto existe o falso en caso contrario.
"""

class Producto:

  def __init__(self, codigo, descripcion, nombre, precio):
    self.codigo = codigo
    self.descripcion = descripcion
    self.nombre = nombre
    self.precio = precio

class TipoProducto:

  def __init__(self, nombre, codigo):
    self.nombre = nombre
    self.codigo = codigo
    self.productos = []

  def agregar_producto(self, producto):
    if len(self.productos) < 10:
      self.productos.append(producto)
    else:
      raise ValueError("Un tipo de producto no puede tener mas de 10 productos")

  def buscar_producto(self, codigo):
    for producto in self.productos:
      if producto.codigo == codigo:
        return producto
    return None

def existe_producto(codigo, tipos_productos):
  for tipo_producto in tipos_productos:
    if tipo_producto.buscar_producto(codigo):
      return True
  return False

def aumentar_precio_productos(codigo, porcentaje, tipos_productos):
  for tipo_producto in tipos_productos:
    for producto in tipo_producto.productos:
      if producto.codigo == codigo:
        producto.precio += producto.precio * porcentaje