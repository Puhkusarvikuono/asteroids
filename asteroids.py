import pygame, random
from circleshape import *
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        asteroid = pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_rotation = random.uniform(20, 50)
        split_velocity1 = self.velocity.rotate(random_rotation)
        split_velocity2 = self.velocity.rotate(-random_rotation)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_split1 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_split2 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_split1.velocity = split_velocity1
        asteroid_split2.velocity = split_velocity2

    
    def update(self, dt):
        self.position = self.position + self.velocity * dt
