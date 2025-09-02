"""
Los productos que comercializa una determinada empresa son libros y
CD. Cada producto viene caracterizado por un código que lo identifica de
manera única, el precio base del mercado, y el IVA que se le aplica que es
diferente en cada caso, el 8% para los libros y el 12% para los CD. Además
las características propias de cada tipo de producto son para los Libros:
título, autor(es), año de publicación, editorial, ISBN y para los CD: título,
intérprete, año de publicación. Por otro lado, esta empresa aplica un 20%
de descuento a los libros y un 10% a los CD. Por tanto, el precio de venta
de cada producto se calculará como: precio base + %IVA - dto. Defina las
clases que sean necesarias para representar los distintos tipos de productos
que acabamos de especificar.
"""

class Producto:

  def __init__(self, codigo, precio_base):
    self.codigo = codigo
    self.precio_base = precio_base

class Libro(Producto):

  def __init__(self, codigo, precio_base, titulo, autores, año_publicacion, editorial, isbn):
    super().__init__(codigo, precio_base)
    self.iva = 0.08
    self.titulo = titulo
    self.autores = autores
    self.año_publicacion = año_publicacion
    self.editorial = editorial
    self.isbn = isbn
    self.descuento = 0.20

  @property
  def precio_venta(self):
    iva = self.precio_base * self.iva
    descuento = self.precio_base * self.descuento
    return self.precio_base + iva - descuento

class CD(Producto):

  def __init__(self, codigo, precio_base, titulo, interprete, año_publicacion):
    super().__init__(codigo, precio_base)
    self.iva = 0.12
    self.titulo = titulo
    self.interprete = interprete
    self.año_publicacion = año_publicacion
    self.descuento = 0.10

  @property
  def precio_venta(self):
    iva = self.precio_base * self.iva
    descuento = self.precio_base * self.descuento
    return self.precio_base + iva - descuento