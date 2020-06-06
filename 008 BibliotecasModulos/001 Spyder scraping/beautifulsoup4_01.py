# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 
import requests

pagina = input("Introduce la URL: ")
respuesta = requests.get("http://" + pagina)

datos = respuesta.text

sopa = BeautifulSoup(datos, "html.parser")
resultados = sopa.find_all('a')
