import pygame, sys
from pygame.locals import *
from os import path
import math
from settings import *
# from debug import debug

class Mobject(pygame.sprite.Sprite):
    def __init__(self, image, group, topleft_pos, angle):
        super().__init__(group)

        # Current constants
        self.ORIG_IMAGE = image
        self.ORIG_WIDTH = image.get_width()
        self.ORIG_HEIGHT = image.get_height()
        self.ORIG_PIXELS = self.ORIG_WIDTH * self.ORIG_HEIGHT
        self.WRATIO = self.ORIG_HEIGHT / self.ORIG_WIDTH  # float
        self.HRATION = self.ORIG_WIDTH / self.ORIG_HEIGHT

        self.image = image      # current modified state
        self.angle = angle      # current angle        
        self.rect = self.image.get_rect(topleft = topleft_pos)

    def balloon(self, zoom = 1.2):
        current_width = self.image.get_width()
        copy = self.ORIG_IMAGE.copy()

        if current_width * zoom >= MIN_WIDTH and current_width * zoom <= MAX_WIDTH:
            return pygame.transform.rotozoom(copy, 0, self.__scale(zoom))
        else: 
            return self.image

    # Calculates scaling between original image and desired image
    def __scale(self, zoom):
        w = self.image.get_width()
        h = self.image.get_height()
        w_ratio = h / w
        h_ratio = w / h

        # Whore algebra how to scale a resolution
        w_scaled = math.sqrt((w * h * zoom) / w_ratio)
        h_scaled = math.sqrt((w * h * zoom) / h_ratio)
        px_scaled = w_scaled * h_scaled

        # More algebra to find scaling from current img to desired img
        return (self.ORIG_WIDTH ** 2) * self.WRATIO / px_scaled

    def scatter(self):
        pass



