import pygame
import os

def loadSprite(animationName, frameCount, flip, scaleX, scaleY, bullet):
    frames = []
    for i in range(1, frameCount):
        if bullet:
            frameName = '%s/res/%s_00%d.png' % (os.getcwd(), animationName, i - 1)
        else:
            frameName = '%s/res/%s (%d).png' % (os.getcwd(), animationName, i)
        frame = pygame.image.load(frameName)
        frame = pygame.transform.scale(frame, (scaleX, scaleY))
        frame.convert()
        if flip:
            frame = pygame.transform.flip(frame, True, False)
        frames.append(frame)
    return frames
        
def importRobotSprites(scaleX, scaleY):
    runR       = loadSprite('Run', 9, False, scaleX, scaleY, False)
    idleR      = loadSprite('Idle', 11, False, scaleX, scaleY, False)       
    jumpR      = loadSprite('Jump', 11, False, scaleX, scaleY, False)
    shootR     = loadSprite('Shoot', 5, False, scaleX, scaleY, False)
    jumpShootR = loadSprite('JumpShoot', 6, False, scaleX, scaleY, False)
    runShootR  = loadSprite('RunShoot', 10, False, scaleX, scaleY, False)
    deadR      = loadSprite('Dead', 11, False, scaleX, scaleY, False)
     
    return runR, idleR, jumpR, shootR, jumpShootR, runShootR, deadR

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
    
    
