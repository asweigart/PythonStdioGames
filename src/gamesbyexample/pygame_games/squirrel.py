# Squirrel Eat Squirrel, by Al Sweigart al@inventwithpython.com
# (Requires Pygame) A game where squirrels eat each other and grow monstrously large.


__version__ = 1
import random, sys, time, math, pygame
from pygame.locals import *

FPS = 30 # frames per second to update the screen
WINWIDTH = 640 # width of the program's window, in pixels
WINHEIGHT = 480 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

GRASSCOLOR = (24, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

CAMERASLACK = 90     # how far from the center the squirrel moves before moving the camera
MOVERATE = 9         # how fast the player moves
BOUNCERATE = 6       # how fast the player bounces (large is slower)
BOUNCEHEIGHT = 30    # how high the player bounces
STARTSIZE = 25       # how big the player starts off
WINSIZE = 300        # how big the player needs to be to win
INVULNTIME = 2       # how long the player is invulnerable after being hit in seconds
GAMEOVERTIME = 4     # how long the "game over" text stays on the screen in seconds
MAXHEALTH = 3        # how much health the player starts with

NUMGRASS = 80        # number of grass objects in the active area
NUMSQUIRRELS = 30    # number of squirrels in the active area
SQUIRRELMINSPEED = 3 # slowest squirrel speed
SQUIRRELMAXSPEED = 7 # fastest squirrel speed
DIRCHANGEFREQ = 2    # % chance of direction change per frame
LEFT = 'left'
RIGHT = 'right'

"""
This program has three data structures to represent the player, enemy squirrels, and grass background objects. The data structures are dictionaries with the following keys:

Keys used by all three data structures:
    'x' - the left edge coordinate of the object in the game world (not a pixel coordinate on the screen)
    'y' - the top edge coordinate of the object in the game world (not a pixel coordinate on the screen)
    'rect' - the pygame.Rect object representing where on the screen the object is located.
Player data structure keys:
    'surface' - the pygame.Surface object that stores the image of the squirrel which will be drawn to the screen.
    'facing' - either set to LEFT or RIGHT, stores which direction the player is facing.
    'size' - the width and height of the player in pixels. (The width & height are always the same.)
    'bounce' - represents at what point in a bounce the player is in. 0 means standing (no bounce), up to BOUNCERATE (the completion of the bounce)
    'health' - an integer showing how many more times the player can be hit by a larger squirrel before dying.
Enemy Squirrel data structure keys:
    'surface' - the pygame.Surface object that stores the image of the squirrel which will be drawn to the screen.
    'movex' - how many pixels per frame the squirrel moves horizontally. A negative integer is moving to the left, a positive to the right.
    'movey' - how many pixels per frame the squirrel moves vertically. A negative integer is moving up, a positive moving down.
    'width' - the width of the squirrel's image, in pixels
    'height' - the height of the squirrel's image, in pixels
    'bounce' - represents at what point in a bounce the player is in. 0 means standing (no bounce), up to BOUNCERATE (the completion of the bounce)
    'bouncerate' - how quickly the squirrel bounces. A lower number means a quicker bounce.
    'bounceheight' - how high (in pixels) the squirrel bounces
Grass data structure keys:
    'grassImage' - an integer that refers to the index of the pygame.Surface object in GRASSIMAGES used for this grass object
"""

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASSIMAGES

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('gameicon.png'))
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Squirrel Eat Squirrel')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    # load the image files
    L_SQUIR_IMG = pygame.image.load('squirrel.png')
    R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, False)
    GRASSIMAGES = []
    for i in range(1, 5):
        GRASSIMAGES.append(pygame.image.load('grass%s.png' % i))

    while True:
        runGame()


