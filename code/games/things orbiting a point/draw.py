import pygame,random
pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
orbs = []
accel = 0
center = [500,500]
toggled = False
toggle2 = False
def rain():
    global orbs,accel,toggle2
    if len(orbs) > 0:
        for i in range(len(orbs)):
            x,y,xa,ya,colour,size = orbs[i]
            if toggle2 == True:
                xa = upOrDown(x,xa)
                ya = leftOrRight(y,ya)
                x += xa
                y += ya
                accel = 0.01#(len(orbs)/100000)
            else:
                accel = 0
            #pygame.draw.rect(screen,colour,pygame.Rect(x, y, size, size))
            pygame.draw.circle(screen,colour,(x,y),size)
            package = x,y,xa,ya,colour,size
            orbs[i] = package
def upOrDown(x,xa):
    if x > center[0]:xa-= accel#+(random.randint(0,100)/10000)
    elif x < center[0]:xa+= accel#+(random.randint(0,100)/10000)
    return xa
def leftOrRight(y,ya):
    if y > center[1]:ya-= accel#+(random.randint(0,100)/10000)
    elif y < center[1]:ya+= accel#+(random.randint(0,100)/10000)
    return ya

def centerpoint():
    pygame.draw.circle(screen,"black",(center[0],center[1]),8,4)

def toggle():
    global toggled
    if toggled == True:
        toggled = False
    else:
        toggled = True
def togglespawn():
    global orbs,toggled
    if toggled == True:
        x,y = pygame.mouse.get_pos()
        u,i = (random.randint(0,1000),random.randint(0,1000))
        colour = random.randint(0,255)
        colour2 = random.randint(0,255)
        colour3 = random.randint(0,255)
        size = random.randint(2,8)
        if u > center[0] and i > center[1]:colour = (255,255,0)
        elif u > center[0] and i < center[1]:colour = (0,255,255)
        elif u < center[0] and i > center[1]:colour = (0,0,235)
        elif u < center[0] and i < center[1]:colour = (255,0,0)
        package = u,i,0,0,colour,10
        orbs.append(package)
def spawn(x,y):
    global orbs
    colour = random.randint(0,255)
    colour2 = random.randint(50,150)
    colour3 = random.randint(0,255)
    size = random.randint(2,8)
    colour = (colour2,colour2,colour2)
    package = x,y,0,0,(colour),4
    orbs.append(package)
screen.fill("white")
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            a,b = pygame.mouse.get_pos()
            m1,m2,m3 = pygame.mouse.get_pressed()
            if m1 == True:spawn(a,b)
            if m2 == True:toggle()
            if m3 == True:
                if toggle2 == True:
                    toggle2 = False
                else:
                    toggle2 = True
    #screen.fill("white")
    #centerpoint()
    rain()
    print(len(orbs))
    #print(accel)
    togglespawn()
    pygame.display.update()
    clock.tick(600000)