def hormigon(): 
   cantidad = float(input("¿Cuántos metros cúbicos de hormigón quieres?:"))
   cemento = 322*cantidad 
   arena = 689*cantidad 
   grava = 1177*cantidad 
   agua = 156*cantidad 
   print("Necesitas las siguientes cantidades:") 
   print(cemento,"kilogramos de cemento") 
   print(arena,"kilogramos de arena") 
   print(grava,"kilogramos de grava") 
   print(agua,"kilogramos de agua") 
hormigon()