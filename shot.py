import pygame
from circleshape import *
from constants import SHOT_RADIUS
from player import *

class Shot(CircleShape):
    def __init__(self, x, y):
        self.radius = SHOT_RADIUS
        super().__init__(x, y, self.radius)
        
    def draw(self, screen):
        shot = pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position = self.position + self.velocity * dt
