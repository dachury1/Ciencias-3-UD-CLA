#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Estudiantes
#
# Created:     28/08/2018
# Copyright:   (c) Estudiantes 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)


def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

pila = Pila()
archivo = open("expresiones.in","r")
linea  = archivo.read()
archivo = open("expresiones.out","w")
for i in lineas.splitlines():
    convertir(i.split(" "),pila)
    resultado = evaluar(pila.desapilar())
    archivo.write(str(resultado)+"\n")
archivo.close()
archivo.close()