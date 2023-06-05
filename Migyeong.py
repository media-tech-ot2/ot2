from Animation import Animation

class Migyeong:
    global door
    def __init__(self, xPos, yPos, w, h):
        self.xPos = xPos
        self.yPos = yPos
        self.w = w
        self.h = h
        self.anim = Animation("anim/mig", 6, self.w, self.h)
        self.frame = 0
        self.frame2 = 0
        self.index = 0
        self.reverse = False
    def openDoor(self, function):
        if self.index == 1:
            self.reverse = True
            function()
        if self.reverse:
            self.frame -= 1
        else:
            self.frame += 1
            
        self.index = max(0, min(1, self.frame // 1 / 9.0))
        # print(index, self.frame, self.frame // 4 / 6.0)
        self.anim.draw(self.xPos, self.yPos, self.index)
    def draw(self):
        self.anim.draw(self.xPos, self.yPos, self.index)
