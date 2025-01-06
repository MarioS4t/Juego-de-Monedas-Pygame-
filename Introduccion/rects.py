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

# pygame.Rect(posX, posY, width, height)
rect = pygame.Rect(100, 150, 120, 60)
#rect.center = (x , y)
rect.center = (width // 2 , height // 2)
print(rect.x)
print(rect.y)

rect2 = pygame.Rect(100, 100, 80, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    # pygame.draw.rect(Superficie,color,rectagulo)
    pygame.draw.rect(surface, red, rect)
    pygame.draw.rect(surface, green, rect2)
    pygame.display.update()