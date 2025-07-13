from asteroidfield import AsteroidField
import sys
from asteroids import Asteroid
from player import * 
import pygame
import random
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    loop = True
    clock = pygame.time.Clock()
    x_coordinate = SCREEN_WIDTH / 2
    y_coordinate = SCREEN_HEIGHT / 2

    # creates containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # set containers that the object will automatically join
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    # instantiation of the obj automatically adds it to the containers
    player = Player(x_coordinate, y_coordinate)
    asteroidfield = AsteroidField()

    dt = 0
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for obj in asteroids:
            if player.collision(obj):
                print("Game Over !")
                sys.exit()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()    

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
        main()
    
