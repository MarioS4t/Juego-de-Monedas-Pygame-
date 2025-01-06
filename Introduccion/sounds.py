import sys
import pygame

pygame.init()
width = 500
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sonidos')



white = (255,255,255)
red = (115,38,80)
green = (0,255,0)
blue = (0,0,255)

pygame.mixer.music.load('sounds/Haggstrom.mp3')
pygame.mixer.music.set_volume(1.0) # 0.0 - 1.0 Float
pygame.mixer.music.play(2, 1.30) # Reproduce la música 2 veces, a partir de 1.30 segundos

# pygame.mixer.music.play(-1, 1.30) # Reproduce la música en bucle, a partir de 1.30 segundos
# pygame.mixer.music.rewind() # Reinicia la música
# pygame.mixer.music.pause() # Pausa la música
# pygame.mixer.music.stop() # Detiene la música
# pygame.mixer.music.fadeout(5000) # Detiene la música en 5 segundos


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)
    pygame.display.update()