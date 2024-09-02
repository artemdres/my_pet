import pygame
import pygame.freetype
import seting
import dog
import statistika
import random

class Game:
    def __init__(self):
        self.okno=pygame.display.set_mode(seting.RAZRE)
        self.q=0
        self.fon=pygame.image.load("images/background.png")
        self.fon=pygame.transform.scale(self.fon, seting.RAZRE)
        self.dog=dog.Dog()
        self.manu=statistika.statistika("images/money.png", 10, 10,0)
        self.hill=statistika.statistika("images/health.png", 10,110, 100 )
        self.smail=statistika.statistika("images/happiness.png", 10, 210, 100)
        self.golod=statistika.statistika("images/satiety.png", 10, 310, 20)
        self.golodanie=pygame.USEREVENT
        pygame.time.set_timer(self.golodanie, random.randint(10000,40000) )
        self.nastroenie=pygame.USEREVENT+1
        pygame.time.set_timer(self.nastroenie, random.randint(10000, 40000))
        self.serdce=pygame.USEREVENT+2
        pygame.time.set_timer(self.serdce,random.randint(10000,40000))
    def otrisovka(self):
        self.okno.blit(self.fon, [0,0])
        self.dog.otrisovka(self.okno)
        self.manu.otrisovka(self.okno)
        self.hill.otrisovka(self.okno)
        self.smail.otrisovka(self.okno)
        self.golod.otrisovka(self.okno)
    
    
    def logika(self):
        pass
    
    
    
    
    def sobitia(self):
        spisok=pygame.event.get()
        for sobitie in spisok:
            if sobitie.type== pygame.QUIT:
                self.q=self.q+1
            if sobitie.type==pygame.MOUSEBUTTONDOWN:
                if self.dog.pramougolnik.collidepoint(sobitie.pos)==True:
                    self.manu.scet=self.manu.scet+1
            if sobitie.type==self.golodanie:
                self.golod.scet=self.golod.scet-random.randint(1,7)
            if sobitie.type==self.nastroenie:
                self.smail.scet=self.smail.scet-random.randint(1,7)
            if self.golod.scet<20:
                if sobitie.type==self.serdce:
                    self.hill.scet=self.hill.scet-random.randint(5,10)
            elif self.smail.scet<20:
                if sobitie.type==self.serdce:
                    self.hill.scet=self.hill.scet-random.randint(5,10``)
                
    
    def plye(self):
        
        
    
   
        while 0==self.q:
        
            
            self.sobitia()
            self.logika()
            self.otrisovka()
            pygame.display.update()       
              
proekt_my_pet=Game()
proekt_my_pet.plye()

