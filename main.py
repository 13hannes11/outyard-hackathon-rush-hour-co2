import pygame
import random
import sys
from pygame.locals import *

from Car  import Car
from Vacuum import Vacuum

pygame.init()

BUBBLE_LIMIT = 1000

SCREEN = pygame.display.set_mode((800,600))
BACKGROUND = (255,255,255)
SCREEN.fill(BACKGROUND)
CLOCK = pygame.time.Clock()

game_objects = []
bubble_objects = []
for i in range(10):
    game_objects.append(Car(random.uniform(0, 200), i * 50, 30, 50, bubble_objects, directionX=random.uniform(1, 5)))

game_objects.append(Vacuum(bubble_objects))

while True:
    SCREEN.fill(BACKGROUND)

    if len(bubble_objects) < BUBBLE_LIMIT:
        for game_object in bubble_objects:
            game_object.update(SCREEN)
        for game_object in bubble_objects:
            game_object.draw(SCREEN)

        for game_object in game_objects:
            game_object.update(SCREEN)
        for game_object in game_objects:
            game_object.draw(SCREEN)
    else:
        # TODO game over screen with message to reduce driving cars
        pass


    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    CLOCK.tick(60)
