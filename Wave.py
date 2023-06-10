import random as r

class Wave:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.currentFrame = 0
        self.ySpacing = self.getParameter("ySpacing", 110)
        
        self.x = self.getParameter("x", width / 2)
        self.y = self.getParameter("y", 0)
        
        self.h = self.getParameter("h", height + 16)
        self.maxWaves = self.getParameter("maxWaves", 4)
        self.theta = self.getParameter("theta", 0.0)
        self.amplitude = [0.0] * self.maxWaves
        self.dy = [0.0] * self.maxWaves
        self.xValues = []
        
        for i in range(self.maxWaves):
            self.amplitude[i] = i
            period = 100 + i
            self.dy[i] = (TWO_PI / period) * self.ySpacing
            
        self.xValues = [0.0] * int(self.h / self.ySpacing)
        
    def update(self, **kwargs):
        # options = ["x", "y", "h"]
        # for optionName in options:
        #     if optionName in kwargs:
        #         self[optionName] = kwargs[optionName]
        
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]
        if "h" in kwargs:
            self.h = kwargs["h"]
            
    
    def updateWave(self):
        startFrame = 60
        durationFrame = 300.0
        per = min((self.currentFrame - startFrame) / durationFrame, 1)
            
        for i in range(self.maxWaves):
            if self.currentFrame < startFrame:
                self.amplitude[i] = i
                period = 100 + i
                self.dy[i] = (TWO_PI / period) * self.ySpacing
            else:
                # self.amplitude[i] = i
                # period = 100 + i
                # self.dy[i] = (TWO_PI / period) * self.ySpacing
                # if i <= self.maxWaves / 2:
                self.amplitude[i] = 30 * per
                period = 100 + 30 * per
                self.dy[i] = (TWO_PI / period) * self.ySpacing
            
        self.xValues = [0.0] * int(self.h / self.ySpacing)
        
    def calc(self):
        self.theta += 0.02
        self.currentFrame += 1
        
        for i in range(len(self.xValues)):
            self.xValues[i] = 0
            
        for j in range(self.maxWaves):
            x = self.theta
            for i in range(len(self.xValues)):
                if j % 2 == 0:
                    self.xValues[i] += sin(x) * self.amplitude[j]
                else:
                    self.xValues[i] += cos(x) * self.amplitude[j]
                x += self.dy[j]

    def render(self, **kwargs):
        noStroke()
        fill(60,50);
        ellipseMode(CENTER)
        
        for i in range(len(self.xValues)):
            x = self.x + self.xValues[i]
            y = self.y + i * self.ySpacing
            #if "randomVisible" in kwargs:
            #    if r.random() >= kwargs["randomVisible"]:
            #        tint(255, 255, 255, int(255 - 255 * (1 - min(kwargs["randomVisible"], 1) * 0.5)))
                
            if "animation" in kwargs:
                kwargs["animation"].draw2(x, y, (i * 3 + self.currentFrame) % 30 / 30.0)
            else:
                ellipse(x, y, 16, 16)
            
            noTint()
        
    def getParameter(self, keyName, defaultValue):
        if keyName in self.kwargs:
            return self.kwargs[keyName]
        
        return defaultValue
