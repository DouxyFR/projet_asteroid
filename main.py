# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        dt = clock.tick(60)/1000
        #print(f"dt={dt}")
        pygame.Surface.fill(screen, "black")

        for thing in updatable:
            thing.update(dt)

        for thing in asteroids:
            if thing.check_collision(player) == True:
                print("Game over!")
                exit()


        for thing in drawable:
            thing.draw(screen)
        
        #player.update(dt)
        #player.draw(screen)
        pygame.display.flip()
        
        

        





if __name__ == "__main__":
    main()