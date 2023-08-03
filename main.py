import pygame, random, end, select_page
from pygame import *
from decimal import *
from screen_setup import setup_screen
from button import Button
from colors import Colors
import time

from audio import play_audio

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



class Car:
    def __init__(self, x, y, width, height, speed, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 2
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.delay = random.randint(30, 100)
        self.start_x = x
        self.spawned = False  # A flag to indicate if the car has been spawned
        self.spawn_pos = (x, y)  # Store the spawn position
        self.direction = 1

    def update(self):
        # self.x -= self.speed
        self.x += self.speed * self.direction
        self.rect.x = self.x
        if self.direction == 1:
            # If the car is moving from left to right, check if it's off-screen on the right side
            if self.x > SCREEN_SIZE[0]:
                # If off-screen, reset the car to the left side
                self.x = -self.width
                self.rect.x = self.x
        else:
            # If the car is moving from right to left, check if it's off-screen on the left side
            if self.x < -self.width:
                # If off-screen, reset the car to the right side
                self.x = SCREEN_SIZE[0]
                self.rect.x = self.x

        if not self.spawned:  # If the car has not been spawned yet
            self.delay -= 1  # Reduce the delay until it reaches 0
            if self.delay <= 0:
                self.spawned = True  # Set the flag to indicate the car has been spawned
                self.x = self.spawn_pos[0]  # Set the car's x-coordinate to the spawn position
                self.rect.x = self.x
                self.rect.y = self.y
        else:
            self.x += self.speed * self.direction
            self.rect.x = self.x

    def reset(self):
        self.x = self.start_x  # Reset the car's x-coordinate to the initial starting point
        self.delay = random.randint(30, 100)


class Player2:
    def __init__(self, x, y, size):
        self.image = (pygame.image.load('graphics/doggos/doggo5/tile000.png'))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.size = size
        self.rect.x = x
        self.rect.y = y
        self.play_animation = False
        self.animation_timer = pygame.time.get_ticks()
        self.animation_interval = 18
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
        self.play_animation = False
        self.current_sprite = 0
        self.click_animation = False

    def update(self):
        k = pygame.key.get_pressed()
        if k[K_UP]:
            self.rect.y -= 5
            self.current_animation = self.up_sprites
            self.play_animation = True
            self.image= self.current_animation[self.current_sprite]
        if k[K_DOWN]:
            self.rect.y += 5
            self.current_animation = self.down_sprites
            self.play_animation = True
            self.image= self.current_animation[self.current_sprite]
        if k[K_LEFT]:
            self.rect.x -= 5
            self.current_animation = self.left_sprites
            self.play_animation = True
            self.image= self.current_animation[self.current_sprite]
        if k[K_RIGHT]:
            self.rect.x += 5
            self.current_animation = self.right_sprites
            self.play_animation = True
            self.image= self.current_animation[self.current_sprite]

        # Move this block inside the update method
        current_time = pygame.time.get_ticks()
        if self.play_animation and self.current_animation:
            if current_time - self.animation_timer >= self.animation_interval:
                self.animation_timer = current_time
                self.current_sprite = (self.current_sprite + 1) % len(self.current_animation)


        # Update the player's position using the rect object
        self.rect.topleft = (self.rect.x, self.rect.y)

    def get_rect(self):
        return self.rect.copy()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

    def loadLVL(self, lvl):
        f = open(lvl, "r")
        data = f.readlines()
        t = []
        self.road_tiles = []
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
                    self.car = Car(x , y , 140, 70, 5, pygame.image.load('graphics/cars/tile002.png'))
                    t.append(Car(x,y,140, 70, 5, pygame.image.load('graphics/cars/tile001.png')))
                    self.road_tiles.append((x, y))
                elif data[y][x] == "P":
                    t.append(Grass(x, y))
                    self.player = Player2(x + 975, y + 900, 32)
                    self.player.update()

        return t

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    def renderSCR(self):
        for tile in self.tiles:
            render(tile, self.screen)
        render(self.player, self.screen)
        for car in self.cars:
            render(car, self.screen)
        pygame.display.update()

    def start(self):
        self.tiles = self.loadLVL("map.txt")
        self.cars = []
        car_spacing = 350
        num_cars_per_road = 1
        cars_per_road = {}

        for i, (x, y) in enumerate(self.road_tiles):
            while len(cars_per_road.get((x, y), [])) < num_cars_per_road:
                # Determine the initial_x based on the car's direction
                initial_x = -100 if random.randint(0, 1) == 0 else SCREEN_SIZE[0]*2
                car = Car(initial_x, y * TILE_SIZE, 70, 35, 2,
                          pygame.image.load('graphics/cars/tile002.png'))  # Slower speed
                self.cars.append(car)

                # Set the direction of the car based on its initial_x
                car.direction = 1 if initial_x == -100 else -1

                # Add the car to the list of cars on this road
                cars_per_road.setdefault((x, y), []).append(car)

                # Call reset to set the car to its starting position
                car.reset()

        # Print the count of cars generated for each road after the loop
        for road, cars_list in cars_per_road.items():
            print(f"Road {road}: {len(cars_list)} cars generated")
    def update(self):
        while True:
            self.events()
            self.player.update()
            self.car.update()

            for car in self.cars:
                # Update the car's position if the delay has passed
                if car.delay <= 0:
                    car.update()
                else:
                    car.delay -= 1

                # Respawn the car at the right edge if it goes off the screen
                if car.x + car.width < 0:
                    car.x = screen_width
                    car.delay = random.randint(0, 100)
                    # Set a new random delay before starting again
                    car.reset()
            self.renderSCR()
            self.clock.tick(60)

    def main(self):
        self.start()
        self.update()


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
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button is clicked
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos):
                time.sleep(.15)
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

game_over = False
clock = pygame.time.Clock()
g = Game()

move_left = False
move_right = False
move_up = False
move_down = False

# game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True



    window.fill(Colors.purple)
    pygame.display.update()
    clock.tick(60)
    g.main()

end.end_screen()
pygame.quit()
