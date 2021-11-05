import pygame
import random
from Bubble import Bubble

class Car:
    def __init__(self, posX, posY, game_objects, color=(0, 255,0), directionX=1):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.directionX = directionX
        self.width = 173
        self.height = 66
        self.game_objects = game_objects
        self.bubble_spawn_time_ms = 1000
        self.time_of_last_spawn = 0
        self.BUBBLE_IMAGE = pygame.image.load("sprites/bubble.png")
        self.image = pygame.image.load("sprites/car.png")

        if directionX < 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, screen):
        screen.blit(self.image, (self.posX, self.posY))
        
    
    def update(self, screen):
        self.posX += self.directionX
        screen_width, screen_height = screen.get_size()
        if self.directionX > 0:
            if self.posX > screen_width:
                self.posX = -self.width
        else:
            if self.posX + self.width < 0:
                self.posX = screen_width + self.width

        
        if self.bubble_spawn_time_ms + self.time_of_last_spawn < pygame.time.get_ticks():
            bubble_y_direction = random.uniform(-1, 1)
            bubble_radius = 16
            if self.directionX > 0:
                bubble_x_speeddiff = random.uniform(0, 0.9)
                bubbleX = self.posX
            else:
                bubble_x_speeddiff = random.uniform(-0.9, 0)
                bubbleX = self.posX + self.width

            self.game_objects.append(Bubble(bubbleX, self.posY + self.height - bubble_radius, 
                self.BUBBLE_IMAGE, 
                radius=bubble_radius,
                direction=(-self.directionX * bubble_x_speeddiff,bubble_y_direction)))
            self.time_of_last_spawn = pygame.time.get_ticks()
