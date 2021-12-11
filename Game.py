import random

import pygame
import os
import sys

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


class Arrow(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("bomb.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = START_POSITION

    def update(self, k,  *args):
        color = k.get_at((self.rect.x, self.rect.y))
        print(color)
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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    Arrow(all_sprites)
    # pygame.mouse.set_visible(False)
    running = True
    START_POSITION = [height, 0]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                all_sprites.update(screen, event)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 0), (0, 0, 100, 100))
        pygame.draw.rect(screen, (255, 255, 0), (width - 100, height - 200, 100, 100))
        pygame.draw.rect(screen, (255, 255, 0), (50, height - 100, 100, 100))
        pygame.draw.rect(screen, (255, 255, 0), (width - 200, 200, 100, 100))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
