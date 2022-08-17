import pygame, sys
from pygame.locals import *
from os import path
from debug import debug

def main():  
    WIDTH, HEIGHT = (800, 600)
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    png = modify_fighter(100)
    png_rect = png.get_rect()
    png_rect.center = WIDTH // 2, HEIGHT // 2

    running = True
    dragging = False

    orig_png = pygame.image.load(path.join('graphics', 'spacefighter.png')).convert_alpha()
    png = orig_png.copy()
    png_direction = pygame.math.Vector2(1,0)
    
    while running:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
                break
            
            elif event.type == KEYDOWN and dragging:
                mouse_pos = pygame.mouse.get_pos()
                # INFLATE
                if event.key == K_UP:
                    png = modify_fighter(orig_png, png, 20)                   
                    png_rect = png.get_rect(center = mouse_pos)

                # DEFLATE
                if event.key == K_DOWN:                    
                    png = modify_fighter(orig_png, png, -20)
                    png_rect = png.get_rect(center = mouse_pos)

                # ROTATE CCW
                if event.key == K_LEFT:
                    png = modify_fighter(png, deg = 90)
                    png_rect = png.get_rect(center = mouse_pos)

                # ROTATE CW
                if event.key == K_RIGHT:
                    png = modify_fighter(png, deg = -90)
                    png_rect = png.get_rect(center = mouse_pos)

            elif event.type == MOUSEBUTTONDOWN and not dragging:
                if png_rect.collidepoint(event.pos):
                    dragging = True

            elif event.type == MOUSEBUTTONDOWN and dragging:
                dragging = False

            elif event.type == MOUSEMOTION and dragging:
                png_rect.move_ip(event.rel)
            

        WIN.fill('black')

        #pygame.draw.rect(WIN, 'blue', png_rect)
        WIN.blit(png, png_rect)

        debug(png.get_width())

        pygame.display.update()

    pygame.quit()
    sys.exit()

def modify_fighter(orig_png = None, i = 0, deg = None):
    pass
    # aspect_ratio = img.get_height() / img.get_width()

    # if orig_width:
    #     if orig_width + i >= 40 and orig_width + i <= 400:  # Cap the scaling        
    #         img = pygame.transform.smoothscale(img, ((orig_width + i), (orig_width + i) * aspect_ratio))   
    #     else:
    #         img = pygame.transform.smoothscale(img, ((orig_width), (orig_width) * aspect_ratio))
    # if deg:
    #     img = pygame.transform.rotate(img, deg)
    # return img

main()