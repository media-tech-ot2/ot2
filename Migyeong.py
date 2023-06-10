from Animation import Animation

class Migyeong:
    def __init__(self, **kwargs):
        self.xPos = width / 2 - 300
        self.yPos = height - 300
        self.w = 300
        self.h = 300
        self.anim = Animation("anim/mig", 6, self.w, self.h)
        
        self.startAnimationFrame = None
    
    def render(self):
        per = 0
        
        if self.startAnimationFrame is not None: 
            per = min((frameCount - self.startAnimationFrame) / 9.0, 1)
                        
            if per == 1:
                per = 2.0 - min((frameCount - self.startAnimationFrame) / 9.0, 2)     
        
        self.anim.draw(self.xPos + per * 10, self.yPos - per * 40, per)
        
    def open(self):
        self.startAnimationFrame = frameCount
