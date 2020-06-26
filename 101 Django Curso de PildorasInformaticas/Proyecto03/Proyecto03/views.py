from django.http import HttpResponse
from django.template import Template, Context
import datetime

class Persona(object):
    def __init__(self,nombre, apellido1, apellido2):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2

def saludo(resquest):  # primera vista
    #nombre="Miguel"
    p1=Persona("Miguel","Alcaide","Bautista")
    fechaActual=datetime.datetime.now()
    temas = ["Plantillas","Modelos","Formularios","Vistas","despliegle"]

    docExterno=open("C:/Users/usuario/Documents/AprendiendoPython/101 Django/Proyecto03/Proyecto03/plantillas/miplantilla.html")
    ptl=Template(docExterno.read())
    docExterno.close()
    ctx =Context({"nombre_persona":p1.nombre, "apellido1_persona":"Alcaide","p1":p1, "fecha":fechaActual, "temas":temas})
    documento=ptl.render(ctx)
    return HttpResponse(documento)