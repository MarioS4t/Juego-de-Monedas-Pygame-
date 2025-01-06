import sys
import pygame

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Crear Texto')

white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)

#1.- Obtener Fuente
font = pygame.font.Font('freesansbold.ttf', 48)

#2.- Crear texto
text = font.render('Hola Mundo!',True,red) # superficie
rect = text.get_rect()
rect.center = (width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    surface.blit(text, rect)
    pygame.display.update()