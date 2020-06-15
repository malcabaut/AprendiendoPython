from django.http import HttpResponse

def saludo(resquest): # primera vista

    return HttpResponse("Hola Mundo")

def despedida(resquest):

    return HttpResponse("Adios")