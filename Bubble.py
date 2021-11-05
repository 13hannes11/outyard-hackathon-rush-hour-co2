import pygame
import random

class Bubble:
    def __init__(self, posX, posY, radius = 1, color=(0,0,0), direction=(1,1)):
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.color = color
        self.directionX = direction[0]
        self.directionY = direction[1]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.posX, self.posY), self.radius)
    
    def update(self, screen):

        screen_width, screen_height = screen.get_size()
       
        self.move_x(screen_width)
        self.move_y(screen_height)

    def move_x(self, screen_width):
        if self.posX + self.radius + self.directionX < screen_width and self.posX - self.radius + self.directionX > 0:
            self.posX += self.directionX
        else:
            self.directionX *= -1


    def move_y(self, screen_height):
        if self.posY + self.radius + self.directionY < screen_height and self.posY - self.radius + self.directionY > 0:
            self.posY += self.directionY
        else:
            self.directionY *= -1


