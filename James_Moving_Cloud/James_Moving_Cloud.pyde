x = 0
def setup():
    size(640,480)
def draw():
    global x
    if x >= 680:
        x = 0
    x += 1
    background(135,206,255)
    print(x)
    noStroke();
    ellipse(x,width/2,80,80)
    ellipse(x + 50,width/2, 80,80)
    ellipse(x + 100,width/2, 80,80)
    ellipse(x + 25, width/2.4,80,80)
    ellipse(x + 75, width/2.4,80,80)
