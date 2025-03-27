"""
Escriba un algoritmo que tome como entrada una secuencia de pares
de nombres de ciudades y distancias entre estas ciudades (medidas en
millas) y reporte las distancias en kilómetros. Debe hacer una función
para convertir de millas a kilómetros (1 milla = 1,6 km), otra función
para leer las siguientes dos ciudades y su distancia, y una función para
determinar si el algoritmo debe seguir ejecutándose. Para ello tome
en cuenta que el fin de la entrada está determinado por dos ciudades
con el mismo nombre y distancia 0. Por ejemplo, para la secuencia
Caracas Valencia 98 Caracas Maturin 312 Caracas Caracas 0, su algoritmo
debe imprimir:
Caracas Valencia: 156,8
Caracas Maturin: 499,2
"""

def read_entry():
  city_1, city_2, distance = input("Ingrese la ciudad origen, ciudad "
  "destino y la distancia en millas separadas por un espacio: ").split()
  return city_1, city_2, float(distance)

def miles_to_km(miles):
  return miles * 1.6

def is_final(city_1, city_2, distance):
  return city_1 == city_2 and distance == 0

while True:
  city_1, city_2, distance = read_entry()
  if is_final(city_1, city_2, distance): break
  print(f"{city_1} {city_2} {miles_to_km(distance):.1f}")