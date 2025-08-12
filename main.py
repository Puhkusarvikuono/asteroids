import pygame, sys
from pygame.time import Clock
from asteroids import *
from constants import *
from player import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player1 = Player(x, y)
    asteroid1 = Asteroid(2, 2, 2)
    asteroidfield1 = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for draw in drawable:
            draw.draw(screen)
        asteroid1.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player1) == True:
                sys.exit("Game Over!")
            for shot in shots:
                if asteroid.collision(shot) == True:
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000

if __name__ == "__main__":
    main()
