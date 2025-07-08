import pygame
import os

class Table():
    def __init__(self):
        pass

    def bg_init(self, display):
        bg = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/table.png"))
        display.blit(bg, (0,0))
        return