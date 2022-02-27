import random
import sys
import sqlite3
import pygame
import os
import sys
from time import sleep
from Main import start_menu, pause, win, level_select, lose

winn = False

poss = (0, 0)
cir = 0
coins_pos = []
COLLISIONS = []
is_collected = []
count = 0
is_dead = False


# 2

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
    player_group.draw(screen)


class Character(pygame.sprite.Sprite):
    def __init__(self, *group):
        global POSITION
        super().__init__(*group)
        self.image = load_image("coala.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = POSITION[0] * self.image.get_width(), \
                                   self.image.get_height() * POSITION[1]
        POSITION = [self.rect.y // 50, self.rect.x // 50]

    def update(self, k, *args):
        global POSITION, win_coord, winn, coins_pos, is_dead
        if args and args[0].type == pygame.KEYDOWN:
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_s:
                while self.rect.y + 1 < 851:
                    if k.get_at((self.rect.x, (self.rect.y + self.image.get_height()) % height)) != (255, 255, 0, 255):
                        self.rect.y += 1
                    else:
                        break
                    if not self.rect.collidelist(COLLISIONS):
                        is_dead = True
                    for i in range(len(coins_pos)):
                        if self.rect.colliderect(coins_pos[i]):
                            is_collected[i] = True
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_w:
                while self.rect.y - 1 >= 0:
                    if k.get_at((self.rect.x, self.rect.y - 1)) != (255, 255, 0, 255):
                        self.rect.y -= 1
                    else:
                        break
                    if not self.rect.collidelist(COLLISIONS):
                        is_dead = True
                    for i in range(len(coins_pos)):
                        if self.rect.colliderect(coins_pos[i]):
                            is_collected[i] = True
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_a:
                while self.rect.x - 1 >= 0:
                    if k.get_at((self.rect.x - 1, self.rect.y)) != (255, 255, 0, 255):
                        self.rect.x -= 1
                    else:
                        break
                    if not self.rect.collidelist(COLLISIONS):
                        is_dead = True
                    for i in range(len(coins_pos)):
                        if self.rect.colliderect(coins_pos[i]):
                            is_collected[i] = True
            if args and args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_d:
                while self.rect.x + 1 < 1351:
                    if k.get_at(((self.rect.x + self.image.get_width()) % width, self.rect.y)) != (255, 255, 0, 255):
                        self.rect.x += 1
                    else:
                        break
                    if not self.rect.collidelist(COLLISIONS):
                        is_dead = True
                    for i in range(len(coins_pos)):
                        if self.rect.colliderect(coins_pos[i]):
                            is_collected[i] = True
            if win_coord[0] == self.rect.x and win_coord[1] == self.rect.y:
                pygame.display.flip()
                winn = True
        POSITION = (self.rect.y // 50, self.rect.x // 50)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(animated_group)
        self.frames = []
        sheet = load_image("coins.png")
        sheet = pygame.transform.scale(sheet, (400, 50))
        self.cut_sheet(sheet, 8, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.num = len(coins_pos)
        coins_pos.append(self.rect)
        is_collected.append(False)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        global count, coin
        if is_collected[self.num]:
            self.rect.y = 0
            self.rect.x = 50 * count
            count += 1
            is_collected[self.num] = False
            print(count)
        else:
            self.rect = coins_pos[self.num]
            self.cur_frame = (self.cur_frame + 1) % len(self.frames * 2)
            self.image = self.frames[self.cur_frame // 2]


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


class Thorn(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, rotation):
        global COLLISIONS
        super().__init__(tiles_group, all_sprites)
        if rotation == "up":
            self.image = load_image("thorns_up.png")
            self.rect = self.image.get_rect().move(
                self.image.get_width() * pos_x, self.image.get_height() * pos_y)

        if rotation == "down":
            self.image = load_image("thorns_down.png")
            self.rect = self.image.get_rect().move(
                self.image.get_width() * pos_x, self.image.get_height() * pos_y)

        if rotation == "left":
            self.image = load_image("thorns_left.png")
            self.rect = self.image.get_rect().move(
                self.image.get_width() * pos_x, self.image.get_height() * pos_y)

        if rotation == "right":
            self.image = load_image("thorns_right.png")
            self.rect = self.image.get_rect().move(
                self.image.get_width() * pos_x, self.image.get_height() * pos_y)
        COLLISIONS.append(self.rect)


class Spirit(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        global COLLISIONS
        super().__init__(player_group)
        self.image = load_image("spirit.png")
        self.rect = self.image.get_rect().move(
            50 * pos_x, 50 * pos_y)
        self.num = len(COLLISIONS)
        COLLISIONS.append(self.rect)

    def update(self, k):
        global COLLISIONS
        global cir
        if cir == 5:
            queue = []
            pos = [0, 0]
            matrix = []
            for i in range(len(mmap) - 1):
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
                if matrix[now[0]][now[1]] != -1 and now[0] != len(mmap) - 2 and matrix[now[0] + 1][now[1]] == 0:
                    matrix[now[0] + 1][now[1]] = matrix[now[0]][now[1]] + 1
                    queue.append((now[0] + 1, now[1]))
                if matrix[now[0]][now[1]] != -1 and now[1] != len(mmap[now[0]]) - 2 and now[0] != len(mmap) - 1 \
                        and now[1] != 30 and matrix[now[0]][now[1] + 1] == 0:
                    matrix[now[0]][now[1] + 1] = matrix[now[0]][now[1]] + 1
                    queue.append((now[0], now[1] + 1))
                if matrix[now[0]][now[1]] != -1 and now[1] != 0 and matrix[now[0]][now[1] - 1] == 0:
                    matrix[now[0]][now[1] - 1] = matrix[now[0]][now[1]] + 1
                    queue.append((now[0], now[1] - 1))
            queue.clear()
            while matrix[now[0]][now[1]] > 2:
                if now[0] != 0 and matrix[now[0]][now[1]] - 1 == matrix[now[0] - 1][now[1]]:
                    now = (now[0] - 1, now[1])
                elif now[0] != len(mmap) - 2 and matrix[now[0]][now[1]] - 1 == matrix[now[0] + 1][now[1]]:
                    now = (now[0] + 1, now[1])
                elif now[1] != 0 and matrix[now[0]][now[1]] - 1 == matrix[now[0]][now[1] - 1]:
                    now = (now[0], now[1] - 1)
                elif now[1] != len(mmap[now[0]]) - 2 and matrix[now[0]][now[1]] - 1 == matrix[now[0]][now[1] + 1]:
                    now = (now[0], now[1] + 1)
            if now[0] != 0 and matrix[now[0] - 1][now[1]] == 1:
                self.rect.y += 50
            elif now[0] != len(mmap) - 2 and matrix[now[0] + 1][now[1]] == 1:
                self.rect.y -= 50
            elif now[1] != 0 and matrix[now[0]][now[1] - 1] == 1:
                self.rect.x += 50
            elif now[1] != len(mmap[now[0]]) - 2 and matrix[now[0]][now[1] + 1] == 1:
                self.rect.x -= 50
            cir = 0
            COLLISIONS[self.num] = self.rect
        cir += 1


# class Dart_Trap(pygame.sprite.Sprite):
#     def __init__(self, pos_x, pos_y, direction):
#         global COLLISIONS
#         super().__init__(player_group)
#         if direction == "r":
#             self.image = load_image("Dart_Trap.png")
#         elif direction == "l":
#             self.image = pygame.transform.flip(load_image("Dart_Trap.png"), True, False)
#         elif direction == "d":
#             self.image = pygame.transform.rotate(load_image("Dart_Trap.png"), 270)
#         elif direction == "u":
#             self.image = pygame.transform.rotate(load_image("Dart_Trap.png"), 90)
#         self.rect = self.image.get_rect().move(
#             50 * pos_x, 50 * pos_y)
#         # COLLISIONS.append(self.rect)


# class Arrow(pygame.sprite.Sprite):
#     def __init__(self, pos_x, pos_y, direction):
#         super().__init__(player_group)
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         if direction == "r":
#             self.image = load_image("Arrow.png")
#             self.rect = self.image.get_rect().move((self.pos_x + 1) * 50, self.pos_y * 50 + 35)
#         elif direction == "l":
#             self.image = pygame.transform.rotate(load_image("Arrow.png"), 180)
#             self.rect = self.image.get_rect().move(self.pos_x * 50 - self.image.get_width(), self.pos_y * 50 + 35)
#         elif direction == "d":
#             self.image = pygame.transform.rotate(load_image("Arrow.png"), 270)
#             self.rect = self.image.get_rect().move(self.pos_x * 50 + 5, (self.pos_y + 1) * 50)
#         elif direction == "u":
#             self.image = pygame.transform.rotate(load_image("Arrow.png"), 90)
#             self.rect = self.image.get_rect().move(self.pos_x * 50 + 35, self.pos_y * 50 - self.image.get_height())
#         self.direction = direction
#         self.pos = (self.rect.x, self.rect.y)
#
#     def update(self, k):
#         if self.rect.collidelist(COLLISIONS):
#             if self.direction == "l":
#                 self.rect.x -= 1
#             elif self.direction == "r":
#                 self.rect.x += 1
#             elif self.direction == "d":
#                 self.rect.y += 1
#             elif self.direction == "u":
#                 self.rect.y -= 1
#         else:
#             self.rect.x = self.pos[0]
#             self.rect.y = self.pos[1]
#             print(COLLISIONS)


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                Tile(x, y)
            elif level[y][x] == "^":
                Thorn(x, y, "up")
            elif level[y][x] == ">":
                Thorn(x, y, "right")
            elif level[y][x] == "<":
                Thorn(x, y, "left")
            elif level[y][x] == "-":
                Thorn(x, y, "down")
            elif level[y][x] == '!':
                Win(x, y)
            elif level[y][x] == '@':
                xp, yp = x, y
            elif level[y][x] == '&':
                Spirit(x, y)
            elif level[y][x] == '$':
                AnimatedSprite(x * 50, y * 50)

    return xp, yp


def choose_level(level):
    global mmap, POSITION
    if level == "1":
        mmap = load_level('map.txt')
        POSITION = generate_level(mmap)
    elif level == "2":
        mmap = load_level('map2.txt')
        POSITION = generate_level(mmap)
    elif level == "3":
        mmap = load_level('map3.txt')
        POSITION = generate_level(mmap)


def delete_sprite():
    global all_sprites, tiles_group, player_group, animated_group, count
    count = 0
    for i in all_sprites:
        i.kill()
    for j in animated_group:
        j.kill()
    for i in player_group:
        i.kill()


def load_pers():
    global player_group
    player_group = pygame.sprite.Group()
    Character(all_sprites)


def database():
    db = sqlite3.connect("database.db")
    cur = db.cursor()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1440, 900
    screen = pygame.display.set_mode(size)
    a = start_menu(screen)
    pygame.display.flip()
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    animated_group = pygame.sprite.Group()
    choose_level(a)
    Character(all_sprites)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                e = pause(screen)
                if e:
                    delete_sprite()
                    if e == "1":
                        b = level_select(screen)
                        choose_level(b)
                        load_pers()
                    elif e == "0":
                        a = start_menu(screen)
                        choose_level(a)
                        load_pers()

                pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                all_sprites.update(screen, event)
        player_group.update(screen)
        animated_group.update()
        draw(screen)
        all_sprites.draw(screen)
        player_group.draw(screen)
        animated_group.draw(screen)
        pygame.display.flip()
        if winn:
            b = win(screen, count)
            delete_sprite()
            choose_level(b)
            load_pers()
            winn = False
            pygame.display.flip()
        if is_dead:
            lose(screen)
            pygame.display.flip()
            is_dead = False
        clock.tick(20)
    pygame.quit()
