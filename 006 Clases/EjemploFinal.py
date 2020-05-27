class Estancia:
    def __init__(self, material_suelo, color_suelo, material_paredes,
color_paredes, material_techo, color_techo):
        self.material_suelo = material_suelo
        self.color_suelo = color_suelo
        self.material_paredes = material_paredes
        self.color_paredes = color_paredes
        self.material_techo = material_techo
        self.color_techo = color_techo

    def propiedades(self):
        print("El material del suelo es", self.material_suelo,
              "y su color", self.color_suelo)
        print("El material de las paredes es", self.material_paredes,
              "y su color", self.color_paredes)
        print("El material del techo es", self.material_techo,
              "y su color", self.color_techo)


# Variable para poder terminar el programa cuando la cambiemos a True
terminamos = False
# Diccionario para guardar las estancias como clave y los objetos como valor
estancias = {}
while terminamos == False:
    respuesta = input(
        "¿Qué quieres hacer?. Puedes elegir 1 para introducir una nueva estancia, 2 para ver una estancia o 3 para terminar: ")
    while respuesta != "1" and respuesta != "2" and respuesta != "3":
        respuesta = input(
            "No has elegido una opción correcta, elige 1, 2 ó 3: ")
    if respuesta == "1":
        nombre_estancia = input("¿Cómo vas a llamar a la estancia?: ")
        material_suelo = input("¿Cuál va a ser el material del suelo?: ")
        color_suelo = input("¿Cuál va a ser el color del suelo?: ")
        material_paredes = input(
            "¿Cuál va a ser el material de las paredes?: ")
        color_paredes = input("¿Cuál va a ser el color de las paredes?: ")
        material_techo = input("¿Cuál va a ser el material del techo?: ")
        color_techo = input("¿Cuál va a ser el color del techo?: ")
        print("")
        # Creamos la clase y la añadimos como valor al diccionario, con clave nombre_estancia
        estancias[nombre_estancia] = Estancia(
            material_suelo, color_suelo, material_paredes, color_paredes, material_techo, color_techo)
    elif respuesta == "2":
        print("Puedes elegir las siguientes estancias:")
        # Creamos una lista para poner en la misma todas las claves del diccionario
        lista_estancias = []
        # Y añadimos todas esas claves, además de imprimirlas numerándolas
for i in estancias.keys():
        lista_estancias.append(i)
        print(lista_estancias.index(i)+1, "-", i)
        numero_estancia = input("¿Qué número de estancia quieres ver?: ")
        # Obligamos a contestar un número
        es_numero = False
        while es_numero == False:
            try:
                numero_estancia = int(numero_estancia)
                es_numero = True
            except:
                numero_estancia = input("No has elegido un número válido. ¿Qué número de estancia quieres ver?: ")
        # Comprobamos si el número es válido o es mayor que la longitud de nuestra lista
        if numero_estancia > len(lista_estancias):
            print("No has elegido un número de estancia adecuado")
        else:
            # Llamamos al método de la clase creada
            estancias[lista_estancias[numero_estancia-1]].propiedades()
        print("")
#else: 
        print("Perfecto, hemos terminado") 
        print("") 
        terminamos = True 

