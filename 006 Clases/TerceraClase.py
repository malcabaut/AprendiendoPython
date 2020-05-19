class Soldado:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
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


# Creamos el primer objeto soldado
primer_soldado = Soldado("Eldelbar", "Elfo")
# Imprimimos el nombre y raza de nuestro soldado
print("Nombre:" + primer_soldado.nombre)
print("Raza:" + primer_soldado.raza)
print("Vida:" + str (primer_soldado.vida))
print("Velocidad:" + str (primer_soldado.velocidad))
print("Coste de entrenamiento:" + str (primer_soldado.coste))

# Veamos de qué tipo es la variable primer_soldado
print(type(primer_soldado))

primer_soldado.nombre="Legolas"

print("Nombre:" + primer_soldado.nombre)
