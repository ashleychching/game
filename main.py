import sys
import pygame
from pygame import *
from decimal import *
from screen_setup import setup_screen
import end
import random
from button import Button
import select_page
from colors import Colors
import time
from audio import play_audio
exec(open('select_page.py').read())
window, screen_width, screen_height = setup_screen()

SCREEN_SIZE = (800, 600)
TILE_SIZE = 32

map = {}

values = range(34)
# 1004?
for i in values:
    map[0] = "P11111111111111111111111111111111111111111111111111"
    map[1] = "111111111111111111111111111111111111111111111111111"
    map[2] = "111111111111111111111111111111111111111111111111111"
    map[3] = "111111111111111111111111111111111111111111111111111"
    map[4] = "111111111111111111111111111111111111111111111111111"
    map[i] = str(int(str(random.randint(1, 4)) * 51))

with open("map.txt", 'w') as file:
    mapValues = [i for i in map.values()]
    row = '\n'
    rowDisplay = [f'{row}{row.join(mapValues)}']
    file.writelines(rowDisplay)

def toSCRCoord(x, y):
    return (x - y, (x + y) / 2 - 420)

def render(object, screen):
    screen.blit(object.image, toSCRCoord(object.rect.x, object.rect.y))

class Grass():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/grass.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Water():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/water.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Railroad():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/railroad.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Road():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/road.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class TallTree():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/tallTree.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class ShortTree():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/shortTree.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class SmallRock():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/smallrock.png')), (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Lilypad():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/lilypad.png')), (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Log():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/log.png')), (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Bench():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('graphics/blocks/bench.png')), (42, 42))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.character_selection = open("char.txt", "r")
        self.character_index = int(self.character_selection.read()) + 1
        print(self.character_index)
        character_folder = f"graphics/doggos/doggo{self.character_index}"
        self.image = pygame.image.load(f"{character_folder}/tile000.png")
        self.animation_counter = 0
        self.current_sprite = 0
        self.play_animation = False
        self.left_sprites = [pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile012.png'), -20),
                             pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile013.png'), -20),
                             pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile014.png'), -20),
                             pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile015.png'), -20),
                             pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile016.png'), -20),
                             pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile017.png'), -20),
                             pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile018.png'), -20),
                             pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile019.png'), -20),
                             pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile020.png'), -20),
                             ]
        self.right_sprites = [
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile012.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile013.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile014.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile015.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile016.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile017.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile018.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile019.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile020.png'), 20), True, False)
        ]
        self.up_sprites = [
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile012.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile013.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile014.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile015.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile016.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile017.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile018.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile019.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile020.png'), 310), True,
                False)]
        self.down_sprites = [pygame.transform.flip(
            pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile012.png'), 30), False,
            False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile013.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile014.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile015.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile016.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile017.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile018.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile019.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load(f'{character_folder}/tile020.png'), 30), False,
                False)]
        self.current_animation = self.up_sprites
        self.animation_timer = pygame.time.get_ticks()
        self.animation_interval = 18
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, surface):
        if self.current_animation and len(self.current_animation) > 0:
            surface.blit(self.current_animation[self.current_sprite], self.rect)

    def update(self):
        if self.play_animation:  # Check if the animation should play
            current_time = pygame.time.get_ticks()
            if self.current_animation and len(self.current_animation) > 0:
                if current_time - self.animation_timer >= self.animation_interval:
                    self.animation_timer = current_time
                    self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
                    if self.current_sprite == 0:
                        self.play_animation = False  # Stop the animation once it completes playing

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            moving_sound = mixer.Sound("audio/jump1.mp3")
            moving_sound2 = mixer.Sound("audio/jump2.mp3")
            moving_sound.set_volume(.1)
            moving_sound2.set_volume(.3)
            moving_sound.play()
            moving_sound2.play()
            if event.key == pygame.K_LEFT:
                self.current_animation = self.left_sprites
            elif event.key == pygame.K_RIGHT:
                self.current_animation = self.right_sprites
            elif event.key == pygame.K_UP:
                self.current_animation = self.up_sprites
            elif event.key == pygame.K_DOWN:
                self.current_animation = self.down_sprites
            self.play_animation = True

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


