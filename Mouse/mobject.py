import pygame, sys
from pygame.locals import *
from os import path
from debug import debug

class Mobject(pygame.sprite.Sprite):
    def __init__(self, image, group, topleft_pos = (100,100), angle = 0):
        super().__init__(group)

        self.image_orig = image
        self.width_orig = image.get_width()
        self.height_orig = image.get_height()
        self.image = image.copy()
        self.angle = angle      
        self.ratio = self.image.get_height() / self.image.get_width()
        self.rect = self.image.get_rect(topleft = topleft_pos)

    def balloon(self, zoom = 10):
        pass
