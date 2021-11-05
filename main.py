import pygame
import random
import sys
from pygame.locals import *

from Car  import Car
from Vacuum import Vacuum

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FONT = pygame.font.SysFont('Comic Sans MS', 128)
TEXT_SCREEN = FONT.render('Game over!', False, (255, 255, 255))
TEXT_RECT = TEXT_SCREEN.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


BUBBLE_LIMIT = 100

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
BACKGROUND = (0,0,0)
SCREEN.fill(BACKGROUND)
CLOCK = pygame.time.Clock()

game_objects = []
bubble_objects = []
for i in range(4):
    game_objects.append(Car(random.uniform(0, SCREEN_WIDTH), i * 80 + 10, bubble_objects, directionX=random.uniform(1, 5)))
for i in range(4, 7):
    game_objects.append(Car(random.uniform(0, SCREEN_WIDTH), i * 80 + 10, bubble_objects, directionX= - random.uniform(1, 5)))

game_objects.append(Vacuum(bubble_objects))

while True:
    SCREEN.fill(BACKGROUND)
    pygame.display.set_caption("Rush Hour CO2")

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
        SCREEN.blit(TEXT_SCREEN, TEXT_RECT)
        pass


    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    CLOCK.tick(60)