class Player2:
    def __init__(self, x, y, size):
        self.image = pygame.transform.scale((pygame.image.load('graphics/doggos/doggo6/tile000.png')), (32, 32))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.size = size
        self.rect.x = x
        self.rect.y = y
        self.animation_counter = 0
        self.current_sprite = 0
        self.play_animation = False
        self.left_sprites = [pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile012.png'), -20),
                             pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile013.png'), -20),
                             pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile014.png'), -20),
                             pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile015.png'), -20),
                             pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile016.png'), -20),
                             pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile017.png'), -20),
                             pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile018.png'), -20),
                             pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile019.png'), -20),
                             pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo1/tile020.png'), -20),
                             ]
        self.right_sprites = [
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile012.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile013.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile014.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile015.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile016.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile017.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile018.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile019.png'), 20), True, False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo5/tile020.png'), 20), True, False)
        ]
        self.up_sprites = [
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile012.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile013.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile014.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile015.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile016.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile017.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile018.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile019.png'), 310), True,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile020.png'), 310), True,
                False)]
        self.down_sprites = [pygame.transform.flip(
            pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile012.png'), 30), False,
            False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile013.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile014.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile015.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile016.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile017.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile018.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile019.png'), 30), False,
                False),
            pygame.transform.flip(
                pygame.transform.rotate(pygame.image.load('graphics/doggos/doggo6/tile020.png'), 30), False,
                False)]
        self.current_animation = self.up_sprites
        self.animation_timer = pygame.time.get_ticks()
        self.animation_interval = 18

    def draw(self, surface):
        if self.current_animation and len(self.current_animation) > 0:
            surface.blit(self.current_animation[self.current_sprite], self.rect)

    def update(self):
        k = pygame.key.get_pressed()
        if k[K_UP]:
            self.rect.y -= 5
        if k[K_DOWN]:
            self.rect.y += 5
        if k[K_LEFT]:
            self.rect.x -= 5
        if k[K_RIGHT]:
            self.rect.x += 5
        if self.play_animation:  # Check if the animation should play
            current_time = pygame.time.get_ticks()
            if self.current_animation and len(self.current_animation) > 0:
                if current_time - self.animation_timer >= self.animation_interval:
                    self.animation_timer = current_time
                    self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)
                    if self.current_sprite == 0:
                        self.play_animation = False  # Stop the animation once it completes playing

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.topleft = (self.x, self.y)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            moving_sound = mixer.Sound("audio/jump1.mp3")
            moving_sound2 = mixer.Sound("audio/jump2.mp3")
            moving_sound.set_volume(.1)
            moving_sound2.set_volume(.3)
            moving_sound.play()
            moving_sound2.play()
            if event.key == pygame.K_LEFT:
                print("left")
                self.current_animation = self.left_sprites
                print(self.current_animation)
            elif event.key == pygame.K_RIGHT:
                print("right")
                self.current_animation = self.right_sprites
                print(self.current_animation)
            elif event.key == pygame.K_UP:
                self.current_animation = self.up_sprites
            elif event.key == pygame.K_DOWN:
                self.current_animation = self.down_sprites
            self.play_animation = True

    def get_rect(self):
        return self.rect.copy()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.jump_count = 0
        self.previous_move_direction = None
        self.game_over = False
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.game_loop()
    def loadLVL(self, lvl):
        f = open(lvl, "r")
        data = f.readlines()
        t = []
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == "1":
                    t.append(Grass(x, y))
                    if random.randint(0, 2) and random.randint(1, 4) == 1:
                        t.append(TallTree(x - 1, y - Decimal(1.15)))
                    if random.randint(0, 2) and random.randint(1, 4) == 1:
                        t.append(ShortTree(x - 1, y - Decimal(1.15)))
                    if random.randint(0, 2) and random.randint(1, 4) == 1:
                        t.append(SmallRock(x - Decimal(0.75), y - Decimal(0.9)))
                    if random.randint(0, 2) and random.randint(1, 5) == 1:
                        t.append(Bench(x - 1, y - Decimal(.5)))
                elif data[y][x] == "2":
                    t.append(Water(x, y))
                    if random.randint(0, 2) and random.randint(1, 2) == 1:
                        t.append(Lilypad(x - 1, y - Decimal(0.75)))
                    if random.randint(0, 2) and random.randint(1, 2) == 1:
                        t.append(Log(x - Decimal(0.85), y - Decimal(0.6)))
                elif data[y][x] == "3":
                    t.append(Railroad(x, y))
                elif data[y][x] == "4":
                    t.append(Road(x, y))
                elif data[y][x] == "P":
                    self.player = Player2(x + 975, y + 900, 32)
                    t.append(Grass(x, y))
        return t

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            self.player.handle_event(event)
        self.player.update()

    def renderSCR(self):
        for tile in self.tiles:
            render(tile, self.screen)
        render(self.player, self.screen)
        pygame.display.update()

    def start(self):
        self.tiles = self.loadLVL("map.txt")

    def update(self):
        while True:
            self.events()
            self.player.update()
            self.renderSCR()
            self.clock.tick(60)

    def main(self):
        self.start()
        self.update()


