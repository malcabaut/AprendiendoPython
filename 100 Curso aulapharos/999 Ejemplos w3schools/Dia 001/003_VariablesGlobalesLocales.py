x = "Global"


def UnaFuncion():
    x = "Local"
    print("La variable x:" + x)

def SegundaFuncion():
    global x
    x="Cambio en funcion de variable global"
    print("La variable x:" + x+" en la segunda funcion")

UnaFuncion()
print("La variable x:" + x)
SegundaFuncion()