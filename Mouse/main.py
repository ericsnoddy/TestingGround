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

    def load_images(self):
        i = []
        for p in self.image_paths:
            i.append(pygame.image.load(p).convert_alpha())
        return i
    
    def create_field(self):
        m = []
        for i in self.images:
            m.append(Mobject(i, self.manipulable_objects))
        return m

    def run(self):

        running = True
        current_mobject = None

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEBUTTONDOWN and not current_mobject:
                    for m in self.mobjects:
                        if m.rect.collidepoint(event.pos):
                            current_mobject = m
                elif event.type == MOUSEBUTTONDOWN and current_mobject:
                    current_mobject = None
                elif event.type == MOUSEMOTION and current_mobject:
                    current_mobject.rect.move_ip(event.rel)

            self.WIN.fill(BG_COLOR)

            for m in self.mobjects:
                self.WIN.blit(m.image, m.rect)
                
            pygame.display.update()

if __name__ == '__main__':
    field = Field()
    field.run()
