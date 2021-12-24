import pygame


def start_menu(screen):
    size = width, height = 800, 600
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text_play = font.render("Играть", True, pygame.Color("yellow"))
    text_x = width // 2 - text_play.get_width() // 2
    text_y = height // 2 - text_play.get_height() // 2 - 150
    text_w = text_play.get_width()
    text_h = text_play.get_height()
    screen.blit(text_play, (text_x, text_y + 60))
    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 10, text_y + 50,
                                                      text_w + 20, text_h + 20), 1)

    text_exit = font.render("Выйти", True, pygame.Color("yellow"))
    screen.blit(text_exit, (text_x, text_y + 200))
    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 10, text_y + 190,
                                                      text_w + 20, text_h + 20), 1)

    upper_l_angle_play = (text_x - 10, text_y + 50)
    lower_r_angle_play = ((text_x - 10) + (text_w + 20), (text_y + 50) + (text_h + 20))
    upper_l_angle_exit = (text_x - 10, text_y + 200)
    lower_r_angle_exit = ((text_x - 10) + (text_w + 20), (text_y + 190) + (text_h + 20))

    pygame.display.flip()

    press = False
    exit = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                if upper_l_angle_play[0] < event.pos[0] < lower_r_angle_play[0] and \
                        upper_l_angle_play[1] < event.pos[1] < lower_r_angle_play[1]:
                    press = True
                elif upper_l_angle_exit[0] < event.pos[0] < lower_r_angle_exit[0] and \
                        upper_l_angle_exit[1] < event.pos[1] < lower_r_angle_exit[1]:
                    exit = True
                else:
                    exit = False
                    press = False
            if event.type == pygame.MOUSEBUTTONDOWN and press:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and exit:
                quit()


def level_select(screen):
    size = width, height = 800, 600
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text_choose_level = font.render("Выберите уровень", True, pygame.Color("yellow"))
    text_level_1 = font.render("1", True, pygame.Color("yellow"))
    text_level_2 = font.render("2", True, pygame.Color("red"))
    text_level_3 = font.render("3", True, pygame.Color("red"))
    text_level_4 = font.render("4", True, pygame.Color("red"))
    text_level_5 = font.render("5", True, pygame.Color("red"))
    text_x = width // 2 - text_level_1.get_width() // 2
    text_y = height // 2 - text_level_1.get_height() // 2

    screen.blit(text_choose_level, (width // 2 - text_choose_level.get_width() // 2, 30))
    screen.blit(text_level_1, (text_x - 280, text_y))
    screen.blit(text_level_2, (text_x - 140, text_y))
    screen.blit(text_level_3, (text_x, text_y))
    screen.blit(text_level_4, (text_x + 140, text_y))
    screen.blit(text_level_5, (text_x + 280, text_y))

    text_w = text_level_1.get_width()
    text_h = text_level_1.get_height()

    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 300, text_y - 10,
                                                      text_w + 40, text_h + 20), 1)

    pygame.draw.rect(screen, pygame.Color("red"), (text_x - 160, text_y - 10,
                                                   text_w + 40, text_h + 20), 1)

    pygame.draw.rect(screen, pygame.Color("red"), (text_x - 20, text_y - 10,
                                                   text_w + 40, text_h + 20), 1)

    pygame.draw.rect(screen, pygame.Color("red"), (text_x + 120, text_y - 10,
                                                   text_w + 40, text_h + 20), 1)

    pygame.draw.rect(screen, pygame.Color("red"), (text_x + 260, text_y - 10,
                                                   text_w + 40, text_h + 20), 1)
    pygame.display.flip()

    upper_l_angle_level_1 = (text_x - 300, text_y - 10)
    lower_r_angle_level_1 = ((text_x - 300) + (text_w + 40), (text_y - 10) + (text_h + 20))

    upper_l_angle_level_2 = (text_x - 10, text_y + 50)
    lower_r_angle_level_2 = ((text_x - 10) + (text_w + 20), (text_y + 50) + (text_h + 20))

    upper_l_angle_level_3 = (text_x - 10, text_y + 50)
    lower_r_angle_level_3 = ((text_x - 10) + (text_w + 20), (text_y + 50) + (text_h + 20))

    upper_l_angle_level_4 = (text_x - 10, text_y + 50)
    lower_r_angle_level_4 = ((text_x - 10) + (text_w + 20), (text_y + 50) + (text_h + 20))

    upper_l_angle_level_5 = (text_x - 10, text_y + 50)
    lower_r_angle_level_5 = ((text_x - 10) + (text_w + 20), (text_y + 50) + (text_h + 20))

    running = True
    press = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                if upper_l_angle_level_1[0] < event.pos[0] < lower_r_angle_level_1[0] and \
                        upper_l_angle_level_1[1] < event.pos[1] < lower_r_angle_level_1[1]:
                    press = True
                else:
                    press = False
            if event.type == pygame.MOUSEBUTTONDOWN and press:
                running = False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    start_menu(screen)
    pygame.display.flip()
