import pygame
import random

from pygame import image
from Bubble import Bubble

class Vacuum:
    def __init__(self, bubble_objects):
        self.posX = -50
        self.posY = -50
        self.width = 124
        self.height = 57
        self.tube_width = 10
        self.bubble_objects = bubble_objects
        self.image = pygame.image.load("sprites/vacuum.png")
        self.image_body = pygame.image.load("sprites/vacuum_body.png")

    def draw(self, screen):
        screen_width, screen_height = screen.get_size()

        screen.blit(self.image_body, 
            ((screen_width - self.image_body.get_width()) / 2, 
            screen_height - (self.image_body.get_height() / 3.3)))
        screen.blit(self.image, (self.posX, self.posY))
        pygame.draw.line(screen, 
            (49, 86, 130),
            (screen_width / 2 - 20, screen_height - 30),
            (self.posX + (self.width - self.tube_width) / 2 , self.posY + self.height), 
            width=self.tube_width)
        

    def update(self, screen):
        x, y = pygame.mouse.get_pos()
        self.posX = x -(self.width / 2)
        self.posY = y -(self.height / 2)

        to_remove = []
    
        for i in range(len(self.bubble_objects)):
            x = self.bubble_objects[i].posX
            y = self.bubble_objects[i].posY
            if isPointInsideRect(x, y, pygame.Rect(self.posX, self.posY, self.width, self.height)):
                to_remove.append(i)

        for i in reversed(to_remove):
            del self.bubble_objects[i]



def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False
