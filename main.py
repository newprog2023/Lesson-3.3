import pygame
import random
import time
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ПРОСТЕНЬКИЙ ТИР - попади в деву из Mortal Kombat')
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load('img/MortalKombat100.png')
target_width = 100
target_height = 100
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#color = (150, 150, 150)
hits = 0
font = pygame.font.Font(None, 36)

# Переменные для отсчета времени
start_time = time.time()
time_limit = 10  # Время в секундах

def get_remaining_time():
    elapsed_time = time.time() - start_time
    remaining_time = max(0, time_limit - int(elapsed_time))
    return remaining_time

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"

def draw_buttons():
    yes_button = pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2, 100, 50)
    no_button = pygame.Rect(2 * SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2, 100, 50)
    pygame.draw.rect(screen, (0, 255, 0), yes_button)
    pygame.draw.rect(screen, (255, 0, 0), no_button)
    yes_text = font.render("ДА", True, (0, 0, 0))
    no_text = font.render("НЕТ", True, (0, 0, 0))
    screen.blit(yes_text, (yes_button.x + 25, yes_button.y + 10))
    screen.blit(no_text, (no_button.x + 25, no_button.y + 10))
    return yes_button, no_button

running = True
game_active = True

while running:
    screen.fill(color)
    if game_active:
        screen.blit(target_image, (target_x, target_y))
        text = font.render(f'Попаданий: {hits}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
        screen.blit(text, text_rect)
        remaining_time = get_remaining_time()
        time_text = font.render(format_time(remaining_time), True, (255, 255, 255))
        screen.blit(time_text, (SCREEN_WIDTH - 80, 10))
    if remaining_time == 0:
        end_text = font.render("Время вышло! Попробовать еще?", True, (255, 255, 255))
        end_text_rect = end_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(font.render(f'Попаданий: {hits}', True, (255, 255, 255)), text_rect)
        screen.blit(end_text, end_text_rect)
        yes_button, no_button = draw_buttons()
        game_active = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_active:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hits += 1
        if event.type == pygame.MOUSEBUTTONDOWN and not game_active:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if yes_button.collidepoint(mouse_x, mouse_y):
                hits = 0
                start_time = time.time()
                game_active = True
            elif no_button.collidepoint(mouse_x, mouse_y):
                running = False

    pygame.display.update()

pygame.quit()
