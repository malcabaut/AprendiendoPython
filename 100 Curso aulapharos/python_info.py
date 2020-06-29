import sys
import pkg_resources

#Nos muestra 
print ("Mi version de Python es:  %s" % (sys.version))
print ("Modulos de Python: ")
dists = [d for d in pkg_resources.working_set]

for i in dists:
    print (i)