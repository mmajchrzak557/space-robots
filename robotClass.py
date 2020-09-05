class Robot(object):
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.speed = 20
        self.width = 224
        self.height = 228
        self.jumpHeight = 10
        self.left = False
        self.right = True
        self.run = False
        self.jump = False
        self.shoot = False
        self.longAnimationFrames = 0
        self.shortAnimationFrames = 0

    def show(self,window):

        global roboRunRight, roboRunLeft, roboIdleRight, roboIdleLeft, roboJumpRight, roboJumpLeft
        
        if self.longAnimationFrames >= 20:
            self.longAnimationFrames = 0
        if self.shortAnimationFrames >= 16:
            self.shortAnimationFrames = 0

        if self.run:
            if self.left:
                window.blit(roboRunLeft[self.shortAnimationFrames//2], (self.x, self.y))
            elif self.right:
                window.blit(roboRunRight[self.shortAnimationFrames//2], (self.x, self.y))
            self.shortAnimationFrames += 1                
        if self.jump:
            if self.left:
                window.blit(robotJumpLeft[self.longAnimationFrames//2], (self.x, self.y))
            elif self.right:
                window.blit(robotJumpRight[self.longAnimationFrames//2], (self.x, self.y))
            self.longAnimationFrames += 1
        if not(self.run) and  not(self.jump):
            if self.left:
                window.blit(robotIdleLeft[self.longAnimationFrames//2], (self.x, self.y))
            elif self.right:
                window.blit(robotIdleRight[self.longAnimationFrames//2], (self.x, self.y))
            self.longAnimationFrames += 1

        
        
