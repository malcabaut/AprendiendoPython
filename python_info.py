# Creo este script para ver la version de Python y los modulos
import sys
import pkg_resources

#Nos muestra 
print ("Mi version de Python es:  %s" % (sys.version))
print ("Modulos de Python: ")
dists = [d for d in pkg_resources.working_set]

for i in dists:
    print (i)
'''
luego instalo virtualenv (pip install virtualenv) para trabajar con distinta versionesde django 
ya que los curso que estoy realizado esta en distintas versiones. 
'''