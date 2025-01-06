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

surface2 = pygame.Surface( (200, 200) )
surface2.fill(green)

rect = surface2.get_rect()
rect.center = (width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    surface.blit(surface2, rect)
    pygame.draw.rect(surface2,red, (100,50,80,40))

    pygame.display.update()