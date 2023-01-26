class Omok_game:
    def __init__(self):
        self.one_space = 29

    def adjust_position(self,x,y):
        if (x%self.one_space) > self.one_space//2:
            x = x + (self.one_space- (x%self.one_space))
        elif (x%self.one_space) <= self.one_space//2:
            x = x - (x%self.one_space)

        if (y%self.one_space) > self.one_space//2:
            y = y + (self.one_space - (y%self.one_space))
        elif (y%self.one_space) <= self.one_space//2:
            y = y - (y%self.one_space)
        return x,y 