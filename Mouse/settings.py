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

# Min and Max
MIN_WIDTH = 40
MAX_WIDTH = 600

# Controls
key_inflate = K_UP
key_deflate = K_DOWN
key_CCW = K_LEFT
key_CW = K_RIGHT
key_color = K_SPACE
key_change = K_BACKSPACE

# Images to import - requires path, topleft position, 0 <= angle < 360
IMAGE_PATHS = [
    [ path.join('graphics', 'spacefighter.png'), (50,150), 0 ],
    [ path.join('graphics', 'spacefighter.png'), (100,200), 45 ],
    [ path.join('graphics', 'spacefighter.png'), (250,210), 79 ],
    [ path.join('graphics', 'spacefighter.png'), (470,50), 270 ]
]