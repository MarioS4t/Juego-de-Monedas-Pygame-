import sys
import pygame

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Eventos del Mouse')

white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('Click izquierdo')
            if event.button == 2:
                print('Click centro')
            if event.button == 3:
                print('Click derecho')
            if event.button == 4:
                print('Rueda arriba')
            if event.button == 5:
                print('Rueda abajo')



        if event.type == pygame.MOUSEBUTTONUP:
            #print('Mouse liberado')
            pass

    surface.fill(white)
    pygame.display.update()