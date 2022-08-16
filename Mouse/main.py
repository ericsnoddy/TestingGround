import pygame, sys
from pygame.locals import *
from settings import *
from mobject import Mobject
from debug import debug

class Field:
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Manipulable Objects')
        
        self.image_paths = []
        for p in IMAGE_PATHS:       # Only supports one image for now
            self.image_paths.append(p)

        self.images = self.load_images()
        self.manipulable_objects = pygame.sprite.Group()
        self.mobjects = self.create_field()
        self.current_mobject = None

    def load_images(self):
        i = []
        for p in self.image_paths:
            img = pygame.image.load(p[0]).convert_alpha()
            pos = p[1]
            ang = p[2]
            i.append(list((img, pos, ang)))
        return i
    
    def create_field(self):
        m = []
        for i in self.images:
            m.append(Mobject(i[0], self.manipulable_objects, i[1], i[2]))
        return m

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN and self.current_mobject:
                    # INFLATE
                    if event.key == K_UP:
                        pass
                    # DEFLATE
                    if event.key == K_DOWN:
                        pass
                    # ROTATE CCW
                    if event.key == K_LEFT:
                        pass
                    # ROTATE CW
                    if event.key == K_RIGHT:
                        pass
                elif not self.current_mobject:
                    if event.type == MOUSEBUTTONDOWN:
                        for m in self.mobjects:
                            if m.rect.collidepoint(event.pos):
                                self.current_mobject = m
                elif self.current_mobject:
                    if event.type == MOUSEBUTTONDOWN:
                        self.current_mobject = None
                    elif event.type == MOUSEMOTION:
                        self.current_mobject.rect.move_ip(event.rel)

            self.WIN.fill(BG_COLOR)

            for m in self.mobjects: self.WIN.blit(m.image, m.rect)

            pygame.display.update()

if __name__ == '__main__':
    field = Field()
    field.run()
