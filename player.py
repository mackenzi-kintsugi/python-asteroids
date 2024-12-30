import pygame
from pygame.sprite import Sprite
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS,PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN 
from circleshape import CircleShape

class Player(CircleShape, Sprite):
    
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        Sprite.__init__(self)
        self.rotation = 0
        
        self.timer = 0
        
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
    
    def update(self, dt):
        # When the player shoots, set the timer equal to a new constant (PLAYER_SHOOT_COOLDOWN)
        self.timer = max(self.timer - dt, 0)  # Decrease and ensure it doesn't go below 0
        
        # Kill when leaving screen
        if (self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or
                self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT):
            self.kill()        
        
        # Key configurations
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
        # if we press the left key, the ship should rotate to the left
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
        # if we press the right key, the ship should rotate to the right
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
            
        '''        
        if keys[pygame.K_s]:
            self.move(-dt)
        '''

        if keys[pygame.K_SPACE]:
            return self.shoot() # Return the new shot
            
        return None # Return None if no shot created

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

    
    def shoot(self):        
        if self.timer > 0:
            return None # Exit the method early if the timer is active
        self.timer = PLAYER_SHOOT_COOLDOWN  # Reset timer after a shot is allowed
              
        # Create direction vector
        direction = pygame.Vector2(0, -1).rotate(self.rotation)
        # Scale it by shoot speed
        velocity = direction * PLAYER_SHOOT_SPEED
        # Create new shot at player's position
        return Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)

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
