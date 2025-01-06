import sys
import pygame

pygame.init()
width = 400
height = 400

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rectangulos')

white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    #pygame.draw.polygon(surface, green, ((x,y), (x,y), (x,y)))
    pygame.draw.polygon(surface, green, ((0, 400), (100, 300), (200, 400)))
    pygame.draw.polygon(surface, red, (
        (146,0),
        (291,106),
        (236,277),
        (56,277),
        (0,106)))
    pygame.display.update()