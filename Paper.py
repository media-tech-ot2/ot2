from Animation import Animation

class Paper:
    def __init__(self):
        
        self.frame = 0
        self.w = 250
        self.h = 250
        self.xPos = 0
        self.yPos = 0
        self.index = 0
        self.anim = Animation("anim/paper", 20, self.w, self.h)
    
    def draw(self, xPos, yPos):
        self.anim.play(xPos - self.w / 2, yPos - self.h / 2)
        
    def draw2(self, xPos, yPos, per):
        self.anim.draw(xPos - self.w / 2, yPos - self.h / 2, per)
               
    def moveTo(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
