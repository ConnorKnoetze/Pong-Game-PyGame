import pygame
import os

class player_Paddle():
    def __init__(self):
        self.pos = [0, 150]
        self.sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/paddle.png"))
        self.speed = 5
        self.limits = (5,350)
        self.rect = pygame.rect.Rect(self.pos,(10,50))

    def draw(self,display):
        display.blit(self.sprite, self.pos)

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            if self.pos[1] >= self.limits[0]:
                self.pos[1] -= self.speed
        
        if key_pressed[pygame.K_DOWN]:
            if self.pos[1] < self.limits[1]:
                self.pos[1] += self.speed
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.rect.Rect(self.pos,(10,50))
