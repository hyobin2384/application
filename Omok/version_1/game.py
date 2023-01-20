import pygame
class Game:
    def __init__(self):
        pygame.init()
        self.turn = 0
        self.stone_half = 29.0
        self.running = True
        self.event_type = 0
        self.used_black_coordinates = []
        self.used_white_coordinates = []
        self.sum_coordinates = set()

        self.screen = pygame.display.set_mode((549, 549))
        pygame.display.set_caption("Omok")
        self.background = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\image\Omoktable.PNG")
        self.black_stone = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\image\black.png")
        self.white_stone = pygame.image.load(r"C:\Users\user\Desktop\application\Omok\image\white.png")
        
        self.black_stone.set_colorkey((181,230,29))
        self.white_stone.set_colorkey((181,230,29))

        self.bs_width, self.bs_height = self.black_get_size()
        self.ws_width, self.ws_height = self.white_get_size()

        self.screen.blit(self.background, (0,0))
    
    def black_get_size(self):
        bs_size = self.black_stone.get_rect().size
        return bs_size[0], bs_size[1]
    
    def white_get_size(self):
        ws_size = self.white_stone.get_rect().size
        return ws_size[0], ws_size[1]

    def blit_black_stoen(self, args):
        self.screen.blit(self.black_stone,(args[0],args[1]))

    def blit_white_stoen(self, args):
        self.screen.blit(self.white_stone,(args[0],args[1]))

    def range_escape_fix(self, x, y):
        if x > 537:
            x = 537
        elif x < 0:
            x = 0

        if y > 537:
            y = 537
        elif y < 0:
            y = 0
        return x,y

    def stone_position(self, x, y):
        if (x % self.stone_half) > 14.6:
            x = x + (self.stone_half- (x % self.stone_half))
        elif (x % self.stone_half) <= 14.5:
            x = x - (x % self.stone_half)

        if (y % self.stone_half) > 14.6:
            y = y + (self.stone_half - (y % self.stone_half))
        elif (y % self.stone_half) <= 14.5:
            y = y - (y % self.stone_half)
        return x,y

    def mouse_position(self):
        x = pygame.mouse.get_pos()[0]-(self.bs_width/2)
        y = pygame.mouse.get_pos()[1]-(self.bs_height/2)
        x,y = self.range_escape_fix(x,y)
        x,y = self.stone_position(x,y)
        return x,y

    def save_used_coordinates(self, args):
        if self.turn == 0:
            self.used_black_coordinates.append((args[0], args[1]))
        elif self.turn == 1:
            self.used_white_coordinates.append((args[0], args[1]))
        self.sum_coordinates.add((args[0], args[1]))
    
    def draw_stone(self):
        x,y = self.mouse_position()
        if self.turn == 0:
            self.screen.blit(self.black_stone,(x,y))
        elif self.turn == 1:
            self.screen.blit(self.white_stone,(x,y))
        self.save_used_coordinates((x,y))
        

    def finish_game_mode(self,bool:bool):
        if bool== True:
            if self.turn == 0:
                print("흑의 승리입니다.")
            else:
                print("백의 승리입니다.")
            self.running = False
            
    
    def draw_possible_stone(self):
        x,y = self.mouse_position()
        if (x,y) not in self.sum_coordinates:
            return True
        else:
            return False
        
    def event_loop(self, event):
        if event.type == pygame.QUIT:
            return True
        return False

    def event_get(self):
       event = pygame.event.get()
       return event


    def mouse_click(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            return True
        else:
            return False

    def update(self):
        pygame.display.update()

    def finish(self):
        pygame.time.wait(1000)
        pygame.quit()