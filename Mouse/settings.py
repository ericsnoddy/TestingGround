from os import path
from pygame.locals import *

# WIN display
WIDTH = 800
HEIGHT = 600
BG_COLOR = 'blue'

# On screen instructions
FONT = None # Pygame default font
FONT_COLOR = 'white'
FONT_BG_COLOR = BG_COLOR
ANTIALIAS = True
TOPLEFT = (20, 20)

# Min width (max determined by screen and image width)
MIN_WIDTH = 20

# Controls
key_center = K_c
key_scatter = K_s
key_scatter_all = K_a
key_inflate = K_UP
key_deflate = K_DOWN
key_inflate_max = K_PAGEUP
key_deflate_min = K_PAGEDOWN
key_CCW = K_LEFT
key_CW = K_RIGHT
key_delete = K_DELETE
key_delete_all = K_BACKSPACE
key_resurrect = K_INSERT
key_resurrect_all = K_PRINTSCREEN
key_home = K_HOME
key_home_all = K_SPACE
key_max_distance = K_END
key_pileup = K_TAB
key_downstage = K_LEFTBRACKET
key_upstage = K_RIGHTBRACKET
key_color = K_RALT
key_change = K_RSHIFT

# Images to import - requires path, topleft position, 0 <= angle < 360
IMAGE_PATHS = [
    [ path.join('graphics', 'spacefighter.png'), (350,150), 0 ],
    [ path.join('graphics', 'spacefighter.png'), (300,400), 45 ],
    [ path.join('graphics', 'spacefighter.png'), (550,210), 79 ],
    [ path.join('graphics', 'spacefighter.png'), (470,550), 270 ]
]