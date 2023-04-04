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
            toBeDirection = direction # so if the player presses something other than arrow buttons the snake doesn't just stop
            if pressed[pygame.K_UP]:
                toBeDirection = (0, -1)
            elif pressed[pygame.K_DOWN]:
                toBeDirection = (0, 1)
            elif pressed[pygame.K_LEFT]:
                toBeDirection = (-1, 0)
            elif pressed[pygame.K_RIGHT]:
                toBeDirection = (1, 0)

            # check if going that direction means going backwards
            toBePosition = (snake[0].x + (toBeDirection[0] * CELL_SIZE), snake[0].y + (toBeDirection[1] * CELL_SIZE))
            if toBePosition != (snake[1].x, snake[1].y): # only care about snake[1], because it's the only cell the player physically can't hit
                direction = toBeDirection

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