class Omok_Logic:
    def __init__(self):
        self.turn = 0
        self.map = [[-1]*19 for _ in range(19)]
    
    def range_check(self,x,y):
        if x > len(self.map) or y > len(self.map):
            return False
        if x < 0 or y < 0:
            return False
        return True

    def _is_check(self,x,y,dx,dy):
        count = 0
        for _ in range(4):
            x = x+(dx*1)
            y = y+(dy*1)
            if self.map[y][x] == self.turn:
                count += 1
            if self.range_check(x,y) == False:
                break
        return count

    def is_omok(self,x,y):
        dir = [(1,0),(0,1),(1,1),(-1,1)]
        for dx,dy in dir:
            a_count = self._is_check(x,y,dx,dy)
            b_count = self._is_check(x,y,-dx,-dy)
            if a_count+b_count >= 4:
                return True

    def possible_stone(self,x,y):
        if self.range_check(x,y) == False:
            return False
        if self.map[y][x] == -1:
            return True
        else:
            return False
    
    def change_turn(self):
        self.turn = (self.turn+1)%2

    def put_stone(self,x,y):
        self.map[y][x] = self.turn

    def result(self):
        if self.turn == 0:
            print("흑이 승리하였습니다.")
        elif self.turn == 1:
            print("백이 승리하였습니다.")