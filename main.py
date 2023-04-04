import pygame

CELL_SIZE = 50

pygame.init()
window = pygame.display.set_mode((CELL_SIZE * 15, CELL_SIZE * 15))

direction = (1, 0)
snake = [pygame.Rect((0, 0, CELL_SIZE, CELL_SIZE))]

clock = pygame.time.Clock()
timePerTick = 500 # milliseconds, so 0.5 second
timeSinceTick = 0

run = True
while run:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if timeSinceTick >= timePerTick:
        for cell in snake:
            cell.move_ip(direction[0] * CELL_SIZE, direction[1] * CELL_SIZE)
        timeSinceTick = 0

    timeSinceTick += clock.tick()
    print(timeSinceTick)

    # --- Drawing ---
    for cell in snake:
        pygame.draw.rect(window, (0, 255, 0), cell)

    pygame.display.update()

pygame.quit()