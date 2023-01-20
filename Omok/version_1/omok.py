import pygame
from rule import Rule

pygame.init()
turn = 0
screen_width = 549
screen_height = 549
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("omok")

background = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\image\Omoktable.PNG")

black_stone = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\image\black.png")
black_stone.set_colorkey((181,230,29))
bs_size = black_stone.get_rect().size
bs_width = bs_size[0]
bs_height = bs_size[1]

white_stone = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\image\white.png")
white_stone.set_colorkey((181,230,29))
ws_size = white_stone.get_rect().size
ws_width = ws_size[0]
ws_height = ws_size[1]

running = True
stone_half = 29.0

screen.blit(background, (0,0))

used_coordinates = set()
used_coordinates_black = []
used_coordinates_white = []
used_coordinates_sum = []
used_coordinates_sum.append(list(used_coordinates_black))
used_coordinates_sum.append(list(used_coordinates_white))

def result(self, turn):
    if turn == 0:
        print("흑의 승리입니다.")
    else:
        print("백의 승리입니다.")
    pygame.time.wait(1000)
    running = False
    exit()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            x = pygame.mouse.get_pos()[0]-(bs_width/2)
            y = pygame.mouse.get_pos()[1]-(bs_height/2)

            if x > 537:
                x = 537
            elif x < 0:
                x = 0

            if y > 537:
                y = 537
            elif y < 0:
                y = 0

            if (x%stone_half) > 14.6:
                x = x + (stone_half- (x%stone_half))
            elif (x%stone_half) <= 14.5:
                x = x - (x%stone_half)

            if (y%stone_half) > 14.6:
                y = y + (stone_half - (y%stone_half))
            elif (y%stone_half) <= 14.5:
                y = y - (y%stone_half)

            if (x,y) not in used_coordinates:
                if turn == 0:
                    used_coordinates_black.append((x,y))
                    screen.blit(black_stone,(x,y))
                else:
                    used_coordinates_white.append((x,y))
                    screen.blit(white_stone,(x,y))
                used_coordinates.add((x,y))
                Rule((x,y),used_coordinates_sum[turn])
            
            turn  = (turn+1)%2
            
        pygame.display.update()
pygame.quit()