def runGame():
    # set up variables for the start of a new game
    invulnerableMode = False  # if the player is invulnerable
    invulnerableStartTime = 0 # time the player became invulnerable
    gameOverMode = False      # if the player has lost
    gameOverStartTime = 0     # time the player lost
    winMode = False           # if the player has won

    # create the surfaces to hold game text
    gameOverSurf = BASICFONT.render('Game Over', True, WHITE)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

    winSurf = BASICFONT.render('You have achieved OMEGA SQUIRREL!', True, WHITE)
    winRect = winSurf.get_rect()
    winRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

    winSurf2 = BASICFONT.render('(Press "r" to restart.)', True, WHITE)
    winRect2 = winSurf2.get_rect()
    winRect2.center = (HALF_WINWIDTH, HALF_WINHEIGHT + 30)

    # camerax and cameray are the top left of where the camera view is
    camerax = 0
    cameray = 0

    grassObjs = []    # stores all the grass objects in the game
    squirrelObjs = [] # stores all the non-player squirrel objects
    # stores the player object:
    playerObj = {'surface': pygame.transform.scale(L_SQUIR_IMG, (STARTSIZE, STARTSIZE)),
                 'facing': LEFT,
                 'size': STARTSIZE,
                 'x': HALF_WINWIDTH,
                 'y': HALF_WINHEIGHT,
                 'bounce':0,
                 'health': MAXHEALTH}

    moveLeft  = False
    moveRight = False
    moveUp    = False
    moveDown  = False

    # start off with some random grass images on the screen
    for i in range(10):
        grassObjs.append(makeNewGrass(camerax, cameray))
        grassObjs[i]['x'] = random.randint(0, WINWIDTH)
        grassObjs[i]['y'] = random.randint(0, WINHEIGHT)

    while True: # main game loop
        # Check if we should turn off invulnerability
        if invulnerableMode and time.time() - invulnerableStartTime > INVULNTIME:
            invulnerableMode = False

        # move all the squirrels
        for sObj in squirrelObjs:
            # move the squirrel, and adjust for their bounce
            sObj['x'] += sObj['movex']
            sObj['y'] += sObj['movey']
            sObj['bounce'] += 1
            if sObj['bounce'] > sObj['bouncerate']:
                sObj['bounce'] = 0 # reset bounce amount

            # random chance they change direction
            if random.randint(0, 99) < DIRCHANGEFREQ:
                sObj['movex'] = getRandomVelocity()
                sObj['movey'] = getRandomVelocity()
                if sObj['movex'] > 0: # faces right
                    sObj['surface'] = pygame.transform.scale(R_SQUIR_IMG, (sObj['width'], sObj['height']))
                else: # faces left
                    sObj['surface'] = pygame.transform.scale(L_SQUIR_IMG, (sObj['width'], sObj['height']))


        # go through all the objects and see if any need to be deleted.
        for i in range(len(grassObjs) - 1, -1, -1):
            if isOutsideActiveArea(camerax, cameray, grassObjs[i]):
                del grassObjs[i]
        for i in range(len(squirrelObjs) - 1, -1, -1):
            if isOutsideActiveArea(camerax, cameray, squirrelObjs[i]):
                del squirrelObjs[i]

        # add more grass & squirrels if we don't have enough.
        while len(grassObjs) < NUMGRASS:
            grassObjs.append(makeNewGrass(camerax, cameray))
        while len(squirrelObjs) < NUMSQUIRRELS:
            squirrelObjs.append(makeNewSquirrel(camerax, cameray))

        # adjust camerax and cameray if beyond the "camera slack"
        playerCenterx = playerObj['x'] + int(playerObj['size'] / 2)
        playerCentery = playerObj['y'] + int(playerObj['size'] / 2)
        if (camerax + HALF_WINWIDTH) - playerCenterx > CAMERASLACK:
            camerax = playerCenterx + CAMERASLACK - HALF_WINWIDTH
        elif playerCenterx - (camerax + HALF_WINWIDTH) > CAMERASLACK:
            camerax = playerCenterx - CAMERASLACK - HALF_WINWIDTH
        if (cameray + HALF_WINHEIGHT) - playerCentery > CAMERASLACK:
            cameray = playerCentery + CAMERASLACK - HALF_WINHEIGHT
        elif playerCentery - (cameray + HALF_WINHEIGHT) > CAMERASLACK:
            cameray = playerCentery - CAMERASLACK - HALF_WINHEIGHT

        # draw the green background
        DISPLAYSURF.fill(GRASSCOLOR)

        # draw all the grass objects on the screen
        for gObj in grassObjs:
            gRect = pygame.Rect( (gObj['x'] - camerax,
                                  gObj['y'] - cameray,
                                  gObj['width'],
                                  gObj['height']) )
            DISPLAYSURF.blit(GRASSIMAGES[gObj['grassImage']], gRect)


        # draw the other squirrels
        for sObj in squirrelObjs:
            sObj['rect'] = pygame.Rect( (sObj['x'] - camerax,
                                         sObj['y'] - cameray - getBounceAmount(sObj['bounce'], sObj['bouncerate'], sObj['bounceheight']),
                                         sObj['width'],
                                         sObj['height']) )
            DISPLAYSURF.blit(sObj['surface'], sObj['rect'])


        # draw the player squirrel
        flashIsOn = round(time.time(), 1) * 10 % 2 == 1
        if not gameOverMode and not (invulnerableMode and flashIsOn):
            playerObj['rect'] = pygame.Rect( (playerObj['x'] - camerax,
                                              playerObj['y'] - cameray - getBounceAmount(playerObj['bounce'], BOUNCERATE, BOUNCEHEIGHT),
                                              playerObj['size'],
                                              playerObj['size']) )
            DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])


        # draw the health meter
        drawHealthMeter(playerObj['health'])

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    moveDown = False
                    moveUp = True
                elif event.key in (K_DOWN, K_s):
                    moveUp = False
                    moveDown = True
                elif event.key in (K_LEFT, K_a):
                    moveRight = False
                    moveLeft = True
                    if playerObj['facing'] != LEFT: # change player image
                        playerObj['surface'] = pygame.transform.scale(L_SQUIR_IMG, (playerObj['size'], playerObj['size']))
                    playerObj['facing'] = LEFT
                elif event.key in (K_RIGHT, K_d):
                    moveLeft = False
                    moveRight = True
                    if playerObj['facing'] != RIGHT: # change player image
                        playerObj['surface'] = pygame.transform.scale(R_SQUIR_IMG, (playerObj['size'], playerObj['size']))
                    playerObj['facing'] = RIGHT
                elif winMode and event.key == K_r:
                    return

            elif event.type == KEYUP:
                # stop moving the player's squirrel
                if event.key in (K_LEFT, K_a):
                    moveLeft = False
                elif event.key in (K_RIGHT, K_d):
                    moveRight = False
                elif event.key in (K_UP, K_w):
                    moveUp = False
                elif event.key in (K_DOWN, K_s):
                    moveDown = False

                elif event.key == K_ESCAPE:
                    terminate()

        if not gameOverMode:
            # actually move the player
            if moveLeft:
                playerObj['x'] -= MOVERATE
            if moveRight:
                playerObj['x'] += MOVERATE
            if moveUp:
                playerObj['y'] -= MOVERATE
            if moveDown:
                playerObj['y'] += MOVERATE

            if (moveLeft or moveRight or moveUp or moveDown) or playerObj['bounce'] != 0:
                playerObj['bounce'] += 1

            if playerObj['bounce'] > BOUNCERATE:
                playerObj['bounce'] = 0 # reset bounce amount

            # check if the player has collided with any squirrels
            for i in range(len(squirrelObjs)-1, -1, -1):
                sqObj = squirrelObjs[i]
                if 'rect' in sqObj and playerObj['rect'].colliderect(sqObj['rect']):
                    # a player/squirrel collision has occurred

                    if sqObj['width'] * sqObj['height'] <= playerObj['size']**2:
                        # player is larger and eats the squirrel
                        playerObj['size'] += int( (sqObj['width'] * sqObj['height'])**0.2 ) + 1
                        del squirrelObjs[i]

                        if playerObj['facing'] == LEFT:
                            playerObj['surface'] = pygame.transform.scale(L_SQUIR_IMG, (playerObj['size'], playerObj['size']))
                        if playerObj['facing'] == RIGHT:
                            playerObj['surface'] = pygame.transform.scale(R_SQUIR_IMG, (playerObj['size'], playerObj['size']))

                        if playerObj['size'] > WINSIZE:
                            winMode = True # turn on "win mode"

                    elif not invulnerableMode:
                        # player is smaller and takes damage
                        invulnerableMode = True
                        invulnerableStartTime = time.time()
                        playerObj['health'] -= 1
                        if playerObj['health'] == 0:
                            gameOverMode = True # turn on "game over mode"
                            gameOverStartTime = time.time()
        else:
            # game is over, show "game over" text
            DISPLAYSURF.blit(gameOverSurf, gameOverRect)
            if time.time() - gameOverStartTime > GAMEOVERTIME:
                return # end the current game

        # check if the player has won.
        if winMode:
            DISPLAYSURF.blit(winSurf, winRect)
            DISPLAYSURF.blit(winSurf2, winRect2)

        pygame.display.update()
        FPSCLOCK.tick(FPS)




