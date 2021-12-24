import random

import pygame
import os
import sys
from Main import start_menu, level_select

START_POSITION = [0, 550]


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def draw(screen):
    screen.fill((0, 0, 0))
    # pygame.draw.rect(screen, (255, 255, 0), (0, 0, 100, 100))
    # pygame.draw.rect(screen, (255, 255, 0), (width - 100, height - 200, 100, 100))
    # pygame.draw.rect(screen, (255, 255, 0), (50, height - 100, 100, 100))
    # pygame.draw.rect(screen, (255, 255, 0), (width - 200, 200, 100, 100))
    all_sprites.draw(screen)
    pygame.display.flip()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("coala.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = START_POSITION[0] * self.image.get_width(), \
                                    self.image.get_height() * START_POSITION[1]

    def update(self, k, *args):
        color = k.get_at((self.rect.x, self.rect.y))
        if args and args[0].type == pygame.KEYDOWN:
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_s:
                while self.rect.y + 1 < 550:
                    if k.get_at((self.rect.x, (self.rect.y + self.image.get_height()) % height)) != (255, 255, 0, 255):
                        self.rect.y += 1
                    else:
                        break
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_w:
                while self.rect.y - 1 > 0:
                    if k.get_at((self.rect.x, self.rect.y - 1)) != (255, 255, 0, 255):
                        self.rect.y -= 1
                    else:
                        break
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_a:
                while self.rect.x - 1 > 0:
                    if k.get_at((self.rect.x - 1, self.rect.y)) != (255, 255, 0, 255):
                        self.rect.x -= 1
                    else:
                        break
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_d:
                while self.rect.x + 1 < 750:
                    if k.get_at(((self.rect.x + self.image.get_width()) % width, self.rect.y)) != (255, 255, 0, 255):
                        self.rect.x += 1
                    else:
                        break


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = load_image("wall.png")
        self.rect = self.image.get_rect().move(
            self.image.get_width() * pos_x, self.image.get_height() * pos_y)


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Tile(x, y)
            elif level[y][x] == '@':
                xp, yp = x, y
    return xp, yp


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    start_menu(screen)
    level_select(screen)
    pygame.display.flip()
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    START_POSITION = generate_level(load_level('map.txt'))
    Arrow(all_sprites)
    pygame.mouse.set_visible(False)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                all_sprites.update(screen, event)
        draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
