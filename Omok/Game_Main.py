# 인터페이스 상속
from Mygame import Mygame
from MyPygame import MyPygame
from omok_logic import Omok_Logic
from omok_game import Omok_game

class Game_Main:
    def __init__(self, mypygame:Mygame):
        self.mypygame = mypygame
        self.running = True
        self.screen_width = 549
        self.screen_height = 549
        self.screen = mypygame.screen_set(self.screen_width,self.screen_height)
        mypygame.screen_name("omok")
        self.background = mypygame.image_load("Omok/image/Omoktable.PNG")
        self.black_stone = mypygame.image_load("Omok/image/black.png")
        self.white_stone = mypygame.image_load("Omok/image/white.png")
        mypygame.color_transparents(self.black_stone,181,230,29)
        mypygame.color_transparents(self.white_stone,181,230,29)
        self.stone_width,self.stone_height = mypygame.get_size(self.black_stone)
        mypygame.bilt(self.screen,self.background,0,0)

        self.logic = Omok_Logic()
        self.game = Omok_game()

    def run(self):
        while self.running:
            for event in self.mypygame.event_get():
                if self.mypygame.event_occur(event) == "quit":
                    self.running = False
                elif self.mypygame.event_occur(event) == "mouse":
                    x,y = self.mypygame.max_min_click_range(self.mypygame.mouse_click_pos(),self.screen_width-12)
                    x,y = self.game.adjust_position(x,y)
                    if self.logic.possible_stone(x//29,y//29):
                        self.logic.put_stone(x//29,y//29)
                        if self.logic.turn == 0:
                            self.mypygame.bilt(self.screen,self.black_stone,x,y)
                        else:
                            self.mypygame.bilt(self.screen,self.white_stone,x,y)
                        if self.logic.is_omok(x//29,y//29):
                            self.logic.result()
                            self.running = False
                        else:
                            self.logic.change_turn()
            self.mypygame.update()
        self.mypygame.finish()

main = Game_Main(MyPygame())
main.run()
