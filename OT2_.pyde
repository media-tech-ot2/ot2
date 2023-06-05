from Animation import Animation
from Paper import Paper
from ParticleSystem import ParticleSystem
from Migyeong import Migyeong
from Wave import Wave

door = None
per = 0.0 # door open percentage(0.0 ~ 1.0)

isDoorOpen = False
mig = None
paper = None
papers = None



# variables for wave calculating
yspacing = 100
h = 0
theta = 0.0
amplitude = 75.0
period = 1000.0
dy = 0.0
xvalues = None 

waveEvent1 = None
waveEvent2 = None
waveEvent3 = None

def setup():
    frameRate(30)
    global door, mig, paper, h, dy, xvalues , papers, waveEvent1, waveEvent2, waveEvent3
    size(1600, 900)
    background(255)
    door = Animation("anim/door", 11, 480, 400)
    mig = Migyeong(width / 2 -300, height - 300, 300, 300)
    # h = height+16
    # dy = (TWO_PI / period) * yspacing;
    # xvalues = [None] * (h/yspacing)
    paper = Paper()
    # papers = [Paper()] * (h/yspacing) 
    
    waveEvent1 = Wave(x = width / 2, y=height - 200, h=100)
    waveEvent2 = Wave(x = width / 2, y=height - 200, h=100)
    waveEvent3 = Wave(x = width / 2, y=height - 200, h=100)

sF = 0 # frame when the door open event started  
def draw():
    global a, per, paper, isDoorOpen, flag1, start_x, mig
    background(255)
    # calcWave()
    # if per > 0.5:
    #     isDoorOpen = True
    # elif per == 0.0 and not xvalues is None:
    #     popPapers()
    # else:
    #     isDoorOpen = False
    # if a:
    #     if frameCount - sF > 25:
    #         per = 1
    #         a = False
    #     door.play(width / 2 - 240, height - 400, False)
    # else:
    door.draw(width / 2 - 240, height - 400, per)
    # if isPressed:
    #     mig.openDoor(doorOpen)
        
    mig.draw()
    # if per != 0.0:
    #     renderWave()
    
    if per > 0:
        waveEvent1.calc()
        waveEvent1.render(animation=paper)
        
        waveEvent1.h += 16
        waveEvent1.y = height - waveEvent1.h - 100
        waveEvent1.updateWave()
        
        if waveEvent1.currentFrame >= 360:
            if waveEvent1.currentFrame <= 410:
                waveEvent2.x -= 2
                waveEvent3.x += 2
                
            waveEvent2.calc()
            waveEvent2.render(animation=paper)
            
            waveEvent2.h += 16
            waveEvent2.y = height - waveEvent2.h - 100
            waveEvent2.updateWave()
        
            waveEvent3.calc()
            waveEvent3.render(animation=paper)
            
            waveEvent3.h += 16
            waveEvent3.y = height - waveEvent3.h - 100
            waveEvent3.updateWave()
    # waveEvent.update(y=height)
    
start_x = 0
isPressed = False
a = False

def doorOpen():
    global a, sF, per
    a = True
    sF = frameCount
    
def mousePressed():
    global start_x, mig, isPressed
    isPressed = True
    start_x = mouseX

    
    
def mouseDragged(): 
    global door, per, start_x
    if isPressed:
        per += (mouseX - start_x) / 400.0
        per = min(1, max(0, per))
        start_x = mouseX


        
def calcWave():
    global theta, dy, xvalues
    theta += 0.02
    y = theta
    for i in range(len(xvalues)):
        xvalues[i] = sin(y) * amplitude
        y += dy

def renderWave():
    global paper
    noStroke()
    fill(255)
    for i in range(len(xvalues)):
        paper.draw(width/2 + xvalues[i] - 125,height - 200 - 125 - i * yspacing)
        #ellipse(width/2 + xvalues[i],height - 100 - i * yspacing, 16, 16)
systems = []
def popPapers():
    global systems
    if xvalues is not None:
        for i in range(len(xvalues)):
            pass
            #systems.append(ParticleSystem(1, PVector(width/2 + xvalues[i], height - 200 - i * yspacing)))
