"""
Usando la función desarrollada en el problema (7) haga una función que
tome como entrada dos rectángulos y determine si algún vértice del 1er
rectángulo está contenido en el 2do rectángulo.
"""

def inside_rectangle(p_x, p_y, x_rect, y_rect, height, width):
  return (x_rect <= p_x <= (width + x_rect)) and ((y_rect - height) <= p_y <= y_rect)

rect_x1 = int(input("Ingrese la coordenada x del vertice superior izquierdo del primer rectangulo: "))
rect_y1 = int(input("Ingrese la coordenada y del vertice superior izquierdo del primer rectangulo: "))
height1 = int(input("Ingrese la altura del primer rectangulo: "))
width1 = int(input("Ingrese el ancho del primer rectangulo: "))

rect_x2 = int(input("Ingrese la coordenada x del vertice superior izquierdo del primer rectangulo: "))
rect_y2 = int(input("Ingrese la coordenada y del vertice superior izquierdo del segundo rectangulo: "))
height2 = int(input("Ingrese la altura del segundo rectangulo: "))
width2 = int(input("Ingrese el ancho del segundo rectangulo: "))

p_x1, p_y1 = rect_x1, rect_y1
p_x2, p_y2 = rect_x1 + width1, rect_y1
p_x3, p_y3 = rect_x1, rect_y1 - height1
p_x4, p_y4 = rect_x1 + width1, rect_y1 - height1

count = 0
if inside_rectangle(p_x1, p_y1, rect_x2, rect_y2, height2, width2): count += 1
if inside_rectangle(p_x2, p_y2, rect_x2, rect_y2, height2, width2): count += 1
if inside_rectangle(p_x3, p_y3, rect_x2, rect_y2, height2, width2): count += 1
if inside_rectangle(p_x4, p_y4, rect_x2, rect_y2, height2, width2): count += 1

if count > 0: print(f"{count} vertices del primer rectangulo estan dentro del segundo rectangulo")
else: print("Ningun verticel del primer rectangulo esta dentro del segundo rectangulo")