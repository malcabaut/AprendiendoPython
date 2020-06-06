# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 
import requests


respuesta = requests.get("https://educacionadistancia.juntadeandalucia.es/cursos/grade/report/user/index.php?id=767")

datos = respuesta.text

sopa = BeautifulSoup(datos, "html.parser")
resultados = sopa.find_all('a')

for enlace in resultados: print(enlace.get("href"))
