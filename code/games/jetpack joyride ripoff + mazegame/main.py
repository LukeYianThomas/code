import pygame,random
pygame.init()




#constants
clock = pygame.time.Clock()
delta_time = 0.1
font = pygame.font.Font(None, size=30)
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
scale = 1

#variables
moving = False
running = True
inputList = []
obstacles = []
x = 0
y = 0
cameraX = screen_width/2
cameraY = screen_height/2
offsetx = 0
offsety = 0
xVel = 0
yVel = 0
placeholder = 0
# Loads player image into a thing to put on screen
player_model = pygame.image.load('player.png').convert()
player_model = pygame.transform.scale(player_model,
                                    (player_model.get_width() * scale,
                                     player_model.get_height() * scale))

#colours
black = (0,0,0)
white = (255,255,255)

#fun-ctions [HEEEELP HEEEEEEEEEEEEEEEELLP SOMEONE HEEELP AAAAAAAAAA]
def superCoolInputHandler():
    global inputList,placeholder,running
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                #player
                if event.key == pygame.K_LEFT:
                    inputList.append("LEFT")
                if event.key == pygame.K_RIGHT:
                    inputList.append("RIGHT")
                if event.key == pygame.K_UP:
                    inputList.append("UP")
                if event.key == pygame.K_DOWN:
                    inputList.append("DOWN")
                #camera
                if event.key == pygame.K_a:
                    inputList.append("CAM_LEFT")
                if event.key == pygame.K_d:
                    inputList.append("CAM_RIGHT")
                if event.key == pygame.K_w:
                    inputList.append("CAM_UP")
                if event.key == pygame.K_s:
                    inputList.append("CAM_DOWN")
                if event.key == pygame.K_LSHIFT:
                    inputList.append("SHIFT")
            if event.type == pygame.KEYUP:
                #player
                if event.key == pygame.K_LEFT:
                    inputList.remove("LEFT")
                if event.key == pygame.K_RIGHT:
                    inputList.remove("RIGHT")
                if event.key == pygame.K_UP:
                    inputList.remove("UP")
                if event.key == pygame.K_DOWN:
                    inputList.remove("DOWN")
                #camera
                if event.key == pygame.K_a:
                    inputList.remove("CAM_LEFT")
                if event.key == pygame.K_d:
                    inputList.remove("CAM_RIGHT")
                if event.key == pygame.K_w:
                    inputList.remove("CAM_UP")
                if event.key == pygame.K_s:
                    inputList.remove("CAM_DOWN")
                if event.key == pygame.K_LSHIFT:
                    inputList.remove("SHIFT")
    if len(inputList)>0:print(inputList)

#pygame 0,0 IS TOP LEFT
# X+ LEFT X- RIGHT
# Y- UP Y+ DOWN
def movementController():
    global xVel,yVel,x,y
    collideCheck(x+xVel,y+yVel)
    x+=xVel
    y+=yVel
    if "LEFT" in inputList:
        xVel -= 0.1
    if "RIGHT" in inputList:
        xVel += 0.1
    if "UP" in inputList:
        yVel -= 0.1
    if "DOWN" in inputList:
        yVel += 0.1
    frictionX = 0.03
    frictionY = 0.03
    if xVel > 0: xVel -= frictionX
    if xVel < 0: xVel += frictionX
    if yVel > 0: yVel -= frictionY
    if yVel < 0: yVel += frictionY
    if -0.04 < xVel < 0.04:xVel = 0
    if -0.04 < yVel < 0.04:yVel = 0

