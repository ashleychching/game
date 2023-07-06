import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Crossy Road")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Set up the player character
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10

# Set up enemy cars
car_width = 140
car_height = 70
car_x = screen_width + car_width
car_y = random.randint(0, screen_height - car_height)
car_speed = 5

clock = pygame.time.Clock()
game_over = False

def draw_player(x, y):
    pygame.draw.rect(window, white, (x, y, player_size, player_size))

def draw_car(x, y):
    pygame.draw.rect(window, green, (x, y, car_width, car_height))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    window.fill(black)
    draw_player(player_x, player_y)

    car_x -= car_speed
    draw_car(car_x, car_y)

    if car_x < -car_width:
        car_x = screen_width + car_width
        car_y = random.randint(0, screen_height - car_height)

    if player_x < car_x + car_width and player_x + player_size > car_x and player_y < car_y + car_height and player_y + player_size > car_y:
        game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
