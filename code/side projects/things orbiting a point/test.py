import pygame
#variables
white = (255,255,255)
black = (0,0,0)
trailsize = 5
timer = 0
trail = []
for i in range(0,trailsize):
    trail.append((400,400))
playerXaccel = 0
playerYaccel = 0
playerX = 400
playerY = 400
decel = 0.02
accel = 0.1
handbreak = 0.5
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
#functions
def playerdraw(x,y):
    global trail
    for i in range(0,len(trail)):
        temp = 255-20*i
        temp = (temp,temp,temp)
        print(x,y)
        pygame.draw.circle(screen,temp,trail[trailsize-(i+1)],4-i/10)
    pygame.draw.circle(screen,white,(x,y),4)
    trail.pop(0)
    package = (x,y)
    trail.append(package)
def playerinputs():
    global playerXaccel,playerYaccel
    inputs = pygame.key.get_pressed()
    if inputs[pygame.K_RIGHT]:
        playerXaccel+=accel
    if inputs[pygame.K_LEFT]:
        playerXaccel-=accel
    if inputs[pygame.K_UP]:
        playerYaccel-=accel
    if inputs[pygame.K_DOWN]:
        playerYaccel+=accel
    if inputs[pygame.K_SPACE]:
        playerXaccel*=0.5
        playerYaccel*=0.5
def playercalc():
    global playerX,playerY,playerXaccel,playerYaccel
    playerX+=playerXaccel
    playerY+=playerYaccel
    if playerXaccel>0:
        playerXaccel-=decel
    elif playerXaccel<0:
        playerXaccel+=decel
    if playerYaccel>0:
        playerYaccel-=decel
    elif playerYaccel<0:
        playerYaccel+=decel
    if playerX>850:
        playerX-=850
    elif playerX<-50:
        playerX+=850
    if playerY>850:
        playerY-=850
    elif playerY<-50:
        playerY+=850

#AAAAAAAAAAAAAAAAAAAAAAAA
def noterender(posx,posy):
    pygame.draw.rect(screen,white,)


def mousemovement():
    global playerX,playerY
    playerX,playerY = pygame.mouse.get_pos()
#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30,30,40))
    playerdraw(playerX,playerY)
    mousemovement()
    #playerinputs()
    #playercalc()
    pygame.display.flip()
    clock.tick(60)
    timer+=1
pygame.quit()
