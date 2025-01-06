import sys
import pygame

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Actuzalizar Texto')

white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)

font = pygame.font.Font('freesansbold.ttf', 48)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)
    seconds = pygame.time.get_ticks() // 1000
    text = font.render(str(seconds), True, red)
    rect = text.get_rect()
    rect.center = (width // 2, height // 2)
    surface.blit(text, rect)
    pygame.display.update()