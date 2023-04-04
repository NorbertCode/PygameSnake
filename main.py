import pygame

CELL_SIZE = 50

pygame.init()
window = pygame.display.set_mode((CELL_SIZE * 15, CELL_SIZE * 15))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()