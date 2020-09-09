import pygame
import sys
import animation as an
import math 

# LALALALALALAALALALA
class Robot(object):
    def __init__(self, x, y, controlKeys):
        global scaleX, scaleY        
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x + scaleX * 0.25, self.y + scaleY * 0.1, scaleX * 0.5, scaleY * 0.85)
        self.xOffset = self.hitbox.x - self.x
        self.yOffset = self.hitbox.y - self.y
        self.xSpeed = 15
        self.ySpeed = 0
        self.jumpHeight = 26
        self.left = False
        self.right = True
        self.run = False
        self.jump = False
        self.doubleJump = False
        self.shoot = False
        self.frameCount = {'shoot':0, 'jumpShoot':0, 'run':0, 'runShoot':0, '10frAnimation':0, 'dead':0}
        self.keys = controlKeys
        self.prevX = self.hitbox.x
        self.prevY = self.hitbox.y
        self.life = 5
        self.dead = False
        self.platform = None
        self.drop = False
        self.heartOffset = 0

    def update(self, wHeight, g, keys, events):

        if self.life <= 0:
            self.dead = True
            
        self.prevX = self.hitbox.x
        self.prevY = self.hitbox.y
        
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == self.keys[1] and not self.dead:
                    self.drop = False
                    if not self.jump and not self.doubleJump:
                        self.jump = True
                        self.ySpeed = - self.jumpHeight                    
                    elif self.jump and not self.doubleJump:
                        self.doubleJump = True
                        self.frameCount['10frAnimation'] = 0
                        if self.ySpeed >=0:
                            self.ySpeed =  -self.jumpHeight
                        else:
                            self.ySpeed -= (self.jumpHeight - 5)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == self.keys[3]:
                    self.drop = True
                else:
                    self.drop = False
                    
        if not self.dead:                   
            if keys[self.keys[0]] and self.hitbox.x > self.xSpeed:
                self.x -= self.xSpeed
                self.run = True
                self.left = True
                self.right = False            
            elif keys[self.keys[2]] and self.hitbox.x < wWidth - self.hitbox.w - self.xSpeed:
                self.x += self.xSpeed
                self.run = True
                self.left = False
                self.right = True            
            else:
                self.run = False
                                   
        self.ySpeed += g
        self.y += self.ySpeed
        self.hitbox.x, self.hitbox.y = self.x + self.xOffset, self.y + self.yOffset
