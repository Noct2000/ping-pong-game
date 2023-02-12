import pygame
import random
from winner import Winner


class PlayScene:
    def __init__(self, display):
        self.display = display
        self.winner = None

    def show(self, max_score, is_exited):
        # Check exit menu option
        if is_exited:
            return

        # Set up window
        width = 800
        height = 600
        window = self.display.set_mode((width, height))
        self.display.set_caption("Ping-Pong Game")

        # Set up clock
        clock = pygame.time.Clock()

        # Set up font
        font = pygame.font.Font(None, 30)

        # Set up ball
        ball_width = 20
        ball_height = 20
        acceleration = -1.1
        ball_x = (width - ball_width) // 2
        ball_y = (height - ball_height) // 2
        ball_speed_x = random.choice([2, 2, 2, 2, -2, -2, -2, -2])
        ball_speed_y = random.choice([2, 2, 2, 2, -2, -2, -2, -2])

        # Set up paddles
        paddle_width = 20
        paddle_height = 120
        left_paddle_x = 0
        left_paddle_y = (height - paddle_height) // 2
        right_paddle_x = width - paddle_width
        right_paddle_y = (height - paddle_height) // 2
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
                    if right_score > left_score:
                        self.winner = Winner("right player", right_score)
                    elif left_score > right_score:
                        self.winner = Winner("left player", left_score)
                    else:
                        self.winner = None

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
            if left_paddle_y + paddle_height > height:
                left_paddle_y = height - paddle_height
            if right_paddle_y < 0:
                right_paddle_y = 0
            if right_paddle_y + paddle_height > height:
                right_paddle_y = height - paddle_height

            # Move ball
            ball_x += ball_speed_x
            ball_y += ball_speed_y

            # Handle ball collisions with walls
            if ball_y <= 0 or ball_y + ball_height >= height:
                ball_speed_y *= -1
            if ball_x <= 0:
                right_score += 1
                if right_score - max_score == 0:
                    self.winner = Winner("right player", right_score)
                    running = False
                ball_x = (width - ball_width) // 2
                ball_y = (height - ball_height) // 2
                ball_speed_x = random.choice([2, 2, 2, 2, -2, -2, -2, -2])
                ball_speed_y = random.choice([2, 2, 2, 2, -2, -2, -2, -2])
            if ball_x + ball_width >= width:
                left_score += 1
                if left_score - max_score == 0:
                    self.winner = Winner("left player", left_score)
                    running = False
                ball_x = (width - ball_width) // 2
                ball_y = (height - ball_height) // 2
                ball_speed_x = random.choice([2, 2, 2, 2, -2, -2, -2, -2])
                ball_speed_y = random.choice([2, 2, 2, 2, -2, -2, -2, -2])

            # Handle ball collisions with paddles
            if ball_x <= paddle_width and ball_y + ball_height >= left_paddle_y and ball_y <= left_paddle_y + paddle_height:
                ball_speed_x *= acceleration
            if ball_x + ball_width >= width - paddle_width and ball_y + ball_height >= right_paddle_y and ball_y <= right_paddle_y + paddle_height:
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
            window.blit(left_score_text, (width // 4, 10))
            window.blit(right_score_text, (width // 4 * 3, 10))

            # Update display
            self.display.update()

            # Tick clock
            clock.tick(60)
