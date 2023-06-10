from Animation import Animation
from Paper import Paper
from Migyeong import Migyeong
from Wave import Wave
from Door import Door
from BackgroundEffect import BackgroundEffect

door = None
per = 0.0

mig = None
paper = None

# variables for wave calculating
waveEvent1 = None
waveEvent2 = None
waveEvent3 = None

backgroundEffect = None

def setup():
    size(1600, 900)
    background(255)
    frameRate(30)
    
    global door, mig, waveEvent1, waveEvent2, waveEvent3, paper, backgroundEffect
    mig = Migyeong()
    paper = Paper() 
    door = Door()
    
    waveEvent1 = Wave(x = width / 2, y=height - 200, h=100)
    waveEvent2 = Wave(x = width / 2, y=height - 200, h=100)
    waveEvent3 = Wave(x = width / 2, y=height - 200, h=100)
    
    backgroundEffect = BackgroundEffect()

sF = 0  
def draw():
    background(255)
    backgroundEffect.render()
    
    global per, paper, mig, sF
    door.render()
    mig.render()
    
    if door.per > 0:
        waveEvent1.calc()
        waveEvent1.render(animation=paper, randomVisible=per)
        
        waveEvent1.h += 16
        waveEvent1.y = height - waveEvent1.h - 100
        waveEvent1.updateWave()
        
        if waveEvent1.currentFrame >= 360:
            waveEvent2.currentFrame = waveEvent1.currentFrame - 1
            waveEvent3.currentFrame = waveEvent1.currentFrame + 1
            if waveEvent1.currentFrame <= 410:
                waveEvent2.x -= 2
                waveEvent3.x += 2
                
            waveEvent2.calc()
            waveEvent2.render(animation=paper, randomVisible=per)
            
            waveEvent2.h += 16
            waveEvent2.y = height - waveEvent2.h - 100
            waveEvent2.updateWave()
        
            waveEvent3.calc()
            waveEvent3.render(animation=paper, randomVisible=per)
            
            waveEvent3.h += 16
            waveEvent3.y = height - waveEvent3.h - 100
            waveEvent3.updateWave()
            
def keyPressed():
    if keyCode == 32:
        if backgroundEffect.type == 'inActive':
            backgroundEffect.active()
            mig.open()
            door.open()
    
def mousePressed():
    door.mousePressed()

def mouseDragged():
    door.mouseDragged()
