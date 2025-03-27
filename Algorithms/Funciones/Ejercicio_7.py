"""
Haga una función para determinar si un punto (X, Y) está dentro de un
rectángulo. El rectángulo es definido por la coordenada del vértice superior
izquierdo, su altura y su ancho.
"""

def inside_rectangle(p_x, p_y, x_rect, y_rect, height, width):
  return (x_rect <= p_x <= (width + x_rect)) and ((y_rect - height) <= p_y <= y_rect)

p_x = int(input("Ingrese la coordenada x del punto: "))
p_y = int(input("Ingrese la coordenada y del punto: "))
rect_x = int(input("Ingrese la coordenada x del vertice superior izquierdo del rectangulo: "))
rect_y = int(input("Ingrese la coordenada y del vertice superior izquierdo del rectangulo: "))
height = int(input("Ingrese la altura del rectangulo: "))
width = int(input("Ingrese el ancho del rectangulo: "))

print(f"El punto esta dentro del rectangulo" if inside_rectangle(p_x, p_y, rect_x, rect_y, height, width)
      else "El punto esta fuera del rentangulo")