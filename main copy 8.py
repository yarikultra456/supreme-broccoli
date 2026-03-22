import pygame
import random


pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("имбулечка")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
RED = (255, 182, 193)
BLUE = (100, 149, 237)
GOLD = (255, 215, 0)


player_size = 150
player_x = W // 4
player_y = H - 10
player_speed = 16


item_size = 30
item_x = random.randint(0, W - item_size)
item_y = 0
item_speed = 0.5

score = 0
font = pygame.font.SysFont("Arial", 32)

running = True
while running:
    screen.fill(RED) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < W - player_size:
        player_x += player_speed

    
    item_y += item_speed
    if item_y > H:
        item_y = 0
        item_x = random.randint(0, W - item_size)
        score -= 3 

 
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    item_rect = pygame.Rect(item_x, item_y, item_size, item_size)

    if player_rect.colliderect(item_rect):
        score += 300
        item_y = 0
        item_x = random.randint(0, W - item_size)
        item_speed += 0.2

    
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    pygame.draw.ellipse(screen, GOLD, (item_x, item_y, item_size, item_size))

    
    score_text = font.render(f"Очки : {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()