#Dado el problema anterior del consecionario de autos debemos modificarlo, teniendo en cuenta:
#1 Ya no sabemos cuántos clientes tendremos
#2 Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
#3 Lo mismo con la cantidad de puertas y los colores
#4 Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
#5 Si la cantidad de clientes fue:
 #5.1: 0 a 5 personas o hay descuento
 #5.2: 6 a 10 personas: hay un descuento de 10%
 #5.3: 11 a 50 personas: hay un descuento del 15%
 #5.4: Más de 50 personas: El descuento es del 18%
#6 Solo se va a mostrar que se vendió al final del programa

def calcular_precio(marca,puertas,color,ventas):
    marcas = {'FORD':100000, 'CHEVROLET':12000,'FIAT': 80000}
    colores = {'Blanco':10000,'Azul':20000,'Negro':30000}
    puertas = {2:50000,4:65000,5:78000}
    precio = marcas[marca]+colores[color]+puertas[puerta]
    if ventas > 5 and ventas < 11:
        precio = precio*0.9
    elif ventas >10 and ventas<51:
        precio = precio*0.85
    elif largo>50:
        precio = precio*0.82
    return precio
    


mas_clientes = 'si'
ventas =[]
marcas = ['FORD','CHEVROLET','FIAT']
puertas = [2,4,5]
colores = ['Blanco','Azul','Negro']
while mas_clientes == 'si': 
    nombre = input('Ingrese nombre: ')
    apellido = input('INgrese Apellido: ')
    marca = ''
    puerta=0
    color = ''
    while marca not in marcas:
        marca = input ('Ingrese marca:  ')
    while puerta not in puertas:
        puerta = int(input('Ingrese cantidad de puertas: '))
    while color not in colores:
        color = input('Ingrese color: ')
#precio =calcular_precio(marca,puerta,color)
    ventas.append({'nombre':nombre,'apellido':apellido,'marca':marca, 'puertas':puerta,'color':color})
    mas_clientes = input('Hay más clientes?: ')
largo = len(ventas)
for i in ventas:
    precio = calcular_precio(marca,puertas,color,largo)
    print("La persona: " + i['nombre']+" "+i['apellido']+
    "compró un auto marca"+i['marca']+" de " +str(i['puertas'])+"puertas y color"+i['color']+" con un precio de $"+str(i['precio']))