'''
igualad:    a == b
desigualad: a != b
a menor que b:  a < b
a menor o igual b: a <= b
a mayor que b:  a > b
a mayor o igual b: a >= b
'''
# if basico en varias lineas
a = 33
b = 200
if b > a:
  print("b es mayor a")

# if anidado en varias lineas
a = 33
b = 33
if b > a:
  print("b es mayor a")
elif a == b:
  print("a y b son iguales")
  
# if anidado con else final en varias lineas
if b > a:
  print("b es mayor a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor b")

# if y acciones en una sola linea
if b > a: print("b es mayor a") 
elif a == b: print("a y b son iguales")
else: print("a es mayor b")

# if else una linea
print("A") if a > b else print("B")
# 3 condiciones en una linea
print("A") if a > b else print("=") if a == b else print("B")


