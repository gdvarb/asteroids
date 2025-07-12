from player import * 
import pygame
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    loop = True
    clock = pygame.time.Clock()
    dt = 0
    x_coordinate = SCREEN_WIDTH / 2
    y_coordinate = SCREEN_HEIGHT / 2
    player = Player(x_coordinate, y_coordinate)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()    


if __name__ == "__main__":
        main()
    
