import sys
import pygame

pygame.init()
width = 400
height = 400

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hola Mundo')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()