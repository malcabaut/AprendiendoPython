# Determinar el tipo de un objeto
x = 200
# Con type() podemos saber el tipo de un objeto
print(type(x))
# con isinstance nos devolvera true o false si el objeto es del tipo que le indiquemos
print("x es un str: "+str(isinstance(x, str)))
print("x es un int: "+str(isinstance(x, int)))