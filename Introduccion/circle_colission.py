import sys
import math
import pygame

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Colisiones')

white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

font = pygame.font.Font('freesansbold.ttf', 48)
image1 = pygame.image.load('images/medium_circle.png')
rect1 = image1.get_rect()
rect1.center = (width // 2, height // 2)

surface2 = pygame.Surface((rect1.width, rect1.height),pygame.SRCALPHA)
surface2.fill((0,0,0,50))
rect2 = surface2.get_rect()
rect2.center = rect1.center

image2 = pygame.image.load('images/medium_circle.png')
rect3 = image2.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)
    rect3.center = pygame.mouse.get_pos()
    surface.blit(image1, rect1)
    surface.blit(surface2, rect2)
    surface.blit(image2, rect3)

    message = ''
    # dist = raiz cuadrada de = x**2 + y**2
    # x = x1 - x2
    # y = y1 - y2

    pygame.draw.line(surface, black, rect1.center, rect3.center, 2)

    dist = math.hypot(rect1.x - rect3.x, rect1.y - rect3.y)
    message = 'La distancia es {}'.format(str(int(dist)))
    if dist < (64 + 64):
        message = 'Colisión!'

    text = font.render(message, True, red)
    rect4 = text.get_rect()
    rect4.midtop = (width // 2, 50)

    surface.blit(text, rect4)

    pygame.display.update()