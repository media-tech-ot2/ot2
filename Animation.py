class Animation:
    def __init__(self, imagePrefix, count, w, h):
        self.images = []
        self.imageCount = count
        self.frame = 0
        self.w = w
        self.h = h
        
        for i in range(count):
            # Use f-string to format 'i' into four digits
            #filename = f"{imagePrefix}{str(i).zfill(4)}.gif"
            filename = imagePrefix + nf(i, 2) + ".png"
            print(filename)
            self.images.append(loadImage(filename))
    
    def play(self, xpos, ypos, isInfinite):
        if isInfinite:
            self.frame = (self.frame + 1) % self.imageCount
        else:
            self.frame = min(self.frame + 1, self.imageCount - 1)
            
        image(self.images[self.frame], xpos, ypos, self.w, self.h)
        
    def draw(self, xpos, ypos, per):
        per = min(per, 1)
        val = max(int(round((self.imageCount - 1) * per)), 0)
        image(self.images[val], xpos, ypos, self.w, self.h)
        
    def getWidth(self):
        return self.images[0].width
