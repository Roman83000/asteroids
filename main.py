import pygame
import sys
from constants import * 
from player import * 
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    Asteroid.containers = (asteroids, updatable, drawable)


    AsteroidField.containers = (updatable)
    asterfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if player.is_collide(obj) == True:
                print("Game over!")
                sys.exit()



        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)   

        pygame.display.flip()
        dt = Clock.tick() / 1000
        


if __name__ == "__main__":
    main()