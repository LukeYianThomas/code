import pygame

#variables
keyDown = []
def playerinputs():
    global keyDown
    keyDown = [1,2,3,4]
    inputs = pygame.key.get_pressed()
    if inputs[pygame.K_e]:
        keyDown.remove(1)
    if inputs[pygame.K_f]:
        keyDown.remove(2)
    if inputs[pygame.K_j]:
        keyDown.remove(3)
    if inputs[pygame.K_i]:
        keyDown.remove(4)
def a(list):
    temp = []
    if 1 not in list:
        temp.append("E")
    if 2 not in list:
        temp.append("F")
    if 3 not in list:
        temp.append("J")
    if 4 not in list:
        temp.append("I")
    print(temp)
    temp.clear()


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    playerinputs()
    a(keyDown)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