def drawHealthMeter(currentHealth):
    for i in range(currentHealth): # draw red health bars
        pygame.draw.rect(DISPLAYSURF, RED,   (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10))
    for i in range(MAXHEALTH): # draw the white outlines
        pygame.draw.rect(DISPLAYSURF, WHITE, (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10), 1)


def terminate():
    pygame.display.quit(); pygame.quit() # Display quit is a workaround for a Raspberry Pi bug.
    sys.exit()


def getBounceAmount(currentBounce, bounceRate, bounceHeight):
    # Returns the number of pixels to offset based on the bounce.
    # Larger bounceRate means a slower bounce.
    # Larger bounceHeight means a higher bounce.
    # currentBounce will always be less than bounceRate
    return int(math.sin( (math.pi / float(bounceRate)) * currentBounce ) * bounceHeight)

def getRandomVelocity():
    speed = random.randint(SQUIRRELMINSPEED, SQUIRRELMAXSPEED)
    if random.randint(0, 1) == 0:
        return speed
    else:
        return -speed


def getRandomOffCameraPos(camerax, cameray, objWidth, objHeight):
    # create a Rect of the camera view
    cameraRect = pygame.Rect(camerax, cameray, WINWIDTH, WINHEIGHT)
    while True:
        x = random.randint(camerax - WINWIDTH, camerax + (2 * WINWIDTH))
        y = random.randint(cameray - WINHEIGHT, cameray + (2 * WINHEIGHT))
        # create a Rect object with the random coordinates and use colliderect()
        # to make sure the right edge isn't in the camera view.
        objRect = pygame.Rect(x, y, objWidth, objHeight)
        if not objRect.colliderect(cameraRect):
            return x, y


