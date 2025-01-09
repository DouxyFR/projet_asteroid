import pygame
from circleshape import *
from constants import *
from shoot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        listpoints = self.triangle()
        pygame.draw.polygon(screen, "white", listpoints, 2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
            keys = pygame.key.get_pressed()
            self.shoot_timer -= dt

            if keys[pygame.K_q]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_z]:
                self.move(+dt)
            if keys[pygame.K_s]:
                self.move(-dt)
            if keys[pygame.K_SPACE]:
                if(self.shoot_timer <= 0):
                    self.shoot_timer = PLAYER_SHOOT_COOLDOWN
                    self.shoot()

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
