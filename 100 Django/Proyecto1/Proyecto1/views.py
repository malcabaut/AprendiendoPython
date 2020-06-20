from django.http import HttpResponse
import datetime

def saludo(resquest):  # primera vista
    documento ="""<!DOCTYPE html>
    <html>
        <body>
            <h1> Una cabezera </h1>
            <p> Hola Mundo. </p>
        </body>
    </html>"""
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