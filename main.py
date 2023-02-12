import pygame
import random

# Initialize Pygame
pygame.init()

# Set up window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong Game")

# Set up clock
clock = pygame.time.Clock()

# Set up font
font = pygame.font.Font(None, 30)

# Set up ball
ball_width = 20
ball_height = 20
acceleration = -1.1
ball_x = (WIDTH - ball_width) // 2
ball_y = (HEIGHT - ball_height) // 2
ball_speed_x = random.choice([2, 2, 2, 2, -2, -2, -2, -2])
ball_speed_y = random.choice([2, 2, 2, 2, -2, -2, -2, -2])

# Set up paddles
paddle_width = 20
paddle_height = 120
left_paddle_x = 0
left_paddle_y = (HEIGHT - paddle_height) // 2
right_paddle_x = WIDTH - paddle_width
right_paddle_y = (HEIGHT - paddle_height) // 2
paddle_speed = 5

# Set up scores
left_score = 0
right_score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle paddle movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s]:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP]:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        right_paddle_y += paddle_speed

    # Ensure paddles stay within window
    if left_paddle_y < 0:
        left_paddle_y = 0
    if left_paddle_y + paddle_height > HEIGHT:
        left_paddle_y = HEIGHT - paddle_height
    if right_paddle_y < 0:
        right_paddle_y = 0
    if right_paddle_y + paddle_height > HEIGHT:
        right_paddle_y = HEIGHT - paddle_height

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Handle ball collisions with walls
    if ball_y <= 0 or ball_y + ball_height >= HEIGHT:
        ball_speed_y *= -1
    if ball_x <= 0:
        right_score += 1
        ball_x = (WIDTH - ball_width) // 2
        ball_y = (HEIGHT - ball_height) // 2
        ball_speed_x = random.choice([2, 2, 2, 2, -2, -2, -2, -2])
        ball_speed_y = random.choice([2, 2, 2, 2, -2, -2, -2, -2])
    if ball_x + ball_width >= WIDTH:
        left_score += 1
        ball_x = (WIDTH - ball_width) // 2
        ball_y = (HEIGHT - ball_height) // 2
        ball_speed_x = random.choice([2, 2, 2, 2, -2, -2, -2, -2])
        ball_speed_y = random.choice([2, 2, 2, 2, -2, -2, -2, -2])

    # Handle ball collisions with paddles
    if ball_x <= paddle_width and ball_y + ball_height >= left_paddle_y and ball_y <= left_paddle_y + paddle_height:
        ball_speed_x *= acceleration
    if ball_x + ball_width >= WIDTH - paddle_width and ball_y + ball_height >= right_paddle_y and ball_y <= right_paddle_y + paddle_height:
        ball_speed_x *= acceleration

    # Clear window
    window.fill((0, 0, 0))

    # Draw ball
    pygame.draw.rect(window, (255, 255, 255), (ball_x, ball_y, ball_width, ball_height))

    # Draw paddles
    pygame.draw.rect(window, (255, 255, 255), (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, (255, 255, 255), (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    # Draw scores
    left_score_text = font.render(str(left_score), True, (255, 255, 255))
    right_score_text = font.render(str(right_score), True, (255, 255, 255))
    window.blit(left_score_text, (WIDTH // 4, 10))
    window.blit(right_score_text, (WIDTH // 4 * 3, 10))

    # Update display
    pygame.display.update()

    # Tick clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
