import pygame
import os


class Enemy():
    def __init__(self):
        self.pos = [690, 150]
        self.sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/paddle.png"))
        self.speed = 3
        self.limits = (5,350)
        self.rect = pygame.rect.Rect(self.pos,(10,50))

    def draw(self,display):
        display.blit(self.sprite, self.pos)

    def update(self, ball_pos):
        self.move_towards(ball_pos)

    def move_towards(self, pos):
        if self.pos[1] > pos[1]-20 or self.pos[1] < pos[1] + 20:
            if self.pos[1] < pos[1] - 20:
                self.pos[1] += self.speed
            else:
                self.pos[1] -= self.speed
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.rect.Rect(self.pos,(10,50))