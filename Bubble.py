import pygame
import random

class Bubble:
    def __init__(self, posX, posY, image, radius = 1, color=(0,0,255), direction=(1,1)):
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.color = color
        self.directionX = direction[0]
        self.directionY = direction[1]
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.posX - self.radius, self.posY - self.radius))
    
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


