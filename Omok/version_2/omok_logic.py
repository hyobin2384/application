class Omok_logic():
    def __init__(self):
        self.turn = 0
        self.map = [[-1] * 19 for _ in range(19)]

    def inable_draw(self, x,y):
        if self.map[[y][x]] == -1:
            return True
        else:
            return False

    def draw(self, x, y):
        if self.inable_draw():
            self.map[[y][x]] == self.turn
    
    def turn_chage(self):
        self.turn = (self.turn)%2

    
    def is_omok(self, x, y):
        dir = [(0,1), (1,0), (1,1), (-1,1)]
        
    def is_check(self, x, y):
        dir = [(0,1), (1,0), (1,1), (-1,1)]
        count = 0

        for i in range(4):
            dx, dy = dir[i]
        self.map[y+dy*1][x+dx*1]


    def result(self):
        ...



