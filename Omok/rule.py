class Rule():
    def __init__(self):
        self.result = False
        self.stone_half = 29

    def is_omok(self, args, lst):
        x_right = args[0]
        x_left = args[0]
        y_top = args[1]
        y_bottom = args[1]
        
        # both_side 
        count = 1
        for _ in range(4):
            if ((x_right + self.stone_half, args[1])) in lst:
                count += 1
                x_right += self.stone_half
            else:
                break
        for _ in range(4):
            if ((x_left - self.stone_half, args[1])) in lst:
                count += 1
                x_left -= self.stone_half
            else:
                break
        if count == 5:
            self.result = True

        # up and down
        count = 1
        for _ in range(4):
            if ((args[0], y_top - self.stone_half)) in lst:
                count += 1
                y_top -= self.stone_half
            else:
                break
        for _ in range(4):
            if ((args[0], y_bottom + self.stone_half)) in lst:
                count += 1
                y_bottom += self.stone_half
            else:
                break
        if count == 5:
            self.result = True

        # right_diagonal
        count = 1
        for _ in range(4):
            if ((x_right + self.stone_half, y_top - self.stone_half)) in lst:
                count += 1
                x_right += self.stone_half
                y_top -= self.stone_half
            else:
                break
        for _ in range(4):
            if ((x_left - self.stone_half, y_bottom + self.stone_half)) in lst:
                count += 1
                x_left -= self.stone_half
                y_bottom += self.stone_half
            else:
                break
        if count == 5:
            self.result = True
        
        # left_diagonal
        count = 1
        for _ in range(4):
            if ((x_left - self.stone_half, y_top - self.stone_half)) in lst:
                count += 1
                x_left -= self.stone_half
                y_top -= self.stone_half
            else:
                break
        for _ in range(4):
            if ((x_right + self.stone_half, y_bottom + self.stone_half)) in lst:
                count += 1
                x_right += self.stone_half
                y_bottom += self.stone_half
            else:
                break
        if count == 5:
            self.result = True