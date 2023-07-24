import pygame, random, sys
from pygame.locals import *
from decimal import *

SCREEN_SIZE = (800, 600)
TILE_SIZE = 32

pygame.font.init()

font = pygame.font.SysFont('Arial', 64)
score = 0

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
        self.image = pygame.transform.scale((pygame.image.load('grass.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Water():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('water.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Railroad():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('railroad.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Road():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('road.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class TallTree():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('tallTree.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class ShortTree():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('shortTree.png')), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class SmallRock():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('smallrock.png')), (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Lilypad():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('lilypad.png')), (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Log():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('log.png')), (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Bench():
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('bench.png')), (42, 42))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Player:
    def __init__(self, x, y):
        self.image = pygame.transform.scale((pygame.image.load('explayer.png')), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score_value = 0

    def update(self):
        k = pygame.key.get_pressed()
        if k[K_UP]:
            self.rect.y -= 5
            self.score_value -= 1
        if k[K_DOWN]:
            self.rect.y += 5
            self.score_value += 1
        if k[K_LEFT]:
            self.rect.x -= 5
        if k[K_RIGHT]:
            self.rect.x += 5
        '''if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT'''


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

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
                    self.player = Player(x + 775, y + 140)
                    t.append(Grass(x, y))
        return t

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def renderSCR(self):
        self.screen.fill("white")
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

pygame.init()

g = Game()
pygame.display.set_caption("Crossy Road")
g.main()
