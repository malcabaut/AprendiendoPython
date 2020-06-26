class Soldado: 
   #Definimos el constructor, es decir, la función __init__ 
    def __init__(self, nombre, raza):
        self.nombre=nombre
        self.raza=raza

#Creamos un Elfo llamado Eldelbar 
nombre = "Eldelbar" 
raza = "Elfo" 
primer_soldado = Soldado(nombre, raza)
print(primer_soldado.nombre) 
print(primer_soldado.raza) 