# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_loop = True
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            
        screen.fill((0, 0, 0))
        pygame.display.flip()
        
if __name__ == "__main__":
    main()