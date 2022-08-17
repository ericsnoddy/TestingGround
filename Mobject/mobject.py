import pygame
from pygame.locals import *
import random

class Mobject(pygame.sprite.Sprite):
    def __init__(self, display_surf, image, topleft_pos, angle):
        super().__init__()

        self.display_surf = display_surf

        # 'constants' - do not alter variables
        self.ORIG_IMAGE = image
        self.ORIG_TOP = topleft_pos[0]
        self.ORIG_LEFT = topleft_pos[1]
        self.ORIG_WIDTH = image.get_width()
        self.ORIG_HEIGHT = image.get_height()
        self.ORIG_PIXELS = self.ORIG_WIDTH * self.ORIG_HEIGHT
        self.WRATIO = self.ORIG_HEIGHT / self.ORIG_WIDTH  # float
        self.HRATIO = self.ORIG_WIDTH / self.ORIG_HEIGHT
        self.BOTTOM_LIMIT = self.display_surf.get_height() - self.ORIG_HEIGHT
        self.RIGHT_LIMIT = self.display_surf.get_width() - self.ORIG_WIDTH
        self.ORIG_ANGLE = angle

        self.image = image      # current modified state
        self.angle = angle      # current angle        
        self.rect = self.image.get_rect(topleft = topleft_pos)

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def move_to(self, x, y):
        self.rect.update(x, y, self.rect.width, self.rect.height)

    def go_home(self):
        self.rect.update(self.ORIG_TOP, self.ORIG_LEFT, self.rect.width, self.rect.height)

    def refresh(self):
        self.image = self.ORIG_IMAGE
        self.angle = self.ORIG_ANGLE
        self.rect = self.image.get_rect(topleft = (self.ORIG_TOP, self.ORIG_LEFT))

    def balloon(self, flux):
        if flux == 'inflate':
            px = 5
        else: px = -5

        w_now = self.image.get_width()

        w_want = w_now + px
        h_want = w_want * self.WRATIO
        
        if w_want <= self.display_surf.get_width() - 100 and h_want <= self.display_surf.get_height() - 100:
            if w_want >= 40 and h_want >= 5:
                self.image = pygame.transform.scale(self.ORIG_IMAGE, (w_want, h_want))
                self.rect = self.image.get_rect(center = self.rect.center)
