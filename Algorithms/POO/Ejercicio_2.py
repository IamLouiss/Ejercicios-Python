CATEGORIAS_VALIDAS = ["albañilería", "plomería", "electricidad"]
TIPOS_VALIDOS = ["manual", "eléctrica", "motora", "híbrida"]

class Herramienta:
  def __init__(self, nombre, desc, costo, codigo_fabrica, nombre_fabricante, 
               categoria, tipo, **kwargs):

    if categoria not in CATEGORIAS_VALIDAS:
        raise ValueError(f"Categoría inválida. Use: {CATEGORIAS_VALIDAS}")
    if tipo not in TIPOS_VALIDOS:
        raise ValueError(f"Tipo inválido. Use: {TIPOS_VALIDOS}")
    
    self.nombre = nombre
    self.desc = desc
    self.costo = costo
    self.codigo_fabrica = codigo_fabrica
    self.nombre_fabricante = nombre_fabricante
    self.categoria = categoria
    self.tipo = tipo
    
    # Atributos opcionales segun el tipo de herramienta
    self.voltaje = kwargs.get('voltaje')
    self.bateria = kwargs.get('bateria')
    self.potencia_motor = kwargs.get('potencia_motor')
    self.combustible = kwargs.get('combustible')
    self.aceite = kwargs.get('aceite')