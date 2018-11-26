import pygame, random, sys, time, math

pygame.init()



### player ###



ship = pygame.image.load("tile\\player_ship\\uper.png")

##### helper should be removed ##################
shipleft    = [pygame.image.load("tile\\player_ship\\uper.png")]
shipright   = [pygame.image.load("tile\\player_ship\\uper.png")]
shipup      = [pygame.image.load("tile\\player_ship\\uper.png")]
shipdown    = [pygame.image.load("tile\\player_ship\\uper.png")]

px = 650
py = 350

mousex = 0
mousey = 0

width   = 36
height  = 36
#vel     = 5
speed   = 0
left    = False
right   = False
up      = False
down    = False
moveCount = 0

### player end ###

### menue #####
menuebg     = None
menuespeedbg = [18, 600, 182, 10]
menuespeed  = [20, 600, 180, 8]
### menue end #######

##########################  STAR CODE #################################

blue    = (135,206,250)
black   = (0,0,0)
white   = (255,255,255)
yellow  = (255,255,0)
green   = (0,128,0)
red     = (0,255,0)

windowWidth     = 1000 
windowHeight    = 700
spaceWidth      = windowWidth
spaceWidthMax   = windowWidth + 50
spaceHeight     = windowHeight  
spaceHeightMax  = spaceHeight + 50
starSize        = 2
starNum         = 200
FPS             = 120
velocityX       = float(0)
velocityY       = float(0)

starcolor = white

stars = []

win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("STAR")

for q in range(starNum):
    x = random.randrange(0, spaceWidth)
    y = random.randrange(0, spaceHeight)
    stars.append([x,y])

########################## END STAR CODE ##############################



########################## get angle ########################

def getangle(x1,y1,x2,y2):
    dot = x1*x2 + y1*y2      # dot product
    det = x1*y2 - y1*x2      # determinant
    angle = math.atan2(det, dot) + 360 * (det<0)
    return angle
######################### END get angle ##################################



def redrawGameWindow():
    global moveCount
    win.fill((0))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    if left:
        win.blit(shipleft, (px,py))
    if right:
        win.blit(shipright, (px,py))
    if up:
        win.blit(shipup, (px,py))
    if down:
        win.blit(shipdown, (px,py))


    #pygame.display.update()

run     = True
while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            print(mousex)
            print(mousey)
            blub = getangle(mousex, mousey, px, py)
            shipleft = pygame.transform.rotate(ship, int(round(blub)))
            print(blub)
            pressed = True


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        velocityX = 1 * speed
        shipleft = pygame.transform.rotate(ship, 90)
        left = True
        right = False
        up = False
        down = False

    if keys[pygame.K_RIGHT]:
        velocityX = -1 * speed
        shipright = pygame.transform.rotate(ship,270)
        right = True
        left = False
        up = False
        down = False

    if keys[pygame.K_UP]:
        shipup = ship
        velocityY = 1 * speed
        right = False
        left = False
        up = True
        down = False

    if keys[pygame.K_DOWN]:
        velocityY = -1 * speed
        shipdown = pygame.transform.rotate(ship,180)
        right = False
        left = False
        up = False
        down = True

    for i in stars:

        i[0] += int(round(velocityX))
        i[1] += int(round(velocityY))
        pygame.draw.circle(win, starcolor, i, starSize) 
        if i[1] > spaceHeight:
            i[0] = random.randrange(200,spaceWidth)
            i[1] = 0
        if i[1] < 0:
            ########
            i[0] = random.randrange(200,spaceWidth)
            i[1] = spaceHeight
        if i[0] > windowWidth:
            i[0] = 200
            i[1] = random.randrange(0, spaceHeight)
        if i[0] < 200:
            i[0] = windowWidth
            i[1] = random.randrange(0, spaceHeight)

    ###### Speed menue #######
    if mousex > 20 and mousex < 180 and mousey > 602 and mousey < 608:
        menuespeed[2] = mousex - 20
        if menuespeed[2] < 50:
            speed = 0
            print("speed 0")
        if menuespeed[2] > 50:
            speed = 2
            print("speed 2")
        if menuespeed[2] > 100: 
            speed = 5
            print("speed 5")
        if menuespeed[2] > 140:
            speed = 8
            print("speed 8")
        
    pygame.draw.rect(win, yellow, pygame.Rect(menuespeedbg[0], menuespeedbg[1], menuespeedbg[2], menuespeedbg[3]))
    pygame.draw.rect(win, blue, pygame.Rect(menuespeed[0], menuespeed[1], menuespeed[2], menuespeed[3]))

    ##### speed menue #######

    pygame.display.flip()
    ###########
    
    redrawGameWindow()

pygame.quit()
