import pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((549, 549))
        self.background = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\Omoktable.PNG")
        self.black_stone = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\black.png")
        self.white_stone = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\white.png")
        
        self.bs_width, self.bs_height = self.black_get_size()
        self.ws_width, self.ws_height = self.white_get_size()

        self.x = pygame.mouse.get_pos()[0]-(self.bs_width/2)
        self.y = pygame.mouse.get_pos()[1]-(self.bs_height/2)

        self.screen.blit(self.background, (0,0))
    
    def black_get_size(self):
        bs_size = self.black_stone.get_rect().size
        return bs_size[0], bs_size[1]
    
    def white_get_size(self):
        ws_size = self.white_stone.get_rect().size
        return ws_size[0], ws_size[1]

    def blit_black_stoen(self):
        self.screen.blit(self.black_stone,(self.x, self.y))

    def blit_white_stoen(self):
        self.screen.blit(self.white_stone,(self.x, self.y))