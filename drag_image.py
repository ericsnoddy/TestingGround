import pygame, sys
from pygame.locals import *
from os import path

def main():  
    WIDTH, HEIGHT = (800, 600)
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    png = modify_fighter(100)
    png_rect = png.get_rect()
    png_rect.center = WIDTH // 2, HEIGHT // 2

    running = True
    dragging = False

    while running:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
                break
            
            elif event.type == KEYDOWN and dragging:
                mouse_pos = pygame.mouse.get_pos()
                # INFLATE
                if event.key == K_UP:
                    png = modify_fighter(png.get_width(), 20)                   
                    png_rect = png.get_rect(center = mouse_pos)

                # DEFLATE
                if event.key == K_DOWN:                    
                    png = modify_fighter(png.get_width(), -20)
                    png_rect = png.get_rect(center = mouse_pos)

                # ROTATE CCW
                if event.key == K_LEFT:
                    png = modify_fighter(deg = 90)
                    png_rect = png.get_rect(center = mouse_pos)

                # ROTATE CW
                if event.key == K_RIGHT:
                    png = modify_fighter(deg = -90)
                    png_rect = png.get_rect(center = mouse_pos)

            elif event.type == MOUSEBUTTONDOWN and not dragging:
                if png_rect.collidepoint(event.pos):
                    dragging = True

            elif event.type == MOUSEBUTTONDOWN and dragging:
                dragging = False

            elif event.type == MOUSEMOTION and dragging:
                png_rect.move_ip(event.rel)
            
            # if event.type == MOUSEBUTTONDOWN and dragging:
            #     dragging = False
            #     png_rect.move_ip(event.pos)
                

        WIN.fill('black')

        #pygame.draw.rect(WIN, 'blue', png_rect)
        WIN.blit(png, png_rect)

        pygame.display.update()

    pygame.quit()
    sys.exit()

# TOTALLY BROKEN
# 

# orig_width to be adjusted, i = increment to inflate, deg = deg to rotate
# None + i = 0 throws error
def modify_fighter(orig_width = None, i = 0, deg = None):
    img = pygame.image.load(path.join('graphics', 'spacefighter.png')).convert_alpha()
    aspect_ratio = img.get_height() / img.get_width()

    if orig_width:
        if orig_width + i >= 40 and orig_width + i <= 400:  # Cap the scaling        
            img = pygame.transform.smoothscale(img, ((orig_width + i), (orig_width + i) * aspect_ratio))   
        else:
            img = pygame.transform.smoothscale(img, ((orig_width), (orig_width) * aspect_ratio))
    if deg:
        img = pygame.transform.rotate(img, deg)
    return img

main()