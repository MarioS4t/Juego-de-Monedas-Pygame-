import sys
import pygame

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Posicion del Mouse')

font = pygame.font.Font('freesansbold.ttf', 48)


white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pos_x, pos_y = pygame.mouse.get_pos() # Devuelve una tupla con las coordenadas del mouse
    messa = f'x: {pos_x} y: {pos_y}'
    text = font.render(messa, True, red)
    rect = text.get_rect()
    rect.center = (width // 2, height // 2)
    surface.fill(white)
    surface.blit(text, rect)
    pygame.display.update()