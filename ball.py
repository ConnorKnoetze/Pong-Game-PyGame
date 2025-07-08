import pygame
import random
import os

class Ball():
    def __init__(self):
        self.img = pygame.image.load(os.path.join(os.path.dirname(__file__), "images/ball.png"))
        self.up_down_limits = (0, 395)
        self.left_right_limits = (0, 700)
        self.start = random.randint(0,1)
        self.has_started = False
        self.speed = 5
        self.pos = [345, 195]
        self.direction = [0,0]
        self.rect = pygame.rect.Rect(tuple(self.pos), (10,10))
    
    def draw(self, display):
        display.blit(self.img, self.pos)

    def move(self):

        if not self.has_started:
            if self.start == 0:
                self.direction[0] = -1
            else:
                self.direction[0] = 1
            self.has_started = True
        if self.pos[1] >= self.up_down_limits[0] and self.pos[1] < self.up_down_limits[1]:
            self.pos[0], self.pos[1] = self.pos[0] + (self.direction[0] * self.speed), self.pos[1] + (self.direction[1] * self.speed)
        else:
            self.direction[1] *= -1
            if self.pos[1] < 200:
                self.pos[1] = 1
            else:
                self.pos[1] = 394
            
        if self.pos[0] < self.left_right_limits[0]:
            return 0
        if self.pos[0] > self.left_right_limits[1]:
            return 1
        self.update_rect()
    def reset(self):
        self.pos = [345, 195]
        self.start = random.randint(0,1)
        self.speed = 5
        self.has_started = False
    
    def update_rect(self):
        self.rect = pygame.rect.Rect(tuple(self.pos), (10,10))
    
    def rebound_player(self):
        rand = random.randint(0, 1)
        if rand == 0:
            self.direction = [1, -random.random()]
        else:
            self.direction = [1, random.random()]
    
    def get_pos(self):
        return self.pos
    
    def rebound_enemy(self):
        rand = random.randint(0, 1)
        if rand == 0:
            self.direction = [-1, -random.random()]
        else:
            self.direction = [-1, random.random()]