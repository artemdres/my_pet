import pygame
import pygame.freetype
import seting

class Game:
    def __init__(self):
        self.okno=pygame.display.set_mode(seting.RAZRE)
        self.q=0
        
    
    
    
    
    
    
    def otrisovka(self):
        self.okno.fill([255,255,255])
    
    
    
    
    def logika(self):
        pass
    
    
    
    
    def sobitia(self):
        pass
    
    
    
    
    
    def plye(self):
        
        
    
   
        while 0==self.q:
        
            
            self.sobitia()
            self.logika()
            self.otrisovka()
              
proekt_my_pet=Game()
proekt_my_pet.plye()

