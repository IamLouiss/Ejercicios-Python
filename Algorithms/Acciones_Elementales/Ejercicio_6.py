"""
Supongamos un reloj analógico (de agujas). Dada lo hora exacta (horas y
minutos), escriba un algoritmo que calcule el ángulo entre ambas agujas.
Por ejemplo, a las 3:00 el ángulo será 90 grados. A las 3:15 el ángulo será
7,5 grados.
"""

hour = int(input("Ingrese una hora (1-12): "))
minutes = int(input("Ingrese los minutos (0-59): "))

# En la aguja de las horas, cada minuto equivale a 0.5 grados y
# en la aguja de los minutos, cada minuto equivale a 6 grados
angle = abs(((hour * 60 + minutes) * 0.5) - (minutes * 6))
if angle > 180: angle = 360 - angle
print(f"El angulo entre las dos agujas es {angle}")