import pygame
import table
import paddle
import ball
import enemy_paddle
import text

class Game():
    def __init__(self, display):
        self.table = table.Table()
        self.player = paddle.player_Paddle()
        self.enemy_paddle = enemy_paddle.Enemy()
        self.ball = ball.Ball()
        self.display = display
        self.points = [0,0]
        self.text = text.Score()

    

    def game_update(self):
        self.table.bg_init(self.display)
        self.text.render(self.display, self.points)
        self.player.update()
        self.player.draw(self.display)
        self.enemy_paddle.draw(self.display)
        self.enemy_paddle.update(self.ball.get_pos())
        point = self.ball.move()
        if point == 0:
            self.points[point] += 1
            self.ball.reset()
        if point == 1:
            self.points[point] += 1
            self.ball.reset()
        self.ball.draw(self.display)
        self.check_player_ball_coll()
        self.check_enemy_ball_coll()
        pygame.display.update()
    
    def check_player_ball_coll(self):
        if pygame.Rect.colliderect(self.player.rect, self.ball.rect):
            self.ball.rebound_player()
            self.ball.speed += 0.2

    def check_enemy_ball_coll(self):
        if pygame.Rect.colliderect(self.enemy_paddle.rect, self.ball.rect):
            self.ball.rebound_enemy()
            self.ball.speed += 0.2
