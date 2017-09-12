import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello world!')


start_button = pygame.draw.rect(DISPLAYSURF,(0,0,240),(150,90,100,50))
continue_button = pygame.draw.rect(DISPLAYSURF,(0,244,0),(150,160,100,50))
quit_button = pygame.draw.rect(DISPLAYSURF,(244,0,0),(150,230,100,50))

pygame.display.flip()

def startGame():
    DISPLAYSURF.fill((0,0,0));
    pygame.display.flip();

# run the game loop
while True:
    for event in pygame.event.get():
    	#print (event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                        pygame.quit()
                        sys.exit()
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                        startGame()
    pygame.display.update()
