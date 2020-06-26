var1="Variable1 fuera"
var2="Variable2 fuera"

def PruebasVariables():
    var1="Variable1 dentro de def"
    global var2 #agora esta usadno la variable global.
    var2 = "Variable2 dentro de la funcion"
    print ("Hola Mundo, var1: "+str(var1))
    print ("Hola Mundo, Var2: "+str(var2))

PruebasVariables()
print ("Hola Mundo, var1: "+str(var1))
print ("Hola Mundo, Var2: "+str(var2))