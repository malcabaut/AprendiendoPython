# Las tuplas no son mutables
nombres = ("Ana", "Maria", "Rodrigo")
try:
    nombres.append("Anita")
except:
    print("No se puede nombres.append('Anita')")

try:
    nombres[0]=("Anita")
except:
    print("No se puede nombres[0]=('Anita')")