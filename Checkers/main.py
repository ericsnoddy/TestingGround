import pygame, sys
from pygame.locals import *
from checkers.constants import WIDTH, HEIGHT, TILESIZE
from checkers.board import Board
from checkers.game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    running = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                row, col = get_row_col(pygame.mouse.get_pos())

        game.update()      
        pygame.display.update()        

    pygame.quit()
    sys.exit()

def get_row_col(pos):
    x, y = pos
    row = y // TILESIZE
    col = x // TILESIZE
    return row, col
    
main()