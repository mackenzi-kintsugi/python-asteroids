''' Note - Pygame Rect:
If Asteroid instances will be involved in collision detections or graphical boundary checks,
you may eventually want to implement self.rect and update it based on self.position.
'''

import pygame
#from pygame.sprite import Sprite
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        # Image and angle initialization
        self.original_image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, "purple", (radius, radius), radius, 2)
        
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0  # Start rotation angle

    def update(self, dt):
        # Update position
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)
        
        # Update angle
        self.angle += 1  # Rotate each frame, adjust speed as needed
        
        # Kill when leaving screen
        # Right to left, remove if past left screen edge
        if self.rect.right < 0:
            self.kill()
        # Left to right, remove if past right screen edge
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


    def draw(self, screen):
        # Rotate the image and update rect (not yet)
        #self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        # Draw the rotated image
        screen.blit(self.image, self.rect.topleft)
    
''' # old version
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
   
        # Define diameter and setup image
        diameter = radius * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA) # Create a surface for the sprite
     

        
    def draw(self, screen): # Draw the asteroid. Position and size are key here.
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
        # If later in development you want to manage sprite boundaries or other spatial operations using the Rect,
        # consider doing something with the returned value from draw.
    
    def update(self, dt):
        # Update position using the velocity and delta time
        self.position += self.velocity * dt
'''