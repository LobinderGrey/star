import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("STAR")

shipleft    = [pygame.image.load("tile\\player_ship\\left.png")]
shipright   = [pygame.image.load("tile\\player_ship\\right.png")]
shipup      = [pygame.image.load("tile\\player_ship\\uper.png")]
shipdown    = [pygame.image.load("tile\\player_ship\\down.png")]

x = 50
y = x
width   = 36
height  = 36
vel     = 5
left    = False
right   = False
up      = True
down    = False
moveCount = 0

def redrawGameWindow():
    global moveCount
    win.fill((0))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    if left:
        win.blit(shipleft[moveCount], (x,y))
    if right:
        win.blit(shipright[moveCount], (x,y))
    if up:
        win.blit(shipup[moveCount], (x,y))
    if down:
        win.blit(shipdown[moveCount], (x,y))

    pygame.display.update()



run     = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        left = True
        right = False
        up = False
        down = False

    if keys[pygame.K_RIGHT]:
        x += vel
        right = True
        left = False
        up = False
        down = False

    if keys[pygame.K_UP]:
        y -= vel
        right = False
        left = False
        up = True
        down = False

    if keys[pygame.K_DOWN]:
        y += vel
        right = False
        left = False
        up = False
        down = True

    
    redrawGameWindow()

pygame.quit()
