import pygame

def loadSprite(animationName, frameCount, flip, scaleX, scaleY, bullet):
    frames = []
    for i in range(1, frameCount):
        if bullet:
            frameName = 'res/%s_00%d.png' % (animationName, i - 1)
        else:
            frameName = 'res/%s (%d).png' % (animationName, i)
        frame = pygame.image.load(frameName)
        frame = pygame.transform.scale(frame, (scaleX, scaleY))
        frame.convert()
        if flip:
            frame = pygame.transform.flip(frame, True, False)
        frames.append(frame)
    return frames
        
def importRobotSprites(scaleX, scaleY):
    runR       = loadSprite('Run', 9, False, scaleX, scaleY, False)
    runL       = loadSprite('Run', 9, True, scaleX, scaleY, False)    
    idleR      = loadSprite('Idle', 11, False, scaleX, scaleY, False)       
    idleL      = loadSprite('Idle', 11, True, scaleX, scaleY, False)    
    jumpR      = loadSprite('Jump', 11, False, scaleX, scaleY, False)
    jumpL      = loadSprite('Jump', 11, True, scaleX, scaleY, False)
    shootR     = loadSprite('Shoot', 5, False, scaleX, scaleY, False)
    shootL     = loadSprite('Shoot', 5, True, scaleX, scaleY, False)
    jumpShootR = loadSprite('JumpShoot', 6, False, scaleX, scaleY, False)
    jumpShootL = loadSprite('JumpShoot', 6, True, scaleX, scaleY, False)
    runShootR  = loadSprite('RunShoot', 10, False, scaleX, scaleY, False)
    runShootL  = loadSprite('RunShoot', 10, True, scaleX, scaleY, False)
    deadR      = loadSprite('Dead', 11, False, scaleX, scaleY, False)
    deadL      = loadSprite('Dead', 11, True, scaleX, scaleY, False)
     
    return runR, runL, idleR, idleL, jumpR, jumpL, shootR, shootL, jumpShootR, jumpShootL, runShootR, runShootL, deadR, deadL

def importBulletSprites(bulletWidth, bulletHeight):
    bulletR = loadSprite('Bullet', 6, False, bulletWidth, bulletHeight, True)
    bulletL = loadSprite('Bullet', 6, True, bulletWidth, bulletHeight, True)

    return bulletR, bulletL

def strip_from_sheet(sheet, start, size, columns, rows=1):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pygame.Rect(location, size)).convert())
    return frames
    
    
