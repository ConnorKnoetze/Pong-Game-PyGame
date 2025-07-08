import pygame

class Score():
    def __init__(self):
        self.font = "fonts/FreeSansBold.ttf"

    def render(self, display, points):
        font = pygame.font.Font(self.font, 50)
        text = font.render(f"{points[1]}  {points[0]}", True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (350,50)
        display.blit(text, textRect)
