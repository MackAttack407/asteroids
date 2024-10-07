import pygame
from circleshape import *
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "PINK", self.position, self.radius, width = 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        ran_angle = random.uniform(20, 50)
        new_vector = self.velocity.rotate(ran_angle)
        new_vector2 = self.velocity.rotate(-ran_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
            
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = new_vector * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vector2 * 1.2
            
        for group in self.groups():
            group.add(new_asteroid)
            group.add(new_asteroid2)



