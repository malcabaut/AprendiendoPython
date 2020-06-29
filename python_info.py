# Creo este script para ver la version de Python y los modulos
import sys
if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata

#Nos muestra 
print ("Mi version de Python es:  %s" % (sys.version))


dists = importlib_metadata.distributions()
print ("Modulos de Python: ")
for dist in dists:
    name = dist.metadata["Name"]
    version = dist.version
    license = dist.metadata["License"]
    print(f'{name} = {version}')
'''
luego instalo virtualenv (pip install virtualenv) para trabajar con distinta versionesde django 
ya que los curso que estoy realizado esta en distintas versiones. 
'''