posicionX = 20 
posicionY = 200 
movimiento = 3 
def setup(): 
    background(255) 
    size(600,400) 
def draw(): 
    background(255) 
    global posicionX 
    global movimiento 
    diametro1 = 40 
    diametro2 = 90 
    fill(0,200,200) 
    ellipse(posicionX,posicionY,diametro1,diametro2) 
    posicionX = posicionX + movimiento 
    if posicionX > width-diametro1/2 or posicionX < diametro1/2: 
        movimiento = -movimiento
