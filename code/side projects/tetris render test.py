#[print(x) for x in thislist]
#newlist = [x for x in fruits if "a" in x]
#newlist = [x for x in fruits if x != "apple"]
import pygame_textinput
import pygame
import random
grid = []
secondGrid = []
emptyGrid = []
#testlist = ["    ","[ ]"]
for i in range(200):emptyGrid.append("    ")
#for i in range(200):grid.append(random.choice(testlist))
for i in range(200):grid.append("   ."),secondGrid.append("    ")
for i in range(20):print(" ".join(str(x) for x in grid[i*10:(i*10)+10]))

def renderGame():
    for i in range(20):
        message = " ".join(str(x) for x in grid[i*10:(i*10)+10])
        message = gameFont.render(message,False, (0,255,0))
        screen.blit(message,(0,i*20))
    for i in range(20):
        message = " ".join(str(x) for x in secondGrid[i*10:(i*10)+10])
        message = gameFont.render(message,False, (0,255,255))
        screen.blit(message,(0,i*20))
def spawner():
    secondGrid[1] = "[ ]"
    secondGrid[3] = "[ ]"
def pieceUpdate():
    global secondGrid,thirdGrid
    thirdGrid = emptyGrid
    for i in range(190):
        if secondGrid[i] == "[ ]":
            secondGrid[i] = "    "
            thirdGrid[i+10] = "[ ]"
    secondGrid = list(thirdGrid)
spawner()


pygame.init()
textinput = pygame_textinput.TextInputVisualizer()
screen = pygame.display.set_mode((200,420))
clock = pygame.time.Clock()
gameFont = pygame.font.SysFont("IMPACT", 20)
while True:
    screen.fill((0,0,0))
    events = pygame.event.get()
    textinput.update(events)
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:# and event.key == pygame.K_RETURN
            if 0<len(textinput.value)>1 or len(textinput.value) == 1 :print(textinput.value[0])
            textinput = pygame_textinput.TextInputVisualizer()
    renderGame()
    pieceUpdate()
    pygame.display.update()
    clock.tick(30)