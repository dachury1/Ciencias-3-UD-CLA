#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LEIDY K
#
# Created:     16/08/2018
# Copyright:   (c) LEIDY K 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import string
class Cola (object):

    def __init__(self):
        self.items=[]

    def encolar (self,dato):
        self.items.append(dato)

    def desencolar (self):
        if self.es_vacia():
             print("La cola esta vacia")
        else:
            return self.items.pop(0)

    def es_vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def mirarElementos(self):
        x=""
        if len(self.items)!=0:
            for i in self.items:
                x+=("-"+i.descripcion())
        return x;

    def buscarPlaca(self, x):
        if len(self.items)!=0:
            for i in self.items:
                if i.getPlaca() == x:
                    return "Registrado: "+i.descripcion()
        return "No se encontro la placa";

    def buscarFicha(self, x):
        if len(self.items)!=0:
            for i in self.items:
                if i.getFicha() == x:
                    return "Registrado: "+i.descripcion()
        return "No se encontro moto con dicha ficha";

    def buscarPropietario(self, x):
        if len(self.items)!=0:
            for i in self.items:
                if i.getPropietario() == x:
                    return "Registrado: "+i.descripcion()
        return "No se encontro moto con dicho propietario";



class Moto:


    def __init__(self, propietario,placa,codigo, ficha):
            self.placa = placa
            self.ficha = ficha
            self.propietario = propietario
            self.cod= codigo

    def descripcion (self):
        return self.placa +" "+ self.ficha +" "+self.cod+" "+ self.propietario

    def getPlaca (self):
        return self.placa+""

    def getFicha (self):
        return self.ficha+""

    def getPropietario (self):
        return self.propietario+""

    def getCodigo (self):
        return self.cod+""

def main ():
   while True:
    usuario = Cola()
    print("1. Registrar")
    print("2. Consulta por Placa")
    print("3. Consulta por Nombre Propietario ")
    print("4. Consulta por Ficha ")
    print("5. Registros ")
    opcion = int(input())
    if opcion == 1:
        placa=raw_input("Placa\n")
        nom=raw_input("Nombre Usuario\n")
        ident=int(input("Carnet\n"))
        ficha= random.randint(0,100)
        motos=Moto(nom,placa,ident,ficha)
        usuario.encolar(motos)
    elif opcion==2:
      placa=raw_input("Placa\n")
      print(usuario.buscarPlaca(placa))
     
    elif opcion==3:
        nom=raw_input("Nombre Usuario\n")
        print(usuario.buscarPropietario(nom))
        
    elif opcion==4:
        ficha=raw_input("Ficha\n")
        print(usuario.buscarFicha(ficha))
        
    elif opcion==5:
        usuario.desencolar()
        print(usuario.mirarElementos())
    else:
        print("Opcion no valida")
        break



main()
