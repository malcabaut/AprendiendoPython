def setup():
    size(600, 400)

def draw():
    if  mousePressed:
        fill(0)
    else:
        fill(255)
    ellipse(mouseX, mouseY, 80, 80)
