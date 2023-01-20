from game import Game
from rule import Rule

g = Game()
r = Rule()

while g.running:
    for event in g.event_get():
        if g.event_loop(event):
            g.running = False
        if g.mouse_click(event):
            if g.draw_possible_stone():
                g.draw_stone()
                if g.turn == 0:
                    r.is_omok(g.mouse_position(), g.used_black_coordinates)
                else:
                    r.is_omok(g.mouse_position(),g.used_white_coordinates)
                g.finish_game_mode(r.result)
                g.turn = (g.turn+1)%2     
    g.update()
g.finish()