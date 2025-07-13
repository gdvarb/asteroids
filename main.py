from player import * 
import pygame
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
    # set containers that the object will automatically join
    Player.containers = (updatable, drawable)
    # instantiation of the Player obj automatically adds it to the containers
    player = Player(x_coordinate, y_coordinate)

    dt = 0
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()    

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
        main()
    
