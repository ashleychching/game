import pygame
from pygame import *
from screen_setup import setup_screen
import end
import random
from button import Button
import os
from audio import play_audio

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
        self.sprites = []
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile000.png'))
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile001.png'))
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile002.png'))
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile003.png'))
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile004.png'))
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile005.png'))
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile006.png'))
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile007.png'))
        self.sprites.append(pygame.image.load('graphics/doggos/black dog/tile008.png'))

        self.left_sprites = [pygame.image.load('graphics/doggos/black dog/tile000.png'),
                             pygame.image.load('graphics/doggos/black dog/tile001.png'),
                             pygame.image.load('graphics/doggos/black dog/tile002.png'),
                             pygame.image.load('graphics/doggos/black dog/tile003.png')]
        self.right_sprites = [pygame.image.load('graphics/doggos/navy dog dog/tile000.png'),
                              pygame.image.load('graphics/doggos/navy dog/tile001.png'),
                              pygame.image.load('graphics/doggos/navy dog/tile002.png'),
                              pygame.image.load('graphics/doggos/navy dog/tile003.png')]
        self.up_sprites = [pygame.image.load('graphics/doggos/white brown dog/tile000.png'),
                           pygame.image.load('graphics/doggos/white brown dog/tile001.png'),
                           pygame.image.load('graphics/doggos/white brown dog/tile002.png'),
                           pygame.image.load('graphics/doggos/white brown dog/tile003.png')]
        self.down_sprites = [pygame.image.load('graphics/doggos/black white dog/tile000.png'),
                             pygame.image.load('graphics/doggos/black white dog/tile001.png'),
                             pygame.image.load('graphics/doggos/black white dog/tile002.png'),
                             pygame.image.load('graphics/doggos/black white dog/tile003.png')]
        self.current_animation = None

        self.current_sprite= 0
        self.image= self.sprites[self.current_sprite]


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.center = (self.x, self.y)
        self.current_sprite += .2
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.update()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            moving_sound = mixer.Sound("audio/jump1.mp3")
            moving_sound2 = mixer.Sound("audio/jump2.mp3")
            moving_sound.set_volume(.1)
            moving_sound2.set_volume(.3)
            moving_sound.play()
            moving_sound2.play()
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
start_button_width = 200
start_button_height = 50
start_button_x = (screen_width - start_button_width) // 2
start_button_y = (screen_height - start_button_height) // 1.25
start_button_color = Colors.purple
start_button_hover_color = Colors.green
start_button_text = ""
start_button_text_color = Colors.white
start_button_font = pygame.font.Font(None, 32)
start_button_rect = pygame.Rect(
    start_button_x,
    start_button_y,
    start_button_width,
    start_button_height,
)
start_button_image = pygame.image.load("graphics/icons/dog running.png")
start_button_image = pygame.transform.scale(start_button_image, (start_button_width / 4, start_button_height))


def button_clicked():
    print("Button clicked!")


# volume button variables
volume_on = True
volume_button_width = 50
volume_button_height = 50
volume_button_x = (screen_width - volume_button_width) // 1.03
volume_button_y = (screen_height - volume_button_height) // 30
volume_button_color = Colors.purple
volume_button_hover_color = Colors.green
volume_button_text = ""
volume_button_text_color = Colors.white
volume_button_font = pygame.font.Font(None, 32)
volume_button_rect = pygame.Rect(
    volume_button_x,
    volume_button_y,
    volume_button_width,
    volume_button_height,
)
volume_on_icon = pygame.image.load('graphics/icons/white vol on.png')
volume_on_icon = pygame.transform.scale(volume_on_icon,
                                        (volume_button_width / 1.5, volume_button_height / 1.5))
volume_off_icon = pygame.image.load('graphics/icons/white vol off.png')
volume_off_icon = pygame.transform.scale(volume_off_icon,
                                         (volume_button_width / 1.5, volume_button_height / 1.5))
volume_button_image = volume_off_icon
# select characters button
select_button_width = 70
select_button_height = 70
select_button_x = (screen_width - select_button_width) // 30
select_button_y = (screen_height - select_button_height) // 1.05
select_button_color = Colors.purple
select_button_hover_color = Colors.green
select_button_text = ""
select_button_text_color = Colors.white
select_button_font = pygame.font.Font(None, 32)
select_button_rect = pygame.Rect(
    select_button_x,
    select_button_y,
    select_button_width,
    select_button_height,
)
select_button_image = pygame.image.load("graphics/icons/white sel char.png")
select_button_image = pygame.transform.scale(select_button_image,
                                             (select_button_width / 1.3, select_button_height / 1.3))

# start screen variables
end_start = False
logo = pygame.image.load('graphics/logo/with image.png')
logoRect = logo.get_rect()
logoRect.center = (screen_width / 2, screen_height / 2.5)
# start screen
while not end_start:
    window.fill(Colors.blue)
    window.blit(logo, logoRect)
    myfont = pygame.font.SysFont("Britannic Bold", 40)
    start_button = Button(start_button_x, start_button_y, start_button_width, start_button_height, start_button_color,
                          start_button_hover_color,
                          start_button_text, start_button_text_color, start_button_font, button_clicked,
                          border_radius=10,
                          image=start_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))
    start_button.draw(window)
    volume_button = Button(volume_button_x, volume_button_y, volume_button_width, volume_button_height,
                           volume_button_color,
                           volume_button_hover_color,
                           volume_button_text, volume_button_text_color, volume_button_font, button_clicked,
                           border_radius=10,
                           image=volume_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))
    volume_button.draw(window)
    select_button = Button(select_button_x, select_button_y, select_button_width, select_button_height,
                           select_button_color,
                           select_button_hover_color,
                           select_button_text, select_button_text_color, select_button_font, button_clicked,
                           border_radius=10,
                           image=select_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))
    select_button.draw(window)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button is clicked
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos):
                end_start = True
            if volume_button_rect.collidepoint(mouse_pos):
                volume_on = not volume_on
                if not volume_on:
                    volume_button_image = volume_on_icon
                    mixer.music.pause()
                else:
                    volume_button_image = volume_off_icon
                    mixer.music.unpause()

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

    window.fill(Colors.purple)
    player.draw(window)
    update_game()

    pygame.display.update()
    clock.tick(60)
end.end_screen()
pygame.quit()
