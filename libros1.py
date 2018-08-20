#-*- coding: utf-8 -*-
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

def mala(term):
    salida = {}
    for i in range(0, len(term)-1):
        salida[term[i]] = len(term)-i-1
    return salida

def posicion(mal, sufijo, full_term):
    for offset in range(1, len(full_term)+1)[::-1]:
        marcador = True
        for sufijo_index in range(0, len(sufijo)):
            term_index = offset-len(sufijo)-1+sufijo_index
            if term_index < 0 or sufijo[sufijo_index] == full_term[term_index]:
                pass
            else:
                marcador = False
        term_index = offset-len(sufijo)-1
        if marcador and (term_index <= 0 or full_term[term_index-1] != mal):
            return len(full_term)-offset+1

def CambioSufijo(llave):
    salida = {}
    buffer = ""
    for i in range(0, len(llave)):
        salida[len(buffer)] = posicion(llave[len(llave)-1-i], buffer, llave)
        buffer = llave[len(llave)-1-i] + buffer    
    return salida

def buscar(texto, palabra):
    caracterBueno = CambioSufijo(palabra)
    mal = mala(palabra)
    i = 0
    k = 0
    for i in range(0,2):
        for i in range(k,len(texto)-len(palabra)+1):
        #while i < len(texto)-len(palabra)+1 and k < len(texto):
            j = len(palabra)
            k=k+1
            while j > 0 and palabra[j-1] == texto[i+j-1]:
                j -= 1
            if j > 0:
                caracterMalo = mal.get(texto[i+j-1], len(palabra))
                sufijoCaracterBueno = caracterBueno[len(palabra)-j]
                if caracterMalo > sufijoCaracterBueno:
                    i += caracterMalo
                    
                else:
                    i += sufijoCaracterBueno
            else:
                #print(i)
                print ('Posicion')
                print(z)
                print('info')
                print(a)

class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []


cola = Cola()
#libros = pd.read_csv('libros.csv') 
archivo = open("libros.csv", "r")
lista = [(x.split(";")[0],x.split(";")[1],x.split(";")[2]) for x in archivo.readlines()]
print (lista)
print('seleccione tipo busqueda')
print('---0.titulo---1.clasificacion---2.autor')
busq = int(input())
print('ingrese busqueda')
pal = input()
pal=pal.lower()
for x in lista:
    cola.encolar(x)
z=0
for a in lista:
    z=z+1
    cola.desencolar
    tp = (a[busq])
    tp=tp.lower()
    #print (pal)
    #print(tp)
    buscar(tp,pal)
    #print (lista)