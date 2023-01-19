class Checker():

    def __init__(self):
        self.strike = 0
        self.ball = 0
        self.out = 0

    def check_number(self, number) -> str:
        if len(set(number)) != 4:
            raise Exception('중복된 수를 사용하였습니다.')

        for i in range(4):
            if number[i] not in "0123456789":
                raise Exception('범위안에 있는 숫자를 입력해주세요')
            

    def check_score(self, predict, enemy) -> str:
        for i in range(4):
            if predict[i] == enemy[i]:
                self.strike += 1
            elif predict[i] in enemy:
                self.ball += 1
            else:
                self.out += 1