def cameraController():
    global cameraX,cameraY
    EXTRA = 1
    if "SHIFT" in inputList: EXTRA = 5
    if "CAM_LEFT" in inputList and (cameraX - 2*EXTRA in range(int(screen_width/2),int(screen_width*1.5))):cameraX -= 2*EXTRA
    if "CAM_RIGHT" in inputList and (cameraX + 2*EXTRA in range(int(screen_width/2),int(screen_width*1.5))):cameraX += 2*EXTRA
    if "CAM_UP" in inputList and (cameraY - 2*EXTRA in range(int(screen_height/2),int(screen_height*1.5))):cameraY -= 2*EXTRA
    if "CAM_DOWN" in inputList and (cameraY + 2*EXTRA in range(int(screen_height/2),int(screen_height*1.5))):cameraY += 2*EXTRA
    
def collideCheck(z,c):
    global playerHitbox,xVel,yVel
    playerHitbox = pygame.Rect(z, c, player_model.get_width(), player_model.get_height())
    for obstacle_rect in obstacles:
        top,bottom,left,right = obstacle_rect[1:5]
        if playerHitbox.clipline(top):
            yVel=yVel*-1
        if playerHitbox.clipline(bottom):
            yVel=yVel*-1
        if playerHitbox.clipline(left):
            xVel=xVel*-1
        if playerHitbox.clipline(right):
            xVel=xVel*-1
    if playerHitbox.clipline((0,screen_height*2+1,screen_width*2,screen_height*2+1)):
            yVel=yVel*-1
    if playerHitbox.clipline((0,-1,screen_width*2,-1)):
            yVel=yVel*-1
    if playerHitbox.clipline((-1,0,-1,screen_height*2)):
            xVel=xVel*-1
    if playerHitbox.clipline((screen_width*2+1,0,screen_width*2+1,screen_height*2)):
            xVel=xVel*-1

#FUCK
def obstacle_generation(amount):
    cornerCut = 2
    size = 25
    for _ in range(amount):
        _x,_y=(random.randint(0,screen_width*2-size),random.randint(0,screen_height*2-size))
        obstacle_rect = _x,_y,size
        top = ((_x+cornerCut,_y),(_x+size-cornerCut-1,_y))
        bottom = ((_x+cornerCut,_y+size-1),(_x+size-cornerCut-1,_y+size-1))
        left = ((_x,_y+cornerCut),(_x,_y+size-cornerCut-1))
        right = ((_x+size-1,_y+cornerCut),(_x+size-1,_y+size-cornerCut-1))
        package = obstacle_rect,top,bottom,left,right
        obstacles.append(package)

def obstacle_render():
    for obstacle_rect in obstacles:
        _x,_y,size = obstacle_rect[0]
        pygame.draw.rect(screen,"orange",pygame.Rect(_x+offsetx,_y+offsety,size,size))

def offsetCalc():
    global offsetx,offsety
    offsetx = (cameraX-320)*-1
    offsety = (cameraY-320)*-1

def minimap():
    scaler = 0.125
    scaler2 = 0.12
    scaler3 = 0.1225
    pygame.draw.rect(screen,"blue",pygame.Rect(478,0,162,162))
    pygame.draw.rect(screen, black,pygame.Rect(479,1,160,160))
    pygame.draw.rect(screen, white,pygame.Rect(479+(cameraX-320)*scaler,1+(cameraY-320)*scaler,80,80))
    pygame.draw.rect(screen, black,pygame.Rect(480+(cameraX-320)*scaler,2+(cameraY-320)*scaler,78,78))
    pygame.draw.rect(screen, white,pygame.Rect(479+x*scaler2,1+y*scaler2,5,5))
    for obstacle_rect in obstacles:
        _x,_y,size = obstacle_rect[0]
        pygame.draw.rect(screen, "orange",pygame.Rect(479+_x*scaler3,1+_y*scaler3,7.5,7.5))
#things to run before game starts
obstacle_generation(250)

#render game
#next tick + collision rebounds
while running:
    screen.fill(black)
    screen.blit(player_model, (x+offsetx, y+offsety))
    offsetCalc()
    obstacle_render()
    minimap()
    superCoolInputHandler()
    movementController()
    cameraController()
    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
# this bit confuses me ^
pygame.quit()