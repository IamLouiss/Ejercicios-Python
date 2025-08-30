"""
En una tienda se tienen diferentes tipos de productos. Cada producto tiene
un código, una descipción, un nombre y un precio. Existen varios tipos
de productos. Cada tipo de producto tiene un nombre, un código y 10
productos.

(a) Se desea que define las estructuras de datos para almacenar un producto,
y para almacenar un tipo de producto.

(b) Supongamos ahora que tenemos un arreglo con 5 tipos de productos
y deseamos aumentar en un 10% el precio de todos los productos que
sean de un tipo con código C.

(c) Haga una función que dado un código de producto P busque el
producto en toda la estructura de datos y retorne verdadero si el
producto existe o falso en caso contrario.
"""

class Product:
  def __init__(self, code : int, description : str, price : float):
    self.code = code
    self.description = description
    self.price = price

  def __str__(self):
    return f"{self.code} -- {self.description} -- ${self.price}"

class Product_type:
  def __init__(self, name : str, code : int):
    self.name = name
    self.code = code
    self.products = []

  def __str__(self):
    return f"{self.name}({self.code})"
  
  def add_product(self, p_code : int, p_description : str, p_price : float):
    if len(self.products) >= 10:
      print("No se pueden agregar mas de 10 productos")
      return
    product = Product(p_code, p_description, p_price)
    self.products.append(product)

def add_percentage_price(types_of_products : list, percent = 0.10):
  for type in types_of_products:
    for product in type.products:
      product.price += (product.price * percent)

def is_existing_product(P: int, types_of_products: list) -> bool:
  for product_type in types_of_products:
    for product in product_type.products:
      if product.code == P:
        return True
  return False

products = []
types_of_products = []