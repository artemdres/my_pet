import pygame
import pygame.freetype

pygame.init()


class statistika:
    def __init__ (self, kartinka_naz, kordinata_x, kordinata_y, scet):
        self.kartinka=pygame.image.load(kartinka_naz)
        self.kartinka=pygame.transform.scale(self.kartinka, [100, 100])
        self.pramougolnik=pygame.rect.Rect([kordinata_x, kordinata_y], [100,100])
        self.text=pygame.freetype.Font("text.ttf", 40)
        self.scet=scet









    def otrisovka (self, okno):
        okno.blit(self.kartinka, self.pramougolnik)
        self.text.render_to(okno,[self.pramougolnik.x+100,self.pramougolnik.y+35], str(self.scet))