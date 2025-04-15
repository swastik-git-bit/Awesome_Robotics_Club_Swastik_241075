

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Enhanced Snake Game')

# Font
font = pygame.font.SysFont(None, 35)

# Clock
clock = pygame.time.Clock()

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def message(msg, color, y_offset=0):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH / 6, HEIGHT / 3 + y_offset])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2
    dx, dy = 0, 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Power-up initialization
    power_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    power_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    power_active = False
    power_timer = 0

    score = 0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You lost! Press Q to Quit or R to Restart", RED, 0)
            message(f"Score: {score}", WHITE, 40)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        x += dx
        y += dy

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BLACK)

        # Draw food and power-up
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        if not power_active:
            pygame.draw.rect(screen, BLUE, [power_x, power_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        if snake_head in snake[:-1]:
            game_close = True

        draw_snake(snake)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

        pygame.display.update()

        # Food eaten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1
            score += 1

        # Power-up eaten
        if x == power_x and y == power_y:
            power_active = True
            power_timer = pygame.time.get_ticks()
            power_x, power_y = -100, -100  # Hide the power-up off-screen

        # Power-up duration and speed control
        speed = 10
        if power_active:
            if pygame.time.get_ticks() - power_timer < 5000:
                speed = 20  # speed boost
            else:
                power_active = False
                # Respawn power-up
                power_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                power_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

        clock.tick(speed)

    pygame.quit()
    quit()

# Run the game
game_loop()
