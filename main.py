import pygame
from pygame import *
import end
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
green = (75, 104, 88)
blue= (229, 236, 244)
mint= (239, 255, 250)
purple=(127, 118, 173)

# Set up the player character
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_surface = pygame.image.load('graphics/doggos/black dog/tile000.png')


# Set up enemy cars
car_width = 140
car_height = 70
car_x = screen_width + car_width
car_y = random.randint(0, screen_height - car_height)
car_surface = pygame.image.load('graphics/cars/tile001.png')
car_surface = pygame.transform.scale(car_surface, (car_width, car_height))
car_speed = 5



clock = pygame.time.Clock()
game_over = False
end_start= False
logo = pygame.image.load('graphics/logo/with image.png')
logoRect= logo.get_rect()
logoRect.center= (screen_width/2, screen_height/2)

while (end_start == False):
    window.fill(blue)

    window.blit(logo,logoRect)
    myfont = pygame.font.SysFont("Britannic Bold", 40)
    #nlabel = myfont.render("Welcome " + " Start Screen", 1, purple)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            end_start = True
    #window.blit(nlabel, (200, 200))
    pygame.display.flip()

def draw_player(x, y):
    pygame.draw.rect(window, white, (x, y, player_size, player_size))
    window.blit(player_surface, (x, y))

def draw_car(x, y):
    pygame.draw.rect(window, green, (x, y, car_width, car_height))
    window.blit(car_surface, (x, y))

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
end.end_screen()
pygame.quit()
