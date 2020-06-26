class Soldado: 
    def __init__(self,nombre,raza,sueldo): 
        self.nombre = nombre 
        self.raza = raza 
        self.__sueldo = sueldo # las __ hace que la variable sea como privada en java
    def arma(self, arma): 
        self.arma = arma 
        print("Muchas gracias, ahora tengo un/una",self.arma)

mi_soldado = Soldado("Eldelbar", "Elfo",10000)
mi_soldado.arma("Arco")
print (mi_soldado.nombre)
print (mi_soldado.raza)
print (mi_soldado.__sueldo)
print (mi_soldado.sueldo)
# Podriamos imprimirlo con este truco:
print(mi_soldado._Soldado__sueldo)