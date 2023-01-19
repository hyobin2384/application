import pygame

pygame.init()

turn = 0
screen_width = 549
screen_height = 549
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("omok")

background = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\Omoktable.PNG")

black_stone = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\black.png")
bs_size = black_stone.get_rect().size
bs_width = bs_size[0]
bs_height = bs_size[1]

white_stone = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\white.png")
ws_size = white_stone.get_rect().size
ws_width = ws_size[0]
ws_height = ws_size[1]

running = True

screen.blit(background, (0,0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 한 칸당 29정도
        # screen.blit(black_stone,(58,29)) 
        # screen.blit(white_stone,(29,29))
        if event.type == pygame.MOUSEBUTTONUP:
            x = pygame.mouse.get_pos()[0]-(bs_width/2)
            y = pygame.mouse.get_pos()[1]-(bs_height/2)
            if turn == 0:
                screen.blit(black_stone,(x,y))
                turn = 1
            elif turn == 1:
                screen.blit(white_stone,(x,y))
                turn = 0
        # if event.type == pygame.MOUSEBUTTONUP:
        #     ...
        pygame.display.update()
pygame.quit()