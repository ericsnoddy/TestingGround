import pygame, sys
from pygame.locals import *
from settings import *
from mobject import Mobject
# from debug import debug

class Field:
    def __init__(self):
        pygame.init()
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Manipulable Objects')
        self.font = pygame.font.Font(FONT,15)
        
        self.image_paths = []
        for p in IMAGE_PATHS:       # Only supports one image for now
            self.image_paths.append(p)

        self.images = self.load_images()
        self.manipulable_objects = pygame.sprite.Group()
        self.mobjects = self.create_mobjects()
        self.current_mobject = None

    def display_instructions(self):
        info = []
        info.append(str(pygame.key.name(key_inflate)) + " to inflate")
        info.append(str(pygame.key.name(key_deflate)) + " to deflatn")
        info.append(str(pygame.key.name(key_CCW)) + " to rotate CCW")
        info.append(str(pygame.key.name(key_CW)) + " to rotate CW")
        info.append(str(pygame.key.name(key_CW)) + " to rotate CW")
        info.append(str(pygame.key.name(key_change)) + " to change color (if available)")
        info.append(str(pygame.key.name(key_change)) + " to load next image")

            # get_linesize() includes a litte padding
        line_height = pygame.font.Font.get_linesize(self.font)

        for index, s in enumerate(info):       
            s_surf = self.font.render(s, ANTIALIAS, FONT_COLOR)
            s_rect = s_surf.get_rect(topleft = TOPLEFT)
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

    def create_mobjects(self):
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
                    if event.key == key_inflate:
                        pass
                    # DEFLATE
                    if event.key == key_deflate:
                        pass
                    # ROTATE CCW
                    if event.key == key_CCW:
                        pass
                    # ROTATE CW
                    if event.key == key_CW:
                        pass
                    # CHANGE COLOR IF POSSIBLE
                    if event.key == key_color:
                        pass
                    if event.key == key_change:
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

            self.display_instructions()

            self.manipulable_objects.draw(self.WIN)

            pygame.display.update()

if __name__ == '__main__':
    field = Field()
    field.run()
