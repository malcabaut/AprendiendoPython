from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(resquest):  # primera vista
    docExterno=open("C:/Users/usuario/Documents/AprendiendoPython/101 Django/Proyecto02/Proyecto02/plantillas/miplantilla.html")
    ptl=Template(docExterno.read())
    docExterno.close()
    ctx =Context()
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