from bs4 import BeautifulSoup
import requests
palabra_clave = input("\nIntroduce la palabra clave:\n")
respuesta = requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q=" +
palabra_clave + "&s=all")
datos = respuesta.text
soup = BeautifulSoup(datos, "html.parser")
resultados = soup.find_all('td', class_="result_text")
for resultado in resultados:
    print(resultado.get_text())
