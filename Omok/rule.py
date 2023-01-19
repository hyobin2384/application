from game import Game
class Rule():
    def __init__(self, args, lst):
        self.stone_half = 29
        self.args = args
        self.x_right = args[0]
        self.x_left = args[0]
        self.y_top = args[1]
        self.y_bottom = args[1]
        self.both_side(lst)
        self.up_and_down(lst)
        self.right_diagonal(lst)
        self.left_diagonal(lst)
        

    def both_side(self, lst): 
        count = 1
        for _ in range(4):
            if ((self.x_right + self.stone_half, self.args[1])) in lst:
                count += 1
                self.x_right += self.stone_half
            else:
                break
        for _ in range(4):
            if ((self.x_left - self.stone_half, self.args[1])) in lst:
                count += 1
                self.x_left -= self.stone_half
            else:
                break

    def up_and_down(self, lst):
        count = 1
        for _ in range(4):
            if ((self.args[0], self.y_top - self.stone_half)) in lst:
                count += 1
                self.y_top -= self.stone_half
            else:
                break
        for _ in range(4):
            if ((self.args[0], self.y_bottom + self.stone_half)) in lst:
                count += 1
                self.y_bottom += self.stone_half
            else:
                break

    def right_diagonal(self, lst):
        count = 1
        for _ in range(4):
            if ((self.x_right + self.stone_half, self.y_top - self.stone_half)) in lst:
                count += 1
                self.x_right += self.stone_half
                self.y_top -= self.stone_half
            else:
                break
        for _ in range(4):
            if ((self.x_left - self.stone_half, self.y_bottom + self.stone_half)) in lst:
                count += 1
                self.x_left -= self.stone_half
                self.y_bottom += self.stone_half
            else:
                break
        
    def left_diagonal(self, lst):
        count = 1
        for _ in range(4):
            if ((self.x_left - self.stone_half, self.y_top - self.stone_half)) in lst:
                count += 1
                self.x_left -= self.stone_half
                self.y_top -= self.stone_half
            else:
                break
        for _ in range(4):
            if ((self.x_right + self.stone_half, self.y_bottom + self.stone_half)) in lst:
                count += 1
                self.x_right += self.stone_half
                self.y_bottom += self.stone_half
            else:
                break