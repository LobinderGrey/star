import pygame, random, sys, time

pygame.init()

win = pygame.display.set_mode((1200,980))

pygame.display.set_caption("STAR")

shipleft    = [pygame.image.load("tile\\player_ship\\left.png")]
shipright   = [pygame.image.load("tile\\player_ship\\right.png")]
shipup      = [pygame.image.load("tile\\player_ship\\uper.png")]
shipdown    = [pygame.image.load("tile\\player_ship\\down.png")]

px = 600
py = 490
width   = 36
height  = 36
vel     = 5
left    = False
right   = False
up      = True
down    = False
moveCount = 0

##########################  SNOW CODE #################################

blue    = (135,206,250)
black   = (0,0,0)
white   = (255,255,255)
yellow  = (255,255,0)
green   = (0,128,0)
red     = (0,255,0)


windowWidth     = 1200 
windowHeight    = 980
spaceWidth      = 1200
spaceWidthMax   = spaceWidth + 50
spaceHeight     = 700  
spaceHeightMax  = spaceHeight + 50
varHeight       = windowHeight
starSize        = 2
starNum         = 200
FPS             = 120
velocityX = 0
velocityY = 0

starcolor = white

stars = []

for q in range(starNum):
    x = random.randrange(0, spaceWidth)
    y = random.randrange(0, spaceHeight)
    stars.append([x,y])

########################## END SNOW CODE ##############################



def redrawGameWindow():
    global moveCount
    win.fill((0))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    if left:
        win.blit(shipleft[moveCount], (px,py))
    if right:
        win.blit(shipright[moveCount], (px,py))
    if up:
        win.blit(shipup[moveCount], (px,py))
    if down:
        win.blit(shipdown[moveCount], (px,py))

    #pygame.display.update()

run     = True
while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        velocityX = 2
        left = True
        right = False
        up = False
        down = False

    if keys[pygame.K_RIGHT]:
        velocityX = -2
        right = True
        left = False
        up = False
        down = False

    if keys[pygame.K_UP]:
        velocityY = 2
        right = False
        left = False
        up = True
        down = False

    if keys[pygame.K_DOWN]:
        velocityY = -2
        right = False
        left = False
        up = False
        down = True

#if mousekeys[pygame.MOUSEBUTTONDOWN]:
 #       mx, my = pygame.mouse.get_pos()
  #      pygame.draw.rect(win, red, [700,700, 10, 100])
   #     pygame.display.flip()
    #    print("hallo")

    #######
    for i in stars:

        i[0] += velocityX
        i[1] += velocityY
        pygame.draw.circle(win, starcolor, i, starSize) 
        if i[1] > spaceHeight:
            i[1] = random.randrange(-50,-5)
            i[0] = random.randrange(spaceWidth)
        if i[1] < -50:
            ########
            i[1] = random.randrange(spaceHeight, spaceHeightMax)
            i[0] = random.randrange(spaceWidth)
        if i[0] > spaceWidth:
            i[1] = random.randrange(spaceHeight)
            i[0] = random.randrange(-50,-5)
        if i[0] < -50:
            #########
            i[1] = random.randrange(spaceHeight)
            i[0] = random.randrange(spaceWidth, spaceWidthMax)


    pygame.display.flip()
    ###########
    
    redrawGameWindow()

pygame.quit()
