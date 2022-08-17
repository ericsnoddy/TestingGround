import pygame, sys
from pygame.locals import *
from settings import *
from mobject import Mobject
import random

class Field:
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Manipulable Objects')
        self.font = pygame.font.Font(FONT, 20)
        
        self.image_paths = []
        for p in IMAGE_PATHS: 
            self.image_paths.append(p)

        self.images = self.load_images()
        self.mobjects = pygame.sprite.Group()
        self.add_mobjects()
        self.clicked = pygame.sprite.Group()
        self.graveyard = pygame.sprite.Group()

    def display_instructions(self):
        info = []
        info.append("press \'" + str(pygame.key.name(key_center)) + "\' to recenter on cursor")
        # info.append("press \'" + str(pygame.key.name(key_center)) + "\' for cursor magnet")
        # info.append("press \'" + str(pygame.key.name(key_inflate)) + "\' to inflate")
        # info.append("press \'" + str(pygame.key.name(key_deflate)) + "\' to deflate")
        # info.append("press \'" + str(pygame.key.name(key_inflate_max)) + "\' to inflate maximum")
        # info.append("press \'" + str(pygame.key.name(key_deflate_min)) + "\' to deflate maximum")
        # info.append("press \'" + str(pygame.key.name(key_CW)) + "\' to rotate clockwise")
        # info.append("press \'" + str(pygame.key.name(key_CCW)) + "\' to rotate counterclockwise")
        info.append("press \'" + str(pygame.key.name(key_scatter)) + "\' to scatter")
        info.append("press \'" + str(pygame.key.name(key_scatter_all)) + "\' to scatter all")
        # info.append("press \'" + str(pygame.key.name(key_max_distance)) + "\' to send maximum distance")
        # info.append("press \'" + str(pygame.key.name(key_upstage)) + "\' to move toward background")
        # info.append("press \'" + str(pygame.key.name(key_downstage)) + "\' to move toward foreground")
        info.append("press \'" + str(pygame.key.name(key_home)) + "\' to return home")
        info.append("press \'" + str(pygame.key.name(key_home_all)) + "\' to return all to home")
        # info.append("press \'" + str(pygame.key.name(key_color)) + "\' to change color (if available)")
        # info.append("press \'" + str(pygame.key.name(key_change)) + "\' to load next image")
        info.append("press \'" + str(pygame.key.name(key_pileup)) + "\' to pile up")
        info.append("press \'" + str(pygame.key.name(key_delete)) + "\' to delete")
        info.append("press \'" + str(pygame.key.name(key_delete_all)) + "\' to delete all")
        info.append("press \'" + str(pygame.key.name(key_resurrect)) + "\' to resurrect")
        info.append("press \'" + str(pygame.key.name(key_resurrect_all)) + "\' to resurrect all")
        

            # get_linesize() includes a litte padding
        line_height = pygame.font.Font.get_linesize(self.font)

        for index, s in enumerate(info):       
            s_surf = self.font.render(s, ANTIALIAS, FONT_COLOR)
            position = (TOPLEFT[0], TOPLEFT[1] + index * line_height)
            s_rect = s_surf.get_rect(topleft = position)
            pygame.draw.rect(self.WIN, FONT_BG_COLOR, s_rect)
            self.WIN.blit(s_surf, s_rect)

    def load_images(self):
        i = []
        for p in self.image_paths:
            img = pygame.image.load(p[0]).convert_alpha()
            pos = p[1]
            ang = p[2]
            i.append(list((img, pos, ang)))
        return i

    def add_mobjects(self):
        m = []
        for i in self.images:
            m.append(Mobject(self.WIN, i[0], i[1], i[2]))
        self.mobjects.add(m)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN and self.clicked:                    
                    if event.key == key_center:
                        self.clicked.sprites()[0].rect.center = pygame.mouse.get_pos()
                    
                    if event.key == key_scatter:
                        x = random.randint(0, WIDTH - self.clicked.sprites()[0].rect.width)
                        y = random.randint(0, HEIGHT - self.clicked.sprites()[0].rect.height)
                        self.clicked.sprites()[0].move_to(x,y)
                        self.clicked.empty()

                    if event.key == key_scatter_all:
                        for mobject in self.mobjects:
                            x = random.randint(0, WIDTH - mobject.rect.width)
                            y = random.randint(0, HEIGHT - mobject.rect.height)
                            mobject.move_to(x,y)
                            self.clicked.empty()

                    if event.key == key_home:
                        self.clicked.sprites()[0].go_home()
                        self.clicked.empty()

                    if event.key == key_home_all:
                        for mobject in self.mobjects:
                            mobject.go_home()
                        self.clicked.empty()

                    if event.key == key_inflate_max:
                        if self.clicked.sprites()[0].WRATIO >= 1:
                            max = WIDTH - 50
                        else: max = HEIGHT - 50                

                    if event.key == key_delete:
                        self.graveyard.add(self.clicked.sprites()[0])
                        self.mobjects.remove(self.clicked.sprites()[0])
                        self.clicked.empty()

                    if event.key == key_delete_all:
                        for mobject in self.mobjects:
                            self.graveyard.add(mobject)
                            self.mobjects.remove(mobject)
                            self.clicked.empty()

                elif event.type == KEYDOWN and self.graveyard:
                    if event.key == key_resurrect or key_resurrect_all:
                        for mobject in self.graveyard.sprites():
                            self.mobjects.add(mobject)
                            self.graveyard.remove(mobject)
                            mobject.refresh()

                            if event.key == key_resurrect:
                                break   # run only once                                
                    # register clicks and attach mobjects    
                elif event.type == MOUSEBUTTONDOWN and len(self.clicked) == 0:
                    for mobject in self.mobjects:
                        if mobject.is_clicked(event.pos):
                            mobject.rect.center = event.pos
                            self.clicked.add(mobject)
                elif event.type == MOUSEBUTTONDOWN and len(self.clicked) == 1:
                    self.clicked.empty()
                elif event.type == MOUSEMOTION and len(self.clicked) == 1:
                    self.clicked.sprites()[0].rect.move_ip(event.rel)                    

            # get_pressed() section is to ensure holding down a key is tracked;
            keys = pygame.key.get_pressed()  

            if keys[key_inflate]:
                for mobject in self.clicked:
                    mobject.balloon('inflate')
                    mobject.rect.center = pygame.mouse.get_pos()
            if keys[key_deflate]:
                for mobject in self.clicked:
                    mobject.balloon('deflate')
                    mobject.rect.center = pygame.mouse.get_pos()

            self.WIN.fill(BG_COLOR)
            self.display_instructions()
            self.mobjects.draw(self.WIN)
            pygame.display.update()

if __name__ == '__main__':
    field = Field()
    field.run()
