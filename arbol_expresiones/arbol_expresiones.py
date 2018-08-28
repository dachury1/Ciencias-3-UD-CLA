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

dictionary = {}

def saveDict(let):
    if let in dictionary:
        return dictionary.get(let)
    else:
        dictionary[let]=null

def updateDict(let, val):
    dictionary[let] = val


def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == "=":
        return updateDict(arbol.der, evaluar(arbol.izq))
    if isinstance(arbol.valor, str) == True:
        return saveDict(arbol.valor)
    return int(arbol.valor)

archivo = open("expresiones.in","r")

exp = archivo.readlines()

pila = Pila()

for i in range(0, len(exp)):
    pp = exp[i]
    str1 = ''.join(pp.strip('\n'))
    exp2 = str1.split(" ")
    print 'a'
    print exp2
    convertir(exp2, pila)


archivo.close()

archivo = open("expresiones.out","w")

while pila.es_vacia() != True:
    respuesta = evaluar(pila.desapilar())
    str(respuesta)
    archivo.write(str(respuesta))
    print respuesta
archivo.close()
