import pygame
import random

def RandomizePosition():
    return pygame.Rect((random.randint(0, AREA_WIDTH - 1) * CELL_SIZE, random.randint(0, AREA_HEIGHT - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def IsInsideSnake(rect, snake):
    isInsideSnake = False
    for cell in snake:
        if rect.colliderect(cell):
            isInsideSnake = True
            break
    return isInsideSnake

def ResetSnake():
    snake = [pygame.Rect((4 * CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE)),
         pygame.Rect((3 * CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE)),
         pygame.Rect((2 * CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE))]
    return snake

def DrawText(text, fontSize, x, y, color = (255, 255, 255)):
    font = pygame.font.SysFont('Arial', fontSize)
    textSurface = font.render(text, True, color)
    window.blit(textSurface, (x, y))

CELL_SIZE = 50
AREA_WIDTH = 15
AREA_HEIGHT = 15

pygame.init()
window = pygame.display.set_mode((CELL_SIZE * AREA_WIDTH, CELL_SIZE * AREA_HEIGHT))
pygame.display.set_caption('Snake')

direction = (1, 0)
snake = ResetSnake()

point = RandomizePosition()
pointsCollected = 0

clock = pygame.time.Clock()
timePerTick = 300 # milliseconds
timeSinceTick = 0

gameOver = False

run = True
while run:
    window.fill((0, 0, 0))

    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            toBeDirection = direction # so if the player presses something other than arrow buttons the snake doesn't just stop
            if pressed[pygame.K_UP] or pressed[pygame.K_w]:
                toBeDirection = (0, -1)
            elif pressed[pygame.K_DOWN]or pressed[pygame.K_s]:
                toBeDirection = (0, 1)
            elif pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                toBeDirection = (-1, 0)
            elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                toBeDirection = (1, 0)
            elif pressed[pygame.K_SPACE] and gameOver:
                gameOver = False
                direction = (1, 0)
                snake = ResetSnake()
                point = RandomizePosition()
                pointsCollected = 0
                timeSinceTick = 0
                pass
            elif pressed[pygame.K_ESCAPE] and gameOver:
                run = False

            # check if going that direction means going backwards
            toBePosition = (snake[0].x + (toBeDirection[0] * CELL_SIZE), snake[0].y + (toBeDirection[1] * CELL_SIZE))
            if toBePosition != (snake[1].x, snake[1].y): # only care about snake[1], because it's the only cell the player physically can't hit
                direction = toBeDirection

    # --- Ticks ---
    if timeSinceTick >= timePerTick and not gameOver:
        collectedPoint = False
        if snake[0].colliderect(point):
            snake.insert(1, snake[1].copy())

            # keep randomizing point's position until it's not spawned inside the snake
            while True:
                point = RandomizePosition()
                print(point, IsInsideSnake(point, snake))
                if not IsInsideSnake(point, snake):
                    break

            pointsCollected += 1
            collectedPoint = True

        for i in reversed(range(1, len(snake))):
            # if a point was collected just move the head and the newly inserted cell
            if not collectedPoint or i <= 1:
                snake[i].x = snake[i - 1].x
                snake[i].y = snake[i - 1].y

        snake[0].move_ip(direction[0] * CELL_SIZE, direction[1] * CELL_SIZE)

        outOfBounds = snake[0].x < 0 or snake[0].x > (AREA_WIDTH - 1) * CELL_SIZE or snake[0].y < 0 or snake[0].y > (AREA_HEIGHT - 1) * CELL_SIZE
        if outOfBounds or IsInsideSnake(snake[0], snake[1:]): # here you have to use snake[1:], because snake[0] obviously collides with itself
            for i in range(len(snake) - 1):
                snake[i] = snake[i + 1].copy()
            snake[-1].move_ip(-direction[0] * CELL_SIZE, -direction[1] * CELL_SIZE)
            gameOver = True

        timeSinceTick = 0

    elif not gameOver:
        timeSinceTick += clock.tick()

    else:
        DrawText('You collected ' + str(pointsCollected) + ' points.', 30, 15, 15)
        DrawText('Press space to restart', 30, 15, 65)
        DrawText('Press esc to quit', 30, 15, 115)

    # --- Drawing ---
    pygame.draw.rect(window, (255, 0, 0), point)
    for cell in snake[1:]:
        pygame.draw.rect(window, (0, 255, 0), cell)
    pygame.draw.rect(window, (0, 224, 0), snake[0])

    pygame.display.update()

pygame.quit()