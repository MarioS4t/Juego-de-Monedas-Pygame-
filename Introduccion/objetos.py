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
    # draw
    # 1. Donde se va a dibujar
    # 2. Color
    # 3. Figura
    pygame.draw.rect(surface, red, (100, 100, 80, 40))
    pygame.draw.circle(surface, green, (200, 300), 100)
    pygame.draw.line(surface, blue, (100, 100), (200, 300), 2 )
    pygame.display.update()