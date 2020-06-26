class Soldado: 
   def __init__(self,nombre,raza): 
      self.nombre = nombre 
      self.raza = raza 
   def arma(self, arma): 
      self.arma = arma 
      print("Muchas gracias, ahora tengo un/una",self.arma) 
class Mando(Soldado): 
   def __init__(self,nombre,raza,rango): 
       Soldado.__init__(self,nombre,raza) 
       self.rango = rango 

primer_mando = Mando("Eldelbar", "Elfo","Sargento")
primer_mando.arma("Arco")