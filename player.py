import pygame
from pygame.sprite import Sprite
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape

class Player(CircleShape, Sprite):
    
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        Sprite.__init__(self)
        self.rotation = 0
        
        height_multiplier = 1.5
        # Make surface even larger to ensure triangle fits
        surface_size = int(PLAYER_RADIUS * 3)  # Increased overall surface size
           
        self.image = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA) # Create a surface for the sprite
        self.rect = self.image.get_rect(center=(x, y)) # Create a rect for positioning       
        
         
        # Draw triangle relative to surface center
       
        center = (surface_size // 2, surface_size // 2) # Center point is now in middle of the larger surface
        points = [
            (center[0], center[1] - PLAYER_RADIUS * height_multiplier),  # top point (the front)
            (center[0] - PLAYER_RADIUS, center[1] + PLAYER_RADIUS),      # bottom left
            (center[0] + PLAYER_RADIUS, center[1] + PLAYER_RADIUS)       # bottom right
        ]
       
               
        pygame.draw.polygon(self.image, "white", points, 2)
        # Save original image for rotation
        self.original_image = self.image.copy()
    

    def rotate(self, dt):
        # This method should modify self.rotation directly
        self.rotation += PLAYER_TURN_SPEED * dt 
        # Rotate the sprite's image
        rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)
        self.image = rotated_image
        # Keep the rect centered
        self.rect = self.image.get_rect(center=self.position)
    
    
    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    
        # Update the sprite's rect position to match
        self.rect.center = self.position


    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
        # if we press the left key, the ship should rotate to the left
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
        # if we press the right key, the ship should rotate to the right
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
            
        if keys[pygame.K_s]:
            self.move(-dt)
