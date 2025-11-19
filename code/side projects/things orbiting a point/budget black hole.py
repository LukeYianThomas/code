import pygame,random
pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
orbs = []
accel = 0.001
center = [500,500]
toggled = False
def rain():
    global orbs
    if len(orbs) > 0:
        for i in range(len(orbs)):
            x,y,colour,size = orbs[i]
            x -= (x-center[0])/center[0]
            y -= (y-center[1])/center[1]
            pygame.draw.circle(screen,colour,(x,y),size+accel*10)
            package = x,y,colour,size
            orbs[i] = package

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
        u,i = (random.randint(-500,1500),random.randint(-500,1500))
        colour = random.randint(150,255)
        colour2 = random.randint(150,255)
        colour3 = random.randint(0,255)
        size = random.randint(1,4)
        colour = (colour3,colour3,colour3)
        package = u,i,colour,size
        orbs.append(package)
def spawn(x,y):
    global orbs
    colour = random.randint(150,255)
    colour2 = random.randint(50,150)
    colour3 = random.randint(0,255)
    size = random.randint(2,8)
    colour = (0,colour,colour)
    package = x,y,(colour),size
    orbs.append(package)
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
                center.clear()
                center.append(a)
                center.append(b)
                print(center)
    screen.fill("black")
    center.clear()
    center.append(random.randint(100,1700))
    center.append(random.randint(100,1700))
    centerpoint()
    print(center)
    rain()
    togglespawn()
    pygame.display.update()
    clock.tick(60000)