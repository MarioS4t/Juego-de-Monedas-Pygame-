import sys
import math
import pygame
from PIL.ImageChops import offset

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Colisiones')

white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

font = pygame.font.Font('freesansbold.ttf', 48)
image1 = pygame.image.load('images/medium_circle.png')
rect1 = image1.get_rect()
rect1.center = (width // 2, height // 2)
mask_circle = pygame.mask.from_surface(image1)
image2 = pygame.image.load('images/small_rectangle.png')
rect2 = image2.get_rect()
mask_rec = pygame.mask.from_surface(image2)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)
    surface.blit(image1, rect1)
    rect2.center = pygame.mouse.get_pos()
    surface.blit(image2, rect2)
    message = 'Sin Colisión'

    offset = (rect2.x - rect1.x, rect2.y - rect1.y)
    if mask_circle.overlap(mask_rec, offset):
        message = 'Colisión!'

    text = font.render(message, True, red)
    rect3 = text.get_rect()
    rect3.midtop = (width // 2, 50)
    surface.blit(text, rect3)

    pygame.display.update()