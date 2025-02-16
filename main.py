#this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main(): 
    pygame.init()
    
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(1):
        #this diplays the window for the game
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()

        #this checks the events happening on the screen and 
        #if the quit event is checked it closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return







if __name__=="__main__":
    main()
