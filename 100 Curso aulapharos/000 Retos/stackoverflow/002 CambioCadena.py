'''
https://es.stackoverflow.com/questions/354101/python-remplazar-palabra-del-string-si-despues-de-esa-palabra-viene-un-numero
Tenemos la frase:
Nos vemos en mayo del 2021. Acuerdate del secreto. no te olvides mayo del 2022
y queremos sustituir los del por / siempres que despues del del hay una fecha \d{4} 
'''
import re  # importamos modulo


frase = "Nos vemos en mayo del 2021. Acuerdate del secreto. no te olvides mayo del 2022"
print(frase)
frase = re.sub(r'\s*del\s*(?=\d{4})', "/", frase)
print(frase)

'''
for i in range(len(frase)):
    if ( i < len(frase)
    and frase[i] == 'd'
    and frase[i+1] == 'e'
    and frase[i+2] == 'l' 
    and re.search(r'\d', frase[i+4]) 
    and re.search(r'\d', frase[i+4])
    and re.search(r'\d', frase[i+5])
    and re.search(r'\d', frase[i+6])
    ):
        print(i)
        frase=frase[0:i]+'/'+frase[i+4:]
print(frase)


busqueda = re.search(r' del\s*\d{4}', frase)# realizamos busqueda del patron.
print(busqueda) # imprimo string de la busqueda
print(busqueda.span()) # indice donde empieza el patron
# Juntamos
frase=busqueda.string[0:busqueda.span()[0]]+'/'+busqueda.string[busqueda.span()[0]+5:]
print (frase)
'''
