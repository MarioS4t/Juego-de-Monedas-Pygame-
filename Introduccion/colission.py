import sys
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

font = pygame.font.Font('freesansbold.ttf', 48)
message = ''
rect1 = pygame.Rect(0,0,100,80)
rect1.center = (width // 2, height // 2)

rect2 = pygame.Rect(0,0,100,80)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    rect2.center = pygame.mouse.get_pos()
    surface.fill(white)
    pygame.draw.rect(surface, blue, rect2)
    pygame.draw.rect(surface, red, rect1)

    if rect1.colliderect(rect2):
        # Agregar sonido
        sound = pygame.mixer.Sound('sounds/coin.wav')
        sound.play()
        message = 'Colisión!'
    else:
        message = 'Sin Colisión'

    text = font.render(message, True, red)
    rect3 = text.get_rect()
    rect3.midtop = (width // 2, 50)
    surface.blit(text, rect3)
    pygame.display.update()