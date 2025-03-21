"""
En un estacionamiento la primera hora (o fracción) cuesta Bs. 100 y cada
hora adicional (o fracción) Bs. 80. Haga un algoritmo que reciba como
entrada la hora de entrada y hora de salida de un vehículo y calcule el
monto a pagar.
"""

entry_time = int(input("Ingrese la hora de entrada (00 - 23): "))
exit_time = int(input("Ingrese la hora de salida (00 - 23): "))

if entry_time > exit_time: print("La hora de entrada no puede ser mayor que la de salida")
else:
  total_hours = exit_time - entry_time
  if total_hours <= 1:
    amount = 100
  else:
    amount = 100 + (total_hours - 1) * 80
  print(f"La cantidad a pagar es {amount} Bs.")