import pygame

import os 
from pathlib import Path


os.chdir(Path(__file__).parent)

pygame.font.init()

def leader_board():
    i = 35
    column_space = 400

    head1 = font_style.render(f'PLAYER', True, yellow)
    head2 = font_style.render(f'SCORE', True, yellow)
    dis.blit(head1, [dis_width / 5, (700 / 4) + 5])
    dis.blit(head2, [dis_width / 5 + column_space, (700 / 4) + 5])
    
    cur.execute('SELECT * FROM snake_score ORDER BY score desc LIMIT 10')
    rows = cur.fetchall()
    for row in rows:
        
        column1 = font_style.render('{:>3}'.format(row[0]), True, yellow)
        column2 = font_style.render('{:30}'.format(row[1]), True, yellow)
        dis.blit(column1, [dis_width / 5, (700 / 4) + i + 5])
        dis.blit(column2, [dis_width / 5 + column_space, (700 / 4) + i + 5])

        i += 35
