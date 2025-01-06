import sys
import pygame

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Imagenes')

white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)

image = pygame.image.load('images/small_rectangle.png') # Superficie
rect = image.get_rect()
rect.center = (width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    surface.blit(image, rect)
    pygame.display.update()