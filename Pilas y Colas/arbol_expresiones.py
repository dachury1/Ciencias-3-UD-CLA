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
<<<<<<< HEAD:arbol_expresiones.py


xp = raw_input("ingrese l expresion en posfija: ").split(" ")

=======
    
>>>>>>> 0935d0c0eeb9976aa98c449dde4ca530fcc4f244:Pilas y Colas/arbol_expresiones.py
pila = Pila()
exp = ""
archivo = open("expresiones.in","r")
exp = archivo.read()
for linea in archivo.readlines():
    convertir(exp.split(" "), pila)
    print evaluar(pila.desapilar())
    archivo2 = open("expresiones.out","w")
    archivo2.write(str(evaluar(pila.desapilar())))
    archivo.close()

