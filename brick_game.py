import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 0.1
PADDLE_SPEED = 1
WHITE = (255, 255, 255)
BRICK_COLOR = (0, 128, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Paddle
paddle_width, paddle_height = 120, 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 40
paddle_dx = 0  # Initialize the paddle's horizontal velocity

# Ball
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Bricks
brick_width, brick_height = 80, 30
bricks = []

for i in range(5):
    for j in range(8):
        brick = pygame.Rect(j * (brick_width + 10) + 70, i * (brick_height + 10) + 50, brick_width, brick_height)
        bricks.append(brick)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                paddle_dx = -PADDLE_SPEED  # Move the paddle left
            elif event.key == pygame.K_RIGHT:
                paddle_dx = PADDLE_SPEED  # Move the paddle right
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                paddle_dx = 0  # Stop the paddle when the keys are released

    # Update paddle position
    paddle_x += paddle_dx

    # Ensure the paddle stays within the screen boundaries
    paddle_x = max(0, min(WIDTH - paddle_width, paddle_x))

    # Update ball position continuously
    ball_x += ball_dx
    ball_y += ball_dy

    # Collision with walls
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1

    # Collision with paddle
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

    if ball_rect.colliderect(pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)):
        if ball_dy > 0:  # Check if the ball is moving downward
            ball_dy *= -1

    # Collision with bricks
    for brick in bricks[:]:  # Using [:] to iterate over a copy of the list
        if ball_rect.colliderect(brick):
            bricks.remove(brick)
            if ball_dy > 0:  # Check if the ball is moving downward
                ball_dy *= -1

    # Game over condition
    if ball_y >= HEIGHT:
        running = False

    # Clear the screen
    screen.fill((20, 0, 0))

    # Draw the paddle
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
