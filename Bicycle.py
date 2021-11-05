import pygame
import random
from Bubble import Bubble

class Bicycle:
    def __init__(self, posX, posY, directionX=random.uniform(1, 3)):
        self.posX = posX
        self.posY = posY
        self.directionX = directionX
        self.width = 73
        self.height = 40
        self.image = pygame.image.load("sprites/bicycle.png")

        if directionX < 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen):
        screen.blit(self.image, (self.posX, self.posY))
        
    
    def update(self, screen):
        self.posX += self.directionX
        screen_width, screen_height = screen.get_size()
        if self.directionX > 0:
            if self.posX + self.width + self.directionX > screen_width:
                self.directionX = -random.uniform(1, 3)
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            if self.posX + self.directionX < 0:
                self.directionX = random.uniform(1, 3)
                self.image = pygame.transform.flip(self.image, True, False)

