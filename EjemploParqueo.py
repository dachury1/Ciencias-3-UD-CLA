#ejercicio de expresiones
from cola import *
from parqueadero import *
from random import randint

def asignar(nombre, doc, placa):
    parqueadero = Parqueadero(nombre, doc, placa)
    cola.encolar(parqueadero)

i=1
a=0
cola = Cola()
while (i != 0):     
    nombre = raw_input("Ingrese su nombre: ")
    doc = raw_input("ingrese su documento: ")
    placa = raw_input("ingrese la placa del vehiculo: ")
    asignar(nombre, doc, placa)
    a=a+1
    i = int(input("¿Desea ingresar otro usuario? 1 Si/0 No:  "))
    if(i==0):
        print "Los siguientes vehiculos salieron del parqueadero"

val = randint(1,a)
b=1
while (b<a):
    parq = cola.desencolar()
    print (parq.nombre)
    print (parq.documento)
    print (parq.placa)
    b=b+1
