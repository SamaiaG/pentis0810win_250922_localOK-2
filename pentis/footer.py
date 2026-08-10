import inoutput as io
import colors as clr

DEFAULT_COLOR = (0,0,0)


class Footer:

    BOTTOM_SPACE  = 24
    SIDE_SPACE    = 48
    REF_HEIGHT    = 864   # 1080p scaled by monitor_size90's 0.8 factor
    REF_FONT_SIZE = 20    # font size this component should look like at REF_HEIGHT

    def __init__(self, screen, screen_width, screen_height, font=None):
        self.screen        = screen
        font_size          = max(1, round(screen_height * self.REF_FONT_SIZE / self.REF_HEIGHT))
        self.font          = font or io.get_font(font_size)
        self.screen_width  = screen_width
        self.screen_height = screen_height
        self.line_gap      = self.font.get_linesize() + 6

    def _draw_lines(self, lines, align):
        y = self.screen_height - self.BOTTOM_SPACE - len(lines) * self.line_gap
        surfaces = [self.font.render(line, True, color) for line, color in lines]
        if align == "left":
            x = self.SIDE_SPACE
            for surf in surfaces:
                self.screen.blit(surf, (x, y))
                y += self.line_gap
        elif align == "center":
            for surf in surfaces:
                self.screen.blit(surf, (self.screen_width // 2 - surf.get_width() // 2, y))
                y += self.line_gap
        else:
            max_w = max((surf.get_width() for surf in surfaces), default=0)
            x = self.screen_width - self.SIDE_SPACE - max_w
            for surf in surfaces:
                self.screen.blit(surf, (x, y))
                y += self.line_gap

    def draw(self, mode_str=None, diff_str=None, username=None, warn_str=None,
             help_str=None, back_str=None, center_str=None):
        left = []
        if mode_str:
            left.append((mode_str, DEFAULT_COLOR))
        if diff_str:
            left.append((diff_str, DEFAULT_COLOR))
        if username:
            left.append((username, DEFAULT_COLOR))
        elif warn_str:
            left.append((warn_str, clr.red3))
        if left:
            self._draw_lines(left, "left")

        right = []
        if help_str:
            right.append((help_str, DEFAULT_COLOR))
        if back_str:
            right.append((back_str, DEFAULT_COLOR))
        if right:
            self._draw_lines(right, "right")

        if center_str:
            self._draw_lines([(center_str, DEFAULT_COLOR)], "center")
