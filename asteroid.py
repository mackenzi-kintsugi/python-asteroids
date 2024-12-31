''' Note - Pygame Rect:
If Asteroid instances will be involved in collision detections or graphical boundary checks,
you may eventually want to implement self.rect and update it based on self.position.
'''

import pygame
import random
#from pygame.sprite import Sprite
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
        x, y = position.x, position.y
        super().__init__(x, y, radius) # Now you can use x and y as intended
        self.velocity = velocity
        
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
         
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []

        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Convert the position to Vector2
        position = pygame.Vector2(self.rect.center)

        # Create new velocities
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        # Create new asteroids with Vector2 position
        new_asteroid1 = Asteroid(position=position, radius=new_radius, velocity=velocity1 * 1.2)
        new_asteroid2 = Asteroid(position=position, radius=new_radius, velocity=velocity2 * 1.2)

        return [new_asteroid1, new_asteroid2]
    
        '''
        # Solution (but still causes crash due to incompatibility with my other files)
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
        '''