# This was built from the tutorial https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
import pygame, math, random
from pygame.locals import *
import pyganim
 
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('PyGame - Testing')
 
rootImg = "resources/images/basic_game/"
rootAud = "resources/audio/basic_game/"

player = pygame.image.load(rootImg + "dude.png")
grass = pygame.image.load(rootImg + "grass.png")
castle = pygame.image.load(rootImg + "castle.png").convert_alpha()
# cow = pygame.image.load("resources/images/animals/cow/cow_front.png") #subject to change



# Used https://github.com/asweigart/pyganim/tree/master/examples
# http://www.pygame.org/project-Pyganim+sprite+animation+module-2106-.html
# for the sprite sheets
cows = pyganim.getImagesFromSpriteSheet(
    filename="resources/images/animals/cow/cow_front.png", 
    rows=4, cols=2,
    scale=2)
cframes = list(zip(cows, [100] * len(cows)))
cowObj = pyganim.PygAnimation(cframes)
cowObj.play()

# 4 - keep looping through
running = 1
while running:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))   

    cowObj.blit(screen, (100, 50))
    # screen.blit(castle, (100,100))

    # 7 - update the screen
    pygame.display.flip()

    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()