import pygame
import random
from Bubble import Bubble

class Vacuum:
    def __init__(self, bubble_objects):
        self.posX = -50
        self.posY = -50
        self.width = 50
        self.height = 50
        self.bubble_objects = bubble_objects

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.posX, self.posY, self.width, self.height))
    
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
