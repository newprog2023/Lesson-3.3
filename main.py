import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ПРОСТЕНЬКИЙ ТИР - попади в деву из Mortal Kombat')
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load('img/MortalKombatG100.png')
target_width = 100
target_height = 100
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
hits = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    screen.blit(target_image, (target_x, target_y))
    text = font.render(f'Попаданий: {hits}', True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hits += 1

    pygame.display.update()

pygame.quit()
