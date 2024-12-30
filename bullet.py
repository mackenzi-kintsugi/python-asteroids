import pygame
from pygame.sprite import Sprite
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        
        # Image and angle initialization
        self.original_image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, "red", (radius, radius), radius, 1)
        
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0  # Start rotation angle

    def update(self, dt):        
        # Kill when leaving screen
        if (self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or
                self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT):
            self.kill()      
        
        # Update position
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)
        
        # Update angle
        self.angle += 1  # Rotate each frame, adjust speed as needed

    def draw(self, screen):
        # Rotate the image and update rect (not yet)
        #self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        # Draw the rotated image
        screen.blit(self.image, self.rect.topleft)
