from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render # agregado en el video 9 pildorasinformaticas
import datetime

class Persona(object):
    def __init__(self,nombre, apellido1, apellido2):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2

def saludo(request):  # primera vista
    #nombre="Miguel"
    p1=Persona("Miguel","Alcaide","Bautista")
    fechaActual=datetime.datetime.now()
    temas = ["Plantillas","Modelos","Formularios","Vistas","despliegle"]

    ctx ={"nombre_persona":p1.nombre, "apellido1_persona":"Alcaide","p1":p1, "fecha":fechaActual, "temas":temas}

    return render(request, "miplantilla.html", ctx)