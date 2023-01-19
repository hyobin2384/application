import pygame
from game import Game

turn = 0
running = True

pygame.init()
g = Game()
pygame.display.set_caption("Omok")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 한 칸당 29정도
        # screen.blit(black_stone,(58,29)) 
        # screen.blit(white_stone,(29,29))
        if event.type == pygame.MOUSEBUTTONUP:
            if turn == 0:
                g.blit_black_stoen()
                turn = 1
            elif turn == 1:
                g.blit_white_stoen()
                turn = 0
        # if event.type == pygame.MOUSEBUTTONUP:
        #     ...
        pygame.display.update()
pygame.quit()