def makeNewSquirrel(camerax, cameray):
    sq = {}
    generalSize = random.randint(5, 25)
    multiplier = random.randint(1, 3)
    sq['width']  = (generalSize + random.randint(0, 10)) * multiplier
    sq['height'] = (generalSize + random.randint(0, 10)) * multiplier
    sq['x'], sq['y'] = getRandomOffCameraPos(camerax, cameray, sq['width'], sq['height'])
    sq['movex'] = getRandomVelocity()
    sq['movey'] = getRandomVelocity()
    if sq['movex'] < 0: # squirrel is facing left
        sq['surface'] = pygame.transform.scale(L_SQUIR_IMG, (sq['width'], sq['height']))
    else: # squirrel is facing right
        sq['surface'] = pygame.transform.scale(R_SQUIR_IMG, (sq['width'], sq['height']))
    sq['bounce'] = 0
    sq['bouncerate'] = random.randint(10, 18)
    sq['bounceheight'] = random.randint(10, 50)
    return sq


def makeNewGrass(camerax, cameray):
    gr = {}
    gr['grassImage'] = random.randint(0, len(GRASSIMAGES) - 1)
    gr['width']  = GRASSIMAGES[0].get_width()
    gr['height'] = GRASSIMAGES[0].get_height()
    gr['x'], gr['y'] = getRandomOffCameraPos(camerax, cameray, gr['width'], gr['height'])
    gr['rect'] = pygame.Rect( (gr['x'], gr['y'], gr['width'], gr['height']) )
    return gr


def isOutsideActiveArea(camerax, cameray, obj):
    # Return False if camerax and cameray are more than
    # a half-window length beyond the edge of the window.
    boundsLeftEdge = camerax - WINWIDTH
    boundsTopEdge = cameray - WINHEIGHT
    boundsRect = pygame.Rect(boundsLeftEdge, boundsTopEdge, WINWIDTH * 3, WINHEIGHT * 3)
    objRect = pygame.Rect(obj['x'], obj['y'], obj['width'], obj['height'])
    return not boundsRect.colliderect(objRect)


if __name__ == '__main__':
    main()