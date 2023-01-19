import game
import checker

g = game.Game()
c = checker.Checker()

while True:
    print("숫자 야구 게임을 시작합니다.(4가지 수를 예측해야합니다.)")
    g.enemy_generate()
    g.predict_enemy_value()
    