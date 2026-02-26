import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Car Chase")

clock = pygame.time.Clock()

# Colors
GRAY = (40, 40, 40)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (220, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Road settings
road_width = 300
road_x = WIDTH//2 - road_width//2
line_y = 0
line_speed = 8

# Player (Police)
player_w, player_h = 50, 90
player_x = WIDTH//2 - player_w//2
player_y = HEIGHT - player_h - 20
player_speed = 6

# Enemy (Suspect)
enemy_w, enemy_h = 50, 90
enemy_x = WIDTH//2 - enemy_w//2
enemy_y = 100
enemy_speed = 5

# Game variables
score = 0
font = pygame.font.SysFont(None, 36)
distance_limit = 400

def draw_road():
    global line_y
    pygame.draw.rect(screen, GRAY, (road_x, 0, road_width, HEIGHT))
    
    # Road lines
    for i in range(20):
        pygame.draw.rect(screen, YELLOW,
                         (WIDTH//2 - 5, i*60 + line_y, 10, 40))
    line_y += line_speed
    if line_y > 60:
        line_y = 0

def draw_player():
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_w, player_h))

def draw_enemy():
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_w, enemy_h))

def show_score():
    text = font.render(f"Chase Time: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over(message):
    text = font.render(message, True, RED)
    screen.blit(text, (WIDTH//2 - 150, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Main loop
while True:
    clock.tick(60)
    screen.fill((0, 120, 0))  # Grass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT] and player_x > road_x:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < road_x + road_width - player_w:
        player_x += player_speed
    if keys[pygame.K_UP]:
        enemy_y += 1  # close distance
    if keys[pygame.K_DOWN]:
        enemy_y -= 1  # fall back

    # Enemy random movement
    enemy_x += random.choice([-2, 0, 2])
    enemy_x = max(road_x, min(enemy_x, road_x + road_width - enemy_w))

    # Distance logic
    distance = player_y - enemy_y
    
    if distance > distance_limit:
        game_over("Suspect Escaped!")

    # Collision (catch)
    if (player_x < enemy_x + enemy_w and
        player_x + player_w > enemy_x and
        player_y < enemy_y + enemy_h and
        player_y + player_h > enemy_y):
        game_over("Suspect Caught!")

    # Increase difficulty
    score += 1
    enemy_y += enemy_speed
    enemy_speed += 0.0005

    draw_road()
    draw_enemy()
    draw_player()
    show_score()

    pygame.display.update()