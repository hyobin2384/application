import random
import checker

class Game():

    def __init__(self):
        self.enemy = []
        self.predict = []
    
    def enemy_generate(self) -> str:
        temp_list = ""
        count = 1
        while True:
            temp = str(random.randrange(0,10))
            if len(set(temp_list + temp)) != count:
                continue
            temp_list += temp
            count += 1
            if count == 5:
                break
        self.enemy = temp_list
    
    def predict_enemy_value(self):
        predict_value = input(f"숫자를 예측해주세요 : ")
        self.predict = predict_value

    def result_notice(self):
        c = checker.Checker(self.predict, self.enemy)
        strike, ball, out = c.check_score()

        print(f"{strike} strike, {ball} ball, {out} out")
        if strike == 4:
            print("승리하셨습니다.")