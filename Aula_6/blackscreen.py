BLACK = (0, 0, 0)
RESOL = [800, 600]
LOOP  = True
import pygame
pygame.init()
screen = pygame.display.set_mode(RESOL)
screen.fill (BLACK)
while LOOP:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            LOOP = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                print ("esquerda")
            if e.key == pygame.K_RIGHT:
                print ("direita")
pygame.quit()
if e.type == pygame.KEYDOWN:
    if e.key == pygame.K_LEFT:
        print ("esquerda")
    if e.key == pygame.K_RIGHT:
        print ("direita")