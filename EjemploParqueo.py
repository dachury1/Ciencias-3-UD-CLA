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
        return "No se encontr0 moto con dicho propietario";



class Moto:

    def __init__(self, placa, ficha, propietario):

        self.placa = placa
        self.ficha = ficha
        self.prop = propietario

    def descripcion (self):
        return self.placa +" "+ self.ficha +" "+ self.prop

    def getPlaca (self):
        return self.placa+""

    def getFicha (self):
        return self.ficha+""

    def getPropietario (self):
        return self.prop+""

   # def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    # return ''.join(random.choice(chars) for _ in range(size))


def main ():
    usuario = Cola()
    moto1=Moto("MXWBOG","102Q","LUIS ARANGO")
    moto2=Moto("WXYMED","709RQ","ANA ROMERO")

    usuario.encolar(moto1)
    usuario.encolar(moto2)

    print(usuario.mirarElementos())

    print(usuario.buscarPlaca("MXWBOG"))
    print(usuario.buscarPlaca("XIP89"))

    print(usuario.buscarFicha("102Q"))
    print(usuario.buscarFicha("30P"))

    print(usuario.buscarPropietario("MARIA"))
    print(usuario.buscarPropietario("ANA ROMERO"))

    usuario.desencolar()
    print(usuario.mirarElementos())


    #placa = raw_input("Placa de la moto")
    #propietario = raw_input("Nombre propietario de la moto")
    #ficha= id_generator(6)

main()


