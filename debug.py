import pygame
pygame.init()

# Attributes
BG_COLOR = (0,0,0)
FONT_COLOR = (255,255,255)
DEFAULT_X, DEFAULT_Y = (10,10)
FONT = None  # None for pygame default font
ANTIALIAS = True

# This method converts the input to a string and displays it
# as a rect at position topleft = (x,y), default included

f = pygame.font.Font(FONT,30)

def debug(info, x = DEFAULT_X, y = DEFAULT_Y):    
    display_surf = pygame.display.get_surface()
    debug_surf = f.render(str(info), ANTIALIAS, FONT_COLOR)
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surf, BG_COLOR, debug_rect)
    display_surf.blit(debug_surf, debug_rect)