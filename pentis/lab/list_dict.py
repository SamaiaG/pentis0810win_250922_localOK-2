
import pygame as pg
list1 = []
def listfunc(a,b):
    list1.append(a)
    list1.append(b)
    r1 = list1.pop(1)
    return r1

nmbr = listfunc(1,2)
if len(list1) <= 1:
    print(nmbr)

#list1.sort()

game_keys = {
    0: "Left", 10: pg.K_LEFT,
    1: "Right", 11: pg.K_RIGHT,
    2: "Down", 12: pg.K_DOWN,
    3: "Rotate CCW", 13: pg.K_y,
    4: "Rotate CW", 14: pg.K_x,
    5: "Rotate 180°", 15: pg.K_a,
    6: "Smash", 16: pg.K_SPACE,
}
game_keys_len = 7
for i in range(game_keys_len):
    print(pg.key.name(game_keys[i+10]))
    key_pair = game_keys[i], pg.key.name(game_keys[i+10])
    print(key_pair)

print(game_keys[10]) 