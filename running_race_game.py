import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sequential Object Catcher Game")

# Colors
BACKGROUND_COLOR = (135, 206, 250)  # Light blue
BASKET_COLOR = (255, 215, 0)  # Gold
ITEM_COLORS = [(255, 69, 0), (0, 191, 255)]  # Red and Blue for alternating items
WHITE = (255, 255, 255)

# Basket settings
basket_width = 100
basket_height = 20
basket_speed = 7
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10  # Position the basket near the bottom

# Falling item settings
item_size = 20
item_x = random.randint(0, WIDTH - item_size)
item_y = -item_size  # Start item off-screen at the top
item_speed = random.randint(3, 6)

# Game variables
score = 0
lives = 3
font = pygame.font.Font(None, 36)
current_color_index = 0  # Track which color is currently falling

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BACKGROUND_COLOR)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Update item position
    item_y += item_speed

    # Check if item is caught
    if (basket_y < item_y + item_size < basket_y + basket_height and
        basket_x < item_x + item_size // 2 < basket_x + basket_width):
        score += 1
        # Reset item position, speed, and alternate color
        item_x = random.randint(0, WIDTH - item_size)
        item_y = -item_size
        item_speed = random.randint(3, 6)
        current_color_index = (current_color_index + 1) % 2  # Alternate color

    # Check if item is missed
    if item_y > HEIGHT:
        lives -= 1
        # Reset item position, speed, and alternate color
        item_x = random.randint(0, WIDTH - item_size)
        item_y = -item_size
        item_speed = random.randint(3, 6)
        current_color_index = (current_color_index + 1) % 2  # Alternate color

    # Draw basket
    pygame.draw.rect(screen, BASKET_COLOR, (basket_x, basket_y, basket_width, basket_height))

    # Draw falling item
    pygame.draw.rect(screen, ITEM_COLORS[current_color_index], (item_x, item_y, item_size, item_size))

    # Display score and lives
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 100, 10))

    # Check for game over
    if lives <= 0:
        game_over_text = font.render("Game Over!", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 60, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Pause to show the game over message
        running = False

    # Update the screen
    pygame.display.flip()
    clock.tick(30)  # Limit to 30 frames per second

pygame.quit()
sys.exit()




