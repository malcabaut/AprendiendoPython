#Declaro todas las variables simultáneamente 
posicion,movimiento,primera_vez,arriba,abajo = [20,200],[3,2],0,0,0 
def setup(): 
    size(600,400) 
def draw(): 
    background(227,220,7) 
    global posicion, movimiento, posicionY, primera_vez, arriba, abajo 
    diametro = 30 
    fill(14,82,175) 
    ellipse(posicion[0],posicion[1],diametro,diametro) 
    dimensionX = 15 
    dimensionY = dimensionX*6 
    if primera_vez == 0: 
        posicionY = height/2 - dimensionY/2 
        primera_vez = 1 
    rect (20, posicionY, dimensionX, dimensionY) 
    posicion[0] = posicion[0] + movimiento[0] 
    posicion[1] = posicion[1] + movimiento[1] 
    if posicion[0] > width - diametro/2 or posicion[0] < diametro/2: 
        movimiento[0] = -movimiento[0] 
    if posicion[1] > height - diametro/2 or posicion[1] < diametro/2: 
        movimiento[1] = -movimiento[1]  
    #movemos la raqueta si hay que hacerlo 
    if arriba == 1 and posicionY > 0: 
        posicionY = posicionY - 3 
    elif abajo == 1 and posicionY < height - dimensionY: 
        posicionY = posicionY + 3 
#funcion que activa el movimiento al presionar tecla UP y DOWN 
def keyPressed(): 
    global arriba, abajo 
    if keyCode == UP: 
        arriba = 1 
    elif keyCode == DOWN: 
        abajo = 1 
#funcion que detiene el movimiento al soltar tecla UP y DOWN 
def keyReleased(): 
    global arriba, abajo 
    if keyCode == UP: 
        arriba = 0 
    elif keyCode == DOWN: 
        abajo = 0 
