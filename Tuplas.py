#listas
autos = ['Ford', 'Chevrolet', 'Fiat']
print(autos)
print(autos[2])
print(autos[-1])
print(autos[0:2])
autos.append('Dodge')
print(autos)
autos.insert(1, 'Ferrari')
print(autos)
#elisminar el elemento 2 Chevrolet
del autos[2]
print(autos)
#saber el largo
print(len(autos))
#modificar elemento
autos[2]='Porsche'
print(autos)
#ver si existe ese porsche
if autos[2] == 'Porsche':
    print('Todo bien')
else:
    print('Todo mal')

#Tuplas

colores = ('Amarillo', 'Azúl', 'Verde')
print(colores)
#esto no se puede hacer, agregar aun color a la tupla
# colores[1] = 'rojo 


#Esto si, verificar si está amarillo en colores
if 'Amarillo' in colores:
    print('El amarillo existe')

#Diccionarios
usuario = {'id':1, 'name':'Pedro','age':37, 'casado':True}
print(usuario['name'])
print(usuario['casado'])

usuario['name'] = 'Nancy Tupla'
print (usuario)
#Tambien se puede modifica, pero como no existe lo va a ingresar
usuario['Apellido'] = 'Algo'
print(usuario)
#print(usuario) 
#lo borramos
del usuario['Apellido']
print(usuario)
#Traerse todas las keys
print(usuario.keys())
#ahora los valores
print(usuario.values())

#para analizar si la lista, tupla o diccionario tiene id
if('id' in usuario):
    print('tiene Id')

#borrar todo el diccionario
usuario.clear()
print(usuario)

#borrar todo
del usuario
print(usuario)