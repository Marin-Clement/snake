import pygame
from random import randrange

window = 750
tile_size = 50
Range = (tile_size // 2, window - tile_size // 2, tile_size)
get_random_position = lambda: [randrange(*Range), randrange(*Range)]
snake = pygame.rect.Rect([0, 0, tile_size - 2, tile_size - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 60
food = snake.copy()
food.center = get_random_position()
screen = pygame.display.set_mode([window] * 2)
clock = pygame.time.Clock()
dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dirs[pygame.K_UP]:
                snake_dir = (0, -tile_size)
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 0, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
            if event.key == pygame.K_DOWN and dirs[pygame.K_DOWN]:
                snake_dir = (0, tile_size)
                dirs = {pygame.K_UP: 0, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
            if event.key == pygame.K_LEFT and dirs[pygame.K_LEFT]:
                snake_dir = (-tile_size, 0)
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 0}
            if event.key == pygame.K_RIGHT and dirs[pygame.K_RIGHT]:
                snake_dir = (tile_size, 0)
                dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 0, pygame.K_RIGHT: 1}
    screen.fill('black')
    # check borders and self eating
    self_eating = pygame.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or self_eating:
        dirs = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
    # check food
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
    # draw food
    pygame.draw.rect(screen, "red", food)
    # draw snake
    [pygame.draw.rect(screen, 'green', segment) for segment in segments]
    # move snake
    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    pygame.display.flip()
    clock.tick(60)