import pygame
from os import path
from .constants import *

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.king = False
        crown_path = path.join('checkers', 'assets', 'crown.png')
        crown_img = pygame.image.load(crown_path).convert_alpha()
        self.crown = pygame.transform.scale(crown_img, (44, 25))

        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):
        self.x = TILESIZE * self.col + TILESIZE // 2
        self.y = TILESIZE * self.row + TILESIZE // 2

    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()

    def draw(self, win):
        radius = TILESIZE // 2 - PIECE_PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + PIECE_OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(self.crown, (self.x - self.crown.get_width()//2, self.y - self.crown.get_height()//2))

    def __repr__(self):
        return str(self.color)
