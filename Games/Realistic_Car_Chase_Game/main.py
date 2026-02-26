
import pygame
import random
import sys
import os

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini GTA Car Chase")

clock = pygame.time.Clock()

# Load assets
base_path = os.path.dirname(__file__)
assets_path = os.path.join(base_path, "assets")

police_img = pygame.image.load(os.path.join(assets_path, "police.png"))
criminal_img = pygame.image.load(os.path.join(assets_path, "criminal.png"))

# Colors
GRASS = (16,120,16)
ROAD = (60,60,60)
YELLOW = (255,255,0)
WHITE = (255,255,255)

road_width = 350
road_x = WIDTH//2 - road_width//2

player = police_img.get_rect(center=(WIDTH//2, HEIGHT-120))
criminal = criminal_img.get_rect(center=(WIDTH//2, 150))

player_speed = 7
criminal_speed = 6
line_offset = 0
font = pygame.font.SysFont(None, 40)
score = 0
distance_limit = 600

def draw_road():
    global line_offset
    screen.fill(GRASS)
    pygame.draw.rect(screen, ROAD, (road_x, 0, road_width, HEIGHT))

    for i in range(12):
        pygame.draw.rect(screen, YELLOW,
                         (WIDTH//2 - 5, i*80 + line_offset, 10, 40))

    line_offset += 10
    if line_offset > 80:
        line_offset = 0

def show_text(text, color, y):
    render = font.render(text, True, color)
    screen.blit(render, (WIDTH//2 - render.get_width()//2, y))

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > road_x:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < road_x + road_width:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    criminal.y += criminal_speed
    criminal.x += random.choice([-3,-2,0,2,3])
    criminal.x = max(road_x, min(criminal.x, road_x + road_width - criminal.width))

    distance = player.y - criminal.y

    if distance > distance_limit:
        screen.fill((0,0,0))
        show_text("CRIMINAL ESCAPED!", (255,0,0), HEIGHT//2)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    if player.colliderect(criminal):
        screen.fill((0,0,0))
        show_text("CRIMINAL CAUGHT!", (0,255,0), HEIGHT//2)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    criminal_speed += 0.002
    score += 1

    draw_road()
    screen.blit(criminal_img, criminal)
    screen.blit(police_img, player)

    score_text = font.render(f"Chase Time: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()
