numero = int(input("Ingrese rango entre 0 y 100: "))
if numero <30:
    print('Alerta: Realizar Riego')
elif numero >= 30 and numero <80:
    print('Alerta: El riego está normal')
else:
    print('Alerta: Hay un exceso de agua')

