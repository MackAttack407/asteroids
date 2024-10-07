import pygame
from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "GRAY", self.triangle(), width=2 )

    def update(self, dt):
        # sub-classes must override
        pass

    def collisions(self, other_circle):
        #returns true if there is a collision with anoter circle based on the radius
        distance = self.position.distance_to(other_circle.position)
        sum_rad = self.radius + other_circle.radius
        
        return distance <= sum_rad
    

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)  
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius)
    def update(self, dt):
        self.position += self.velocity * dt  