import pygame

class Lane:
    def __init__(self, posY, width, height, add_markings=True):
        self.posX = 0
        self.posY = posY
        self.width = width
        self.height = height
        self.add_markings = add_markings

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.posX, self.posY, self.width, self.height))
        if self.add_markings:
            for i in range(6):
                pygame.draw.rect(screen, (70, 70, 70), pygame.Rect(self.posX + i * 150, self.posY + self.height-5, 70, 5))
        
    def update(self, screen):
        pass