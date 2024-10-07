import pygame
from circleshape import *
from constants import *


class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, angle=0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.x = x
        self.y = y
        self.angle = angle
        self.position = pygame.Vector2(self.position.x, self.position.y)
        self.shot_timer = 0


# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        self.shot_timer -= dt
        if self.shot_timer < 0:
            self.shot_timer = 0

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_timer <= 0:
            #create a new shot at the players position
            new_shot = Shot(self.position.x, self.position.y)

            #calculate direction using the player's facing angle
            direction = pygame.math.Vector2(0, 1).rotate(self.rotation) #assume 'angle' holds players direction
            new_shot.velocity = direction * PLAYER_SHOOT_SPEED
            
            #reset the shot timer
            self.shot_timer = PLAYER_SHOOT_COOLDOWN

            return new_shot
        return None
    
    