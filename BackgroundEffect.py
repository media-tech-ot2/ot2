class BackgroundEffect:
    def __init__(self):
        self.inActiveImage = loadImage("image/background1.jpg")
        self.activeImage = loadImage("image/background2.jpg")
        
        self.type = 'inActive'
        self.startAnimationFrame = None
    
    def render(self):
        if self.startAnimationFrame is not None:
            opacity = min((frameCount - self.startAnimationFrame) * 12, 255)
            if self.type == 'active':
                image(self.inActiveImage, 0, 0)
            else:
                image(self.activeImage, 0, 0)
                
            tint(255, opacity)
        
        if self.type == 'inActive':
            image(self.inActiveImage, 0, 0)
        else:
            image(self.activeImage, 0, 0)
        noTint()
        
    def active(self):
        self.startAnimationFrame = frameCount
        self.type = 'active'
        
    def inActive(self):
        self.startAnimationFrame = frameCount
        self.type = 'inActive'
