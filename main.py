import pygame
from pygame import *
from screen_setup import setup_screen
import end
import random
from button import Button

window, screen_width, screen_height = setup_screen()


# Set up colors
class Colors:
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (75, 104, 88)
    blue = (229, 236, 244)
    mint = (239, 255, 250)
    purple = (127, 118, 173)


class Player:
    def __init__(self, x, y, size, image):
        self.x = x
        self.y = y
        self.size = size
        self.image = image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.center = (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.update()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move(-5, 0)
            elif event.key == pygame.K_RIGHT:
                self.move(5, 0)
            elif event.key == pygame.K_UP:
                self.move(0, -5)
            elif event.key == pygame.K_DOWN:
                self.move(0, 5)

    def get_rect(self):
        return self.rect.copy()


class Car:
    def __init__(self, x, y, width, height, speed, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def reset(self, screen_width, screen_height):
        self.x = screen_width + self.width
        self.y = random.randint(0, screen_height - self.height)
        self.rect.x = self.x
        self.rect.y = self.y


# collision logic
def update_game():
    global game_over

    car.update()
    car.draw(window)

    if car.x < -car.width:
        car.reset(screen_width, screen_height)

    player_rect = player.get_rect()
    car_rect = car.rect

    if player_rect.colliderect(car_rect):
        game_over = True


# Set up the player character
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_image = pygame.image.load('graphics/doggos/black dog/tile000.png')
player = Player(player_x, player_y, player_size, player_image)

# Set up enemy cars
car_width = 140
car_height = 70
car_speed = 5
car_image = pygame.image.load('graphics/cars/tile001.png')
car = Car(screen_width + car_width, random.randint(0, screen_height - car_height), car_width, car_height, car_speed,
          car_image)

# start/play button
button_width = 200
button_height = 50
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 1.25
button_color = Colors.purple
button_hover_color = Colors.mint
button_text = ""
button_text_color = (255, 255, 255)  # White
button_font = pygame.font.Font(None, 32)
button_rect = pygame.Rect(
    button_x,
    button_y,
    button_width,
    button_height,
)
button_image = pygame.image.load("graphics/icons/dog running.png")
button_image = pygame.transform.scale(button_image, (button_width / 4, button_height))


def button_clicked():
    print("Button clicked!")


# start screen variables
end_start = False
logo = pygame.image.load('graphics/logo/with image.png')
logoRect = logo.get_rect()
logoRect.center = (screen_width / 2, screen_height / 2.5)
# start Screen
while (end_start == False):
    window.fill(Colors.blue)
    window.blit(logo, logoRect)
    myfont = pygame.font.SysFont("Britannic Bold", 40)
    start_button = Button(button_x, button_y, button_width, button_height, button_color, button_hover_color,
                          button_text, button_text_color, button_font, button_clicked, border_radius=10,
                          image=button_image, shadow_color=Colors.green, shadow_offset=(7, 7))
    start_button.draw(window)
    pygame.display.flip()
    while not end_start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the left mouse button is clicked
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    end_start = True
game_over = False
clock = pygame.time.Clock()
# game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        player.handle_event(event)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_UP]:
        player.move(0, -5)
    if keys[pygame.K_DOWN]:
        player.move(0, 5)

    window.fill(Colors.purple )
    player.draw(window)
    update_game()

    pygame.display.update()
    clock.tick(60)
end.end_screen()
pygame.quit()
