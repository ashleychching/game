import pygame
from pygame import *
from screen_setup import setup_screen
import end
import random
from newbutton import Button
#from button import Button

window, screen_width, screen_height = setup_screen()

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (75, 104, 88)
blue = (229, 236, 244)
mint = (239, 255, 250)
purple = (127, 118, 173)

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
end_start = False
logo = pygame.image.load('graphics/logo/with image.png')
logoRect = logo.get_rect()
logoRect.center = (screen_width / 2, screen_height / 2)

#start/play button
button_width = 200
button_height = 50
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2
button_color = (0, 255, 0)  # Green
button_hover_color = (200, 200, 0)  # Darker green
button_text = "play!"
button_text_color = (255, 255, 255)  # White
button_font = pygame.font.Font(None, 32)
button_rect = pygame.Rect(
    screen_width // 2 - button_width // 2,
    screen_height // 2 - button_height // 2,
    button_width,
    button_height,
)
def button_clicked():
    print("Button clicked!")

# start Screen
while (end_start == False):
    window.fill(blue)
    window.blit(logo, logoRect)
    myfont = pygame.font.SysFont("Britannic Bold", 40)
    # Create the button instance
    button = Button(button_x, button_y, button_width, button_height, button_color, button_hover_color,
                    button_text, button_text_color, button_font, button_clicked)
    button.draw(window)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            end_start = True

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the left mouse button is clicked
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    print("Start game!")
                    end_start =True



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
