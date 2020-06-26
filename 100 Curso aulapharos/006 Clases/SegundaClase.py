class Soldado: 
   def __init__(self, nombre, raza): 
        self.nombre = nombre 
        self.raza = raza 
        print("He sido creado para servirle, a sus órdenes, soy un", self.raza, "y me llamo", self.nombre) 
#Creamos el primer objeto soldado 
primer_soldado = Soldado("Eldelbar","Elfo")