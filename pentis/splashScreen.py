import os
import sys
import pygame as pg
import inoutput as io
from inoutput import imageStart
from utils import screen, screen_width, screen_height, clock
import colors as clr

DURATION_MS = 2000
VERSION     = "v0.9"

_LOGO_FONT_PATH = "graphics\\Russo_One.ttf" if os.name == 'nt' else "graphics/Russo_One.ttf"

_logo_font    = pg.font.Font(_LOGO_FONT_PATH, int(screen_height * 0.09))
_loading_font = io.get_font(int(screen_height * 0.03))
_version_font = io.get_font(int(screen_height * 0.022))

_BAR_W = int(screen_width * 0.243)
_BAR_H = int(screen_height * 0.022)
_BAR_X = (screen_width - _BAR_W) // 2
_BAR_Y = int(screen_height * 0.889)


def splashScreen(screen):
    start = pg.time.get_ticks()
    progress = 0.0

    while progress < 1.0:
        progress = min(1.0, (pg.time.get_ticks() - start) / DURATION_MS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

        screen.blit(imageStart, (0, 0))

        logo_surf = _logo_font.render("PENTIS", True, clr.purple)
        screen.blit(logo_surf, logo_surf.get_rect(center=(screen_width // 2, int(screen_height * 0.71))))

        loading_surf = _loading_font.render(io.t("splash", "loading"), True, clr.gry1)
        screen.blit(loading_surf, loading_surf.get_rect(center=(screen_width // 2, int(screen_height * 0.838))))

        pg.draw.rect(screen, clr.gry3, (_BAR_X, _BAR_Y, _BAR_W, _BAR_H), border_radius=_BAR_H // 2)
        fill_w = int(_BAR_W * progress)
        if fill_w > 0:
            pg.draw.rect(screen, clr.purple, (_BAR_X, _BAR_Y, fill_w, _BAR_H), border_radius=_BAR_H // 2)

        version_surf = _version_font.render(VERSION, True, clr.gry2)
        screen.blit(version_surf, version_surf.get_rect(center=(screen_width // 2, int(screen_height * 0.941))))

        pg.display.flip()
        clock.tick(60)