# collision logic
    def update_game(self):
        global game_over

        self.car.update()
        self.car.draw(window)

        if self.car.x < -self.car.width:
            self.car.reset(screen_width, screen_height)

        player_rect = self.player.get_rect()
        car_rect = self.car.rect

        if player_rect.colliderect(car_rect):
            crash_sound = mixer.Sound("audio/crash.mp3")
            crash_sound.set_volume(.3)
            crash_sound.play()
            time.sleep(.5)
            self.game_over = True


    # Set up the player character
    player_size = 50
    player_x = screen_width // 2 - player_size // 2
    player_y = screen_height - player_size - 10

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


    def button_clicked(self):
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
    # button rendering
    start_button = Button(start_button_x, start_button_y, start_button_width, start_button_height, start_button_color,
                          start_button_hover_color,
                          start_button_text, start_button_text_color, start_button_font, button_clicked,
                          border_radius=10,
                          image=start_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))

    select_button = Button(select_button_x, select_button_y, select_button_width, select_button_height,
                           select_button_color,
                           select_button_hover_color,
                           select_button_text, select_button_text_color, select_button_font, button_clicked,
                           border_radius=10,
                           image=select_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))

    # start screen
    while not end_start:
        window.fill(Colors.blue)
        window.blit(logo, logoRect)
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        start_button.draw(window)
        volume_button = Button(volume_button_x, volume_button_y, volume_button_width, volume_button_height,
                               volume_button_color,
                               volume_button_hover_color,
                               volume_button_text, volume_button_text_color, volume_button_font, button_clicked,
                               border_radius=10,
                               image=volume_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))
        volume_button.draw(window)
        select_button.draw(window)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the left mouse button is clicked
                mouse_pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_pos):
                    time.sleep(.15)
                    player = Player2(player_x, player_y, player_size)
                    end_start = True
                if volume_button_rect.collidepoint(mouse_pos):
                    volume_on = not volume_on
                    if not volume_on:
                        volume_button_image = volume_on_icon
                        mixer.music.pause()
                    else:
                        volume_button_image = volume_off_icon
                        mixer.music.unpause()
                if select_button_rect.collidepoint(mouse_pos):
                    time.sleep(.15)
                    select_page.open_select_page()


    def game_loop(self):
        counter_font = pygame.font.Font(None, 36)
        counter_pos = (10, 10)
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                self.player.handle_event(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and not self.move_left:
                        self.move_left = True
                        self.player.move(-40, 0)
                    elif event.key == pygame.K_RIGHT and not self.move_right:
                        self.move_right = True
                        self.player.move(40, 0)
                    elif event.key == pygame.K_UP and not self.move_up:
                        self.move_up = True
                        self.player.move(0, -40)
                        if (self.move_left and self.previous_move_direction != "left") or \
                                (self.move_right and self.previous_move_direction != "right") or \
                                (self.move_up and self.previous_move_direction != "up" and not self.move_down) or \
                                (self.move_down and self.previous_move_direction != "down" and not self.move_up):
                            self.jump_count += 1
                            self.previous_move_direction = None
                    elif event.key == pygame.K_DOWN and not self.move_down:
                        self.move_down = True
                        self.player.move(0, 40)

                    # Check for key release events
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.move_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.move_right = False
                    elif event.key == pygame.K_UP:
                        self.move_up = False
                    elif event.key == pygame.K_DOWN:
                        self.move_down = False

            self.player.update()

            window.fill(Colors.purple)
            self.player.draw(window)
            counter_text = counter_font.render(f"Jumps: {self.jump_count}", True, Colors.white)
            window.blit(counter_text, counter_pos)
            self.update_game()
            pygame.display.update()
            self.clock.tick(60)

        end.end_screen()
        pygame.quit()


if __name__ == "__main__":
    game = Game()

