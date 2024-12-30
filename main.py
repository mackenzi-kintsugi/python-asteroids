# be sure to activate venv by using, source venv/bin/activate

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player, Shot  # Add Player import
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Add the Player & Asteroid class to their needed groups
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable) # Ensure tuple
    
    # Create player and asteroid field instances (before the loop)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # instantiate a Player object in the middle of the screen
    asteroidfield = AsteroidField()
    
    game_loop = True
    clock = pygame.time.Clock()
    dt = 0
       
    
    while game_loop:
        # update dt with delta time at each iterations
        dt = clock.tick(60) / 1000  # Convert from milliseconds to seconds
        
        # hand events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            
        # Update game state
        updatable.update(dt)
        
        # Shots fired!
        for sprite in updatable:
            result = sprite.update(dt)
            if isinstance(result, Shot):  # If a shot was created
                shots.add(result)  # Add it to the shots group        
        
        # Collision detection check
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game Over!")
                #import sys
                #sys.exit()
        
        for shot in shots:
            collided_asteroids = pygame.sprite.spritecollide(shot, asteroids, True)
            
            # If I wish to make piercing rounds, get rid of below
            for asteroid in collided_asteroids:
                shot.kill()  # Assuming the shot should be removed after collision
                # You may handle other reactions, like playing sounds or updating scores here
 
        
        screen.fill((0, 0, 0))     
        # render/draw everything, before flip
        drawable.draw(screen)
        
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()