#        if self.hitbox.y >= wHeight:
#             self.y = - self.hitbox.y - self.yOffset
#            self.jump = False
#            self.doubleJump = False
#            self.y = wHeight - self.hitbox.h - self.yOffset
#            self.ySpeed = 0

    def checkPlatformCollision(self, platform):
        collision = self.hitbox.colliderect(platform.hitbox)
        if collision:              
            if self.prevY < self.hitbox.y and self.prevY <= platform.y - self.hitbox.h and not self.drop:
                self.jump = False
                self.doubleJump = False
                self.y = platform.y - self.hitbox.h - self.yOffset
                self.ySpeed = 0
            else:
                self.drop = False
                self.jump = True
            self.hitbox.x, self.hitbox.y = self.x + self.xOffset, self.y + self.yOffset
    
    def reset_frames(self, key, n, fps):
        if self.frameCount[key] >= n * fps:
            self.frameCount[key] = 0
            if key == 'shoot':
                self.shoot = False
            elif key == 'dead':
                self.frameCount[key] = 10*fps - 1
        
            
                   
                
        
    def show(self, window):
        framesPerSprite = 2
        self.reset_frames('shoot', 4, framesPerSprite)
        self.reset_frames('jumpShoot', 5, framesPerSprite)
        self.reset_frames('run', 8, framesPerSprite)
        self.reset_frames('runShoot', 9, framesPerSprite)
        self.reset_frames('10frAnimation', 10, framesPerSprite)
        self.reset_frames('dead', 10, framesPerSprite)
            
        prevFrames = dict(self.frameCount)
            
        if self.right:
            if not self.dead:
                if not self.run and not self.jump and not self.shoot:
                    window.blit(idleR[self.frameCount['10frAnimation']//framesPerSprite], (self.x, self.y))
                    self.frameCount['10frAnimation'] += 1
                elif not self.run and not self.jump and self.shoot:
                    window.blit(shootR[self.frameCount['shoot']//framesPerSprite], (self.x, self.y))
                    self.frameCount['shoot'] += 1
                elif not self.run and self.jump and not self.shoot:
                    window.blit(jumpR[self.frameCount['10frAnimation']//framesPerSprite], (self.x, self.y))
                    self.frameCount['10frAnimation'] += 1
                elif not self.run and self.jump and self.shoot:
                    window.blit(jumpShootR[self.frameCount['jumpShoot']//framesPerSprite], (self.x, self.y))
                    self.frameCount['jumpShoot'] += 1
                elif self.run and not self.jump and not self.shoot:
                    window.blit(runR[self.frameCount['run']//framesPerSprite], (self.x, self.y))
                    self.frameCount['run'] += 1
                elif self.run and not self.jump and self.shoot:
                    window.blit(runShootR[self.frameCount['runShoot']//framesPerSprite], (self.x, self.y))
                    self.frameCount['runShoot'] += 1
                elif self.run and self.jump and not self.shoot:
                    window.blit(jumpR[self.frameCount['10frAnimation']//framesPerSprite], (self.x, self.y))
                    self.frameCount['10frAnimation'] += 1
                elif self.run and self.jump and self.shoot:
                    window.blit(jumpShootR[self.frameCount['jumpShoot']//framesPerSprite], (self.x, self.y))
                    self.frameCount['jumpShoot'] += 1
            else:
                window.blit(deadR[self.frameCount['dead']//framesPerSprite], (self.x, self.y))
                self.frameCount['dead'] +=1
        elif self.left:
            if not self.dead:
                if not self.run and not self.jump and not self.shoot:
                    window.blit(idleL[self.frameCount['10frAnimation']//framesPerSprite], (self.x, self.y))
                    self.frameCount['10frAnimation'] += 1
                elif not self.run and not self.jump and self.shoot:
                    window.blit(shootL[self.frameCount['shoot']//framesPerSprite], (self.x, self.y))
                    self.frameCount['shoot'] += 1
                elif not self.run and self.jump and not self.shoot:
                    window.blit(jumpL[self.frameCount['10frAnimation']//framesPerSprite], (self.x, self.y))
                    self.frameCount['10frAnimation'] += 1
                elif not self.run and self.jump and self.shoot:
                    window.blit(jumpShootL[self.frameCount['jumpShoot']//framesPerSprite], (self.x, self.y))
                    self.frameCount['jumpShoot'] += 1
                elif self.run and not self.jump and not self.shoot:
                    window.blit(runL[self.frameCount['run']//framesPerSprite], (self.x, self.y))
                    self.frameCount['run'] += 1
                elif self.run and not self.jump and self.shoot:
                    window.blit(runShootL[self.frameCount['runShoot']//framesPerSprite], (self.x, self.y))
                    self.frameCount['runShoot'] += 1
                elif self.run and self.jump and not self.shoot:
                    window.blit(jumpL[self.frameCount['10frAnimation']//framesPerSprite], (self.x, self.y))
                    self.frameCount['10frAnimation'] += 1
                elif self.run and self.jump and self.shoot:
                    window.blit(jumpShootL[self.frameCount['jumpShoot']//framesPerSprite], (self.x, self.y))
                    self.frameCount['jumpShoot'] += 1
            else:
                window.blit(deadL[self.frameCount['dead']//framesPerSprite], (self.x, self.y))
                self.frameCount['dead'] +=1
            for key in prevFrames:
                k = str(key)
                if self.frameCount[k] == prevFrames[k]:
                    self.frameCount[k] = 0            

    def showLives(self, window, left):
        w = heart.get_width()
        img = heart
        self.heartOffset += 0.15
        imgSize = abs(int(w*math.sin(self.heartOffset)))+15
        for i in range(self.life):
            if i == self.life - 1:
                img = pygame.transform.scale(img, (imgSize, imgSize))
                if left:
                    window.blit(img, ((i+0.5)*w - imgSize/2+10, 10 + w/2 - imgSize/2))
                else:
                    window.blit(img, (wWidth - (i+0.5)*w - imgSize/2 - 10, 10 + w/2 - imgSize/2))                                                   
            elif left:
                window.blit(img, (i*w + 10, 10))
            else:
                window.blit(img, (wWidth - i*w - w - 10, 10))
                
class Platform(object):
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.w = width
        self.h = 35
        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)

    def show(self, window):
        for i in range(self.w//25):
            window.blit(platformTile, (self.x + i*25, self.y))
            pygame.draw.rect(window, 52, (self.x + i*25, self.y, 25, 35), 1)      
        return
                
class Projectile(object):
    def __init__(self, player):
        if player.right:
            self.x = player.hitbox.x + player.hitbox.w + 5
        else:
            self.x = player.hitbox.x - 20
        self.y = player.hitbox.y + player.hitbox.h * 0.4
        self.speed = 25
        self.right = player.right
        self.frames = 0
        self.hitbox = pygame.Rect(self.x, self.y, 22, 14)

    def show(self, window):
        if self.frames >= 10:
            self.frames = 0
        if self.right:
            window.blit(bulletR[self.frames//2], (self.x, self.y))
        else:
            window.blit(bulletL[self.frames//2], (self.x, self.y))
        self.frames += 1

    def update(self):
        if self.right:
            self.x += self.speed
            self.hitbox = self.hitbox.move(self.speed, 0)
        else:
            self.x -= self.speed
            self.hitbox = self.hitbox.move(-self.speed, 0)

    def hit(self, player):
        return self.hitbox.colliderect(player.hitbox)

class Explosion(object):
    def __init__(self, projectile):
        if not projectile.right:
            self.x = projectile.x - 35
        else:
            self.x = projectile.x + 15
        self.y = projectile.y - 10
        self.frames = 0
        self.hitbox = pygame.Rect(self.x, self.y, 48,48)

    def show(self, window):
        window.blit(boom[self.frames//2], (self.x, self.y))
        self.frames += 1
        

pygame.init()

g = 2.5
showInfo = False
scaleX, scaleY = 126, 127
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
wWidth = pygame.display.Info().current_w
wHeight = pygame.display.Info().current_h
pygame.display.set_caption('Robot Fights')
pygame.key.set_repeat(0,100)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

runR, runL, idleR, idleL, jumpR, jumpL, shootR, shootL, jumpShootR, jumpShootL, runShootR, runShootL, deadR, deadL = an.importRobotSprites(scaleX, scaleY)
bulletR, bulletL = an. importBulletSprites(22, 14)
background = pygame.transform.scale(pygame.image.load('res/back.png'), (wWidth, wHeight)).convert()
platformTile = pygame.transform.scale((pygame.image.load('res/tile.png')), (25, 35)).convert()
sheet = pygame.transform.scale(pygame.image.load('res/Explosion (3).png'), (576, 48)).convert()
size = sheet.get_size()
boom = an.strip_from_sheet(sheet, (0,0), (size[0]/12, size[1]), 12, 1)
heart = pygame.transform.scale(pygame.image.load('res/heart.png'), (30,30)).convert()
heart.set_colorkey(0)

players  = [Robot (wWidth - 340, 0, [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]), Robot (110, 650, [pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s])]
players[0].right, players[0].left = False, True

### HARDCODED PLATFORMS ###
platforms = [Platform(140, 400, 150), Platform(110, 900, 350), Platform(190, 200, 350), Platform(440, 650, 400), Platform(540, 400, 200)]
platforms += [Platform(wWidth - 280, 400, 150), Platform(wWidth - 460, 900, 350), Platform(wWidth - 540, 200, 350)]
    
projectiles = []
explosions = []

while True:
    clock.tick(35)
    window.blit(background, (0, 0))

    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    if keys[pygame.K_r]:
        players  = [Robot (wWidth - 340, 0, [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]),
                    Robot (110, 650, [pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s])]
        players[0].right, players[0].left = False, True
        projectiles = []
                                    
    if keys[pygame.K_p] and not players[0].shoot and not players[0].dead:
        projectiles.append(Projectile(players[0]))
        players[0].shoot = True
        
    if keys[pygame.K_SPACE] and not players[1].shoot and not players[1].dead:
        projectiles.append(Projectile(players[1]))
        players[1].shoot = True
        
    for platform in platforms:
        platform.show(window)
    
    for player in players:
        player.update(wHeight, g, keys, events)
        for platform in platforms:
            player.checkPlatformCollision(platform)
        player.show(window)
        player.showLives(window, players.index(player))
        if showInfo:
            pygame.draw.rect(window, (0,255,0), (player.x, player.y, scaleX, scaleY), 3)
            pygame.draw.rect(window, (0,100,255), (player.hitbox), 3)
               
    for i in range(len(projectiles) - 1, -1, -1):
        deleted = False
        projectiles[i].update()
        projectiles[i].show(window)
        for j in range(len(players)):
            if projectiles[i].hit(players[j]):
                players[j].life -= 1
                explosions.append(Explosion(projectiles[i]))
                projectiles.pop(i)
                deleted = True
                break
        if deleted:
            continue
        if showInfo:
            pygame.draw.rect(window, (255,0,255), projectiles[i].hitbox, 2)            
        if projectiles[i].x <-50 or projectiles[i].x > wWidth + 50:
            projectiles.remove(projectiles[i])

    for i in range(len(explosions) - 1, -1, -1):
        if explosions[i].frames < 24:
            explosions[i].show(window)
        else:
            explosions.remove(explosions[i])

        
    pygame.display.update()
#   print(1000//(pygame.time.get_ticks() - prev))
#   prev = pygame.time.get_ticks()
