posicionX = 20 
posicionY = 200 
def setup(): 
    background(255) 
    size(600,400) 
def draw(): 
    global posicionX
    global posicionY
    fill(0,200,200) 
    ellipse(posicionX,posicionY,40,40) 
    posicionX = posicionX + 1 
