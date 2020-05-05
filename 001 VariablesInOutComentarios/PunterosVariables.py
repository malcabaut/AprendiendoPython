#Para ver la direcion de puntero se usa id(variable)
variable=23
print("La variable contiene "+ str (variable) +" y su id es "+ str(id(variable)))
# Si cambiamos la variable
variable=2
print("La variable contiene "+ str (variable) +" y su id es "+ str(id(variable)))
# La direccion cambia ya que python crea un puntero nuevo y supongo que borra la anterior.