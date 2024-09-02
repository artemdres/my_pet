import pygame

class Dog:
    def __init__ (self, ):
        
        self.kartinka=pygame.image.load("images/dog.png")
        self.kartinka=pygame.transform.scale(self.kartinka, [300, 500])
        self.pramougolnik=pygame.rect.Rect([500,250], [300,500])
    def otrisovka(self,okno ):
        okno.blit(self.kartinka, self.pramougolnik)
