import random

import pygame
import os
import sys
from time import sleep
from Main import start_menu, pause, win

poss = (0, 0)
cir = 0


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
    all_sprites.draw(screen)
    pygame.display.flip()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, *group):
        global POSITION
        super().__init__(*group)
        self.image = load_image("coala.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = POSITION[0] * self.image.get_width(), \
                                   self.image.get_height() * POSITION[1]
        POSITION = [self.rect.y // 50, self.rect.x // 50]

    def update(self, k, *args):
        global POSITION
        global win_coord
        if args and args[0].type == pygame.KEYDOWN:
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_s:
                while self.rect.y + 1 < 551:
                    if k.get_at((self.rect.x, (self.rect.y + self.image.get_height()) % height)) != (255, 255, 0, 255):
                        self.rect.y += 1
                    else:
                        break
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_w:
                while self.rect.y - 1 >= 0:
                    if k.get_at((self.rect.x, self.rect.y - 1)) != (255, 255, 0, 255):
                        self.rect.y -= 1
                    else:
                        break
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_a:
                while self.rect.x - 1 >= 0:
                    if k.get_at((self.rect.x - 1, self.rect.y)) != (255, 255, 0, 255):
                        self.rect.x -= 1
                    else:
                        break
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_d:
                while self.rect.x + 1 < 751:
                    if k.get_at(((self.rect.x + self.image.get_width()) % width, self.rect.y)) != (255, 255, 0, 255):
                        self.rect.x += 1
                    else:
                        break
            if win_coord[0] == self.rect.x and win_coord[1] == self.rect.y:
                win(screen)

        POSITION = (self.rect.y // 50, self.rect.x // 50)


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


class Win(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0):
        super().__init__(tiles_group, all_sprites)
        global win_coord
        win_coord = (0, 0)
        self.image = load_image("win.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(
            self.image.get_width() * pos_x, self.image.get_height() * pos_y)
        if pos_x > 0 and pos_y > 0:
            win_coord = (pos_x * 50, pos_y * 50)


class Spirit(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group)
        self.image = load_image("spirit.png")
        self.rect = self.image.get_rect().move(
            50 * pos_x, 50 * pos_y)

    def update(self, k):
        global cir
        if cir == 50:
            queue = []
            pos = [0, 0]
            matrix = []
            for i in range(len(mmap)):
                matrix.append([])
                for j in range(len(mmap[i])):
                    if k.get_at((50 * j, 50 * i)) == (255, 255, 0, 255):
                        matrix[i].append(-1)
                    else:
                        matrix[i].append(0)
            # self.rect.x = self.rect.x // len(matrix[self.rect.y // 50]) * len(matrix[self.rect.y // 50])
            matrix[self.rect.y // 50][self.rect.x // 50] = 1
            queue.append((self.rect.y // 50, self.rect.x // 50))
            now = (0, 0)
            while queue:
                now = queue.pop(0)
                if now[0] == POSITION[0] and now[1] == POSITION[1]:
                    break
                if matrix[now[0]][now[1]] != -1 and now[0] != 0 and matrix[now[0] - 1][now[1]] == 0:
                    matrix[now[0] - 1][now[1]] = matrix[now[0]][now[1]] + 1
                    queue.append((now[0] - 1, now[1]))
                if matrix[now[0]][now[1]] != -1 and now[0] != len(mmap) - 1 and matrix[now[0] + 1][now[1]] == 0:
                    matrix[now[0] + 1][now[1]] = matrix[now[0]][now[1]] + 1
                    queue.append((now[0] + 1, now[1]))
                if matrix[now[0]][now[1]] != -1 and now[1] != len(mmap[now[0]]) - 1 and now[1] != 14 \
                        and matrix[now[0]][now[1] + 1] == 0:
                    matrix[now[0]][now[1] + 1] = matrix[now[0]][now[1]] + 1
                    queue.append((now[0], now[1] + 1))
                if matrix[now[0]][now[1]] != -1 and now[1] != 0 and matrix[now[0]][now[1] - 1] == 0:
                    matrix[now[0]][now[1] - 1] = matrix[now[0]][now[1]] + 1
                    queue.append((now[0], now[1] - 1))
            queue.clear()
            # for i in matrix:
            #     print(i)
            while matrix[now[0]][now[1]] > 2:
                if now[0] != 0 and matrix[now[0]][now[1]] - 1 == matrix[now[0] - 1][now[1]]:
                    now = (now[0] - 1, now[1])
                elif now[0] != len(mmap) - 1 and matrix[now[0]][now[1]] - 1 == matrix[now[0] + 1][now[1]]:
                    now = (now[0] + 1, now[1])
                elif now[1] != 0 and matrix[now[0]][now[1]] - 1 == matrix[now[0]][now[1] - 1]:
                    now = (now[0], now[1] - 1)
                elif now[1] != len(mmap[now[0]]) - 1 and matrix[now[0]][now[1]] - 1 == matrix[now[0]][now[1] + 1]:
                    now = (now[0], now[1] + 1)
            if now[0] != 0 and matrix[now[0] - 1][now[1]] == 1:
                self.rect.y += 50
            elif now[0] != len(mmap) - 1 and matrix[now[0] + 1][now[1]] == 1:
                self.rect.y -= 50
            elif now[1] != 0 and matrix[now[0]][now[1] - 1] == 1:
                self.rect.x += 50
            elif now[1] != len(mmap[now[0]]) - 1 and matrix[now[0]][now[1] + 1] == 1:
                self.rect.x -= 50
            cir = 0
        cir += 1


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Tile(x, y)
            elif level[y][x] == '!':
                Win(x, y)
            elif level[y][x] == '@':
                xp, yp = x, y
            elif level[y][x] == '$':
                Spirit(x, y)
    return xp, yp


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    start_menu(screen)
    pygame.display.flip()
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    mmap = load_level('map.txt')
    POSITION = generate_level(mmap)
    Arrow(all_sprites)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause(screen)
                pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                all_sprites.update(screen, event)
                all_sprites.draw(screen)
        player_group.update(screen)
        draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
    pygame.quit()
