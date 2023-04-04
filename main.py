import pygame

CELL_SIZE = 50

pygame.init()
window = pygame.display.set_mode((CELL_SIZE * 15, CELL_SIZE * 15))

direction = (1, 0)
snake = [pygame.Rect((2 * CELL_SIZE, 0, CELL_SIZE, CELL_SIZE)),
         pygame.Rect((CELL_SIZE, 0, CELL_SIZE, CELL_SIZE)),
         pygame.Rect((0, 0, CELL_SIZE, CELL_SIZE))]

clock = pygame.time.Clock()
timePerTick = 500 # milliseconds, so 0.5 second
timeSinceTick = 0

run = True
while run:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP] and direction != (0, 1):
                direction = (0, -1)
            elif pressed[pygame.K_DOWN] and direction != (0, -1):
                direction = (0, 1)
            elif pressed[pygame.K_LEFT] and direction != (1, 0):
                direction = (-1, 0)
            elif pressed[pygame.K_RIGHT] and direction != (-1, 0):
                direction = (1, 0)

    if timeSinceTick >= timePerTick:
        for i in reversed(range(1, len(snake))):
            snake[i].x = snake[i - 1].x
            snake[i].y = snake[i - 1].y

        snake[0].move_ip(direction[0] * CELL_SIZE, direction[1] * CELL_SIZE)

        timeSinceTick = 0

    timeSinceTick += clock.tick()

    # --- Drawing ---
    for cell in snake:
        pygame.draw.rect(window, (0, 255, 0), cell)

    pygame.display.update()

pygame.quit()