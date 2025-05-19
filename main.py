# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    group_updates = pygame.sprite.Group()
    group_draws = pygame.sprite.Group()
    Shot.containers = (shots, group_draws, group_updates)
    Asteroid.containers = (asteroids, group_draws, group_updates)
    AsteroidField.containers = (group_updates)
    Player.containers = (group_draws, group_updates)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #instantiate player

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # color screen
        group_updates.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                pygame.quit()
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.kill()
        for item in group_draws:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()

if __name__ == "__main__":
    main()