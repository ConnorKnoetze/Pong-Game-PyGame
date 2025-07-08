import pygame
import game


pygame.init()

display = pygame.display.set_mode((700, 400))
game = game.Game(display)

clock = pygame.time.Clock()

running = True


while running:
    
    clock.tick(60)
    
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    game.game_update()

pygame.quit()