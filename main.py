#this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main(): 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    time = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        #this checks the events happening on the screen and 
        #if the quit event is checked it closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #this diplays the window for the game
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        #limiting the framerate to 60
        dt = (time.tick(60)) / 1000










if __name__=="__main__":
    main()
