import pygame
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    
    px = SCREEN_WIDTH / 2
    py = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)

    AsteroidField()
    player = Player(px, py)
    player

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        updatable.update(dt)
        screen.fill(000000)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


        dt = clock.tick(60) / 1000


    

if __name__ == "__main__":
    main()
