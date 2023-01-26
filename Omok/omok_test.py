from omok_logic import Omok_Logic

omok = Omok_Logic()
running = True

while running:
    x,y = input("x와 y를 입력해주세용 : ").split()
    x = int(x)
    y = int(y)
    if omok.possible_stone(x,y):
        omok.put_stone(x,y)
        if omok.is_omok(x,y):
            omok.result()
            running = False
        else:
            omok.change_turn()

print(omok.map)