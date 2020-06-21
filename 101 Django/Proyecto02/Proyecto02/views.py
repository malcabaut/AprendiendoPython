from django.http import HttpResponse
from django.template import Template, Context
import datetime

class Persona(object):
    def __init__(self,nombre, apellido1, apellido2):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2

def saludo1(resquest):  # primera vista
    #nombre="Miguel"
    p1=Persona("Miguel","Alcaide","Bautista")
    fechaActual=datetime.datetime.now()

    docExterno=open("C:/Users/usuario/Documents/AprendiendoPython/101 Django/Proyecto02/Proyecto02/plantillas/miplantilla.html")
    ptl=Template(docExterno.read())
    docExterno.close()
    ctx =Context({"nombre_persona":p1.nombre, "apellido1_persona":"Alcaide","p1":p1, "fecha":fechaActual})
    documento=ptl.render(ctx)
    return HttpResponse(documento)

def saludo2(resquest):  # primera vista
    #nombre="Miguel"
    p1=Persona("Miguel","Alcaide","Bautista")
    fechaActual=datetime.datetime.now()
    temas = ["Plantillas","Modelos","Formularios","Vistas","despliegle"]

    docExterno=open("C:/Users/usuario/Documents/AprendiendoPython/101 Django/Proyecto02/Proyecto02/plantillas/miplantilla.html")
    ptl=Template(docExterno.read())
    docExterno.close()
    ctx =Context({"nombre_persona":p1.nombre, "apellido1_persona":"Alcaide","p1":p1, "fecha":fechaActual, "temas":temas})
    documento=ptl.render(ctx)
    return HttpResponse(documento)

def despedida(resquest):

    return HttpResponse("Adios")

def dameFecha(resquest):
    fechaActual=datetime.datetime.now()
    documento ="""<!DOCTYPE html>
    <html>
        <body>
            <h1> Fecha y hora </h1>
            <p> %s </p>
        </body>
    </html>"""%fechaActual
    return HttpResponse(documento)

def calculaEdad(resquest, edad, agno):
  
    perido=agno-2020
    edadFutura=edad+perido
    documento ="""<!DOCTYPE html>
    <html>
        <body>
            <h2> En el año %s tedrás %s años</h2>
        </body>
    </html>"""%(agno,edadFutura)
    return HttpResponse(documento)