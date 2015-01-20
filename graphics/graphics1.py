import os.path, sys
import random
import pygame
from pygame.locals import *


class Object(pygame.sprite.Sprite):
    def __init__(self, img, cX, cY):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(img, -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.cX = cX
        self.cY = cY
        self.coord = (cX, cY)


class Car(Object):
    def __init__(self, cX, cY):
        Cars.__init__(self, "ñar.bmp", cX, cY)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def draw_background():
    screen = pygame.display.get_surface()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    back, back_rect = load_image("set.jpg")
    screen.blit(back, (0, 0))
    pygame.display.flip()
    return back


def action(bk):
    cars_list = [] 
    screen = pygame.display.get_surface()
    car1 = Car(10,10)
    cars_list.append(car)
    cars = pygame.sprite.RenderPlain(creatures_list)
 
    while 1:
        input(pygame.event.get())
        screen.blit(bk, (0, 0))
        cars.update()
        cars.draw(screen)
        pygame.display.flip()

 
def init_window():
    pygame.init()
    window = pygame.display.set_mode((550, 480))
    pygame.display.set_caption('Project: Cars')
 

def input(events):
    for event in events:
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        else:
            pass 
 

def main():
    init_window()
    bk = draw_background()
    action(bk)    
 
if __name__ == '__main__': main()