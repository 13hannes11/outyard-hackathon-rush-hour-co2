import pygame
import random
from Bubble import Bubble

class Car:
    def __init__(self, posX, posY, height, width, game_objects, color=(0,0,0), directionX=1):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.directionX = directionX
        self.width = width
        self.height = height
        self.game_objects = game_objects
        self.bubble_spawn_time_ms = 1000
        self.time_of_last_spawn = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.posX, self.posY, self.width, self.height))
    
    def update(self, screen):
        self.posX += self.directionX
        screen_width, screen_height = screen.get_size()
        if self.posX > screen_width:
            self.posX = -self.width
        if self.bubble_spawn_time_ms + self.time_of_last_spawn < pygame.time.get_ticks():
            bubble_y_direction = random.uniform(-1, 1)
            bubble_x_speeddiff = random.uniform(0, 0.9)
            bubble_radius = random.uniform(5, 10)
            self.game_objects.append(Bubble(self.posX, self.posY, radius=bubble_radius, direction=(-self.directionX * bubble_x_speeddiff,bubble_y_direction)))
            self.time_of_last_spawn = pygame.time.get_ticks()
