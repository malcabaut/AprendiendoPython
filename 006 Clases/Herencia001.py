class Soldado: 
   def __init__(self,nombre,raza): 
      self.nombre = nombre 
      self.raza = raza 
   def arma(self, arma): 
      self.arma = arma 
      print("Muchas gracias, ahora tengo un/una",self.arma) 
class Mando(Soldado): 
    pass # esnecesario indicar que no tendra contenido con pass

primer_soldado = Mando("Eldelbar", "Elfo")
primer_soldado.arma("Arco")
