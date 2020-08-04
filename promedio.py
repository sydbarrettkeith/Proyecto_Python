#ingreso de datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
mate = int(input("Ingrese nota de matemáticas: "))
literatura = int(input("Ingrese nota de literatura; "))
fisica = int(input("Ingrese nota de física: "))

#sacar promedio
prom =(mate + literatura + fisica)/3

#imprimir datos
print ("El alumno "+nombre+" "+apellido+" tiene como promedio:" +str (prom))

#ver aprobación de alumno
if prom > 6:
    print ("El alumno aprobó")
elif prom >=4:
    print ("A recuperatorio")
else:
    print ("Insuficiente")