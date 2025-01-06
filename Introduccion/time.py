import sys
import pygame

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Obtener Tiempo')

white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    time = pygame.time.get_ticks() // 1000 # Devuelve el tiempo en milisegundos
    print(time)
    surface.fill(white)

    pygame.display.update()