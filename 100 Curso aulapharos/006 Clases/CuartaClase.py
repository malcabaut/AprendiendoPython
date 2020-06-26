class Soldado:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        """Incluyo el arma como variable propia del objeto y valor inicial vacío"""
        self.arma = ""
        if raza == "Elfo":
            self.vida = 80
            self.velocidad = 10
            self.coste = 200
        elif raza == "Humano":
            self.vida = 100
            self.velocidad = 7
            self.coste = 100
        elif raza == "Enano":
            self.vida = 120
            self.velocidad = 3
            self.coste = 180
    def armar(self, arma): 
        self.arma = arma
        print("Muchas gracias, ahora tengo un",self.arma)
mi_primer_soldado = Soldado("Eldelbar","Elfo") 
mi_primer_soldado.arma = "Arco"
primer_soldado = Soldado("Juan","Humano") 
primer_soldado.armar("Espada") 
segundo_soldado = Soldado("Bran","Humano") 
segundo_soldado.armar("Espada") 
tercer_soldado = Soldado("Glóin","Enano") 
tercer_soldado.armar("Hacha")
