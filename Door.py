from Animation import Animation

class Door:
    def __init__(self):
        self.w = 480.0
        self.h = 400.0
        self.totalFrame = 11
        self.image = Animation("anim/door", self.totalFrame, self.w, self.h)
        
        self.x = width / 2 - 240
        self.y = height - 400
        self.per = 0
        self.openRate = 0
        self.state = ""
        
        self.prevPosition = {"x": 0, "y": 0}
        self.startAnimationFrame = None
        
    def render(self):
        noStroke()
        fill("#333333")
        noTint()
        rect(width / 2 - 66, self.y + 57, 133, 286)
        
        if self.startAnimationFrame is not None: 
            self.per = min((frameCount - self.startAnimationFrame) / 11.0, 1)
            
            if self.per == 1:
                self.startAnimationFrame = None
        
        self.image.draw(self.x, self.y, self.per)
        
    def open(self):
        self.startAnimationFrame = frameCount
        
    def mousePressed(self):
        self.prevPosition["x"] = mouseX 
        self.prevPosition["y"] = mouseY
        
    def mouseDragged(self):
        movementX = mouseX - self.prevPosition["x"]
        self.openRate += movementX / self.w
        self.per = self.openRate
        
        self.prevPosition["x"] = mouseX 
        self.prevPosition["y"] = mouseY
        
        
       
