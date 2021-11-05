import pygame
import random
import sys
from pygame.locals import *

from Bubble import Bubble
from Car  import Car

pygame.init()

SCREEN = pygame.display.set_mode((800,600))
BACKGROUND = (255,255,255)
SCREEN.fill(BACKGROUND)
CLOCK = pygame.time.Clock()

car_objects = []
bubble_objects = []
for i in range(10):
    car_objects.append(Car(random.uniform(0, 200), i * 50, 30, 50, car_objects, directionX=random.uniform(1, 5)))

while True:
    SCREEN.fill(BACKGROUND)
    for game_object in car_objects:
        game_object.update(SCREEN)
    for game_object in car_objects:
        game_object.draw(SCREEN)

    for game_object in bubble_objects:
        game_object.update(SCREEN)
    for game_object in bubble_objects:
        game_object.draw(SCREEN)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    CLOCK.tick(60)
