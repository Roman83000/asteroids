import pygame
import sys
from constants import * 
from player import * 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = updatable
    asterfield = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    
    dt = 0
    



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if player.is_collide(obj):
                print("Game over!")
                sys.exit()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)   

        pygame.display.flip()
        dt = Clock.tick() / 1000
        


if __name__ == "__main__":
    main()