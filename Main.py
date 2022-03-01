import pygame


def start_menu(screen):
    size = width, height = 1440, 900
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
                result = level_select(screen)
                running = False
                return result
            elif event.type == pygame.MOUSEBUTTONDOWN and exit:
                quit()


def level_select(screen):
    size = width, height = 1440, 900
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text_choose_level = font.render("Выберите уровень", True, pygame.Color("yellow"))
    text_level_1 = font.render("1", True, pygame.Color("yellow"))
    text_level_2 = font.render("2", True, pygame.Color("yellow"))
    text_level_3 = font.render("3", True, pygame.Color("yellow"))
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

    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 160, text_y - 10,
                                                      text_w + 40, text_h + 20), 1)

    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 20, text_y - 10,
                                                      text_w + 40, text_h + 20), 1)

    pygame.draw.rect(screen, pygame.Color("red"), (text_x + 120, text_y - 10,
                                                   text_w + 40, text_h + 20), 1)

    pygame.draw.rect(screen, pygame.Color("red"), (text_x + 260, text_y - 10,
                                                   text_w + 40, text_h + 20), 1)
    pygame.display.flip()

    upper_l_angle_level_1 = (text_x - 300, text_y - 10)
    lower_r_angle_level_1 = ((text_x - 300) + (text_w + 40), (text_y - 10) + (text_h + 20))

    upper_l_angle_level_2 = (text_x - 160, text_y - 10)
    lower_r_angle_level_2 = ((text_x - 160) + (text_w + 20), (text_y - 10) + (text_h + 20))

    upper_l_angle_level_3 = (text_x - 20, text_y - 10)
    lower_r_angle_level_3 = ((text_x - 20) + (text_w + 20), (text_y - 10) + (text_h + 20))

    upper_l_angle_level_4 = (text_x - 10, text_y + 50)
    lower_r_angle_level_4 = ((text_x - 10) + (text_w + 20), (text_y + 50) + (text_h + 20))

    upper_l_angle_level_5 = (text_x - 10, text_y + 50)
    lower_r_angle_level_5 = ((text_x - 10) + (text_w + 20), (text_y + 50) + (text_h + 20))

    running = True
    press = False
    press2 = False
    press3 = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                if upper_l_angle_level_1[0] < event.pos[0] < lower_r_angle_level_1[0] and \
                        upper_l_angle_level_1[1] < event.pos[1] < lower_r_angle_level_1[1]:
                    press = True
                elif upper_l_angle_level_2[0] < event.pos[0] < lower_r_angle_level_2[0] and \
                        upper_l_angle_level_2[1] < event.pos[1] < lower_r_angle_level_2[1]:
                    press2 = True
                elif upper_l_angle_level_3[0] < event.pos[0] < lower_r_angle_level_3[0] and \
                        upper_l_angle_level_3[1] < event.pos[1] < lower_r_angle_level_3[1]:
                    press3 = True
                else:
                    press = False
                    press2 = False
                    press3 = False
            if event.type == pygame.MOUSEBUTTONDOWN and press:
                running = False
                return "1"
            if event.type == pygame.MOUSEBUTTONDOWN and press2:
                running = False
                return "2"
            if event.type == pygame.MOUSEBUTTONDOWN and press3:
                running = False
                return "3"


def pause(screen):
    print("work")
    size = width, height = 1440, 900
    screen.fill((120, 120, 120), pygame.Rect(520, 0, 400, 900))
    pygame.draw.line(screen, (100, 100, 100), (530, 0), (530, 900), width=20)
    pygame.draw.line(screen, (100, 100, 100), (530, 890), (919, 890), width=20)

    image2 = pygame.image.load('data/pause.png').convert_alpha()
    screen.blit(image2, (680, 50))

    font = pygame.font.Font(None, 50)
    text_play = font.render("Продолжить", True, pygame.Color("yellow"))
    text_x = width // 2 - text_play.get_width() // 2 + 10
    text_y = height // 2 - text_play.get_height() // 2 - 150
    text_w = text_play.get_width()
    text_h = text_play.get_height()
    screen.blit(text_play, (text_x, text_y + 80))
    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 10, text_y + 70,
                                                      text_w + 20, text_h + 20), 4)

    text_l_select = font.render("Выбор уровня", True, pygame.Color("yellow"))
    text_x = width // 2 - text_l_select.get_width() // 2 + 10
    text_y = height // 2 - text_l_select.get_height() // 2 - 150
    text_w = text_l_select.get_width()
    text_h = text_l_select.get_height()
    screen.blit(text_l_select, (text_x, text_y + 195))
    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 10, text_y + 185,
                                                      text_w + 20, text_h + 20), 4)

    text_exit = font.render("В меню", True, pygame.Color("yellow"))
    text_x = width // 2 - text_exit.get_width() // 2 + 10
    text_y = height // 2 - text_exit.get_height() // 2 - 150
    text_w = text_exit.get_width()
    text_h = text_exit.get_height()
    screen.blit(text_exit, (text_x, text_y + 310))
    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 10, text_y + 300,
                                                      text_w + 20, text_h + 20), 4)

    upper_l_angle_play = (text_x - 10, text_y + 70)
    lower_r_angle_play = ((text_x - 10) + (text_w + 20), (text_y + 70) + (text_h + 20))
    upper_l_angle_lvl_select = (text_x - 10, text_y + 185)
    lower_r_angle_lvl_select = ((text_x - 10) + (text_w + 20), (text_y + 185) + (text_h + 20))
    upper_l_angle_exit = (text_x - 10, text_y + 300)
    lower_r_angle_exit = ((text_x - 10) + (text_w + 20), (text_y + 300) + (text_h + 20))

    pygame.mouse.set_visible(True)

    pygame.display.flip()

    press = False
    l_sel = False
    exit = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mouse.set_visible(False)
                running = False
            if event.type == pygame.MOUSEMOTION:
                if upper_l_angle_play[0] < event.pos[0] < lower_r_angle_play[0] and \
                        upper_l_angle_play[1] < event.pos[1] < lower_r_angle_play[1]:
                    press = True
                elif upper_l_angle_exit[0] < event.pos[0] < lower_r_angle_exit[0] and \
                        upper_l_angle_exit[1] < event.pos[1] < lower_r_angle_exit[1]:
                    exit = True
                elif upper_l_angle_lvl_select[0] < event.pos[0] < lower_r_angle_lvl_select[0] and \
                        upper_l_angle_lvl_select[1] < event.pos[1] < lower_r_angle_lvl_select[1]:
                    l_sel = True
                else:
                    l_sel = False
                    exit = False
                    press = False
            if event.type == pygame.MOUSEBUTTONDOWN and press:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and exit:
                return "0"
 #               running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and l_sel:
                return "1"
   #             running = False



def win(screen, monet):
    size = width, height = 1440, 900
    screen.fill((0, 0, 0), pygame.Rect(470, 0, 500, 900))

    font = pygame.font.Font(None, 50)
    text_level_completed = font.render("Уровень завершен!", True, pygame.Color("green"))

    text_coins_collected = font.render("Монет собрано:", True, pygame.Color("green"))

    text_coins_collected_quanity = font.render(str(monet), True, pygame.Color("yellow"))

    text_b_select_level = font.render("К выбору уровней", True, (19, 108, 191))

    text_x = width // 2 - text_level_completed.get_width() // 2
    text_y = height // 2 - text_level_completed.get_height() // 2

    screen.blit(text_level_completed, (width // 2 - text_level_completed.get_width() // 2, 30))
    screen.blit(text_coins_collected, (text_x, text_y - 60))

    screen.blit(text_coins_collected_quanity, (text_x + 160, text_y))
    text_w = text_coins_collected_quanity.get_width()
    text_h = text_coins_collected_quanity.get_height()
    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x + 150, text_y - 5,
                                                      text_w + 20, text_h + 10), 4)

    screen.blit(text_b_select_level, (text_x, text_y + 300))
    text_w = text_b_select_level.get_width()
    text_h = text_b_select_level.get_height()
    pygame.draw.rect(screen, (19, 108, 191), (text_x - 10, text_y + 290,
                                              text_w + 20, text_h + 20), 4)

    upper_l_angle_b_select_level = (text_x - 10, text_y + 290)
    lower_r_angle_b_select_level = ((text_x - 10) + (text_w + 20), (text_y + 290) + (text_h + 20))

    pygame.mouse.set_visible(True)

    pygame.display.flip()

    running = True
    b_select_level = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                if upper_l_angle_b_select_level[0] < event.pos[0] < lower_r_angle_b_select_level[0] and \
                        upper_l_angle_b_select_level[1] < event.pos[1] < lower_r_angle_b_select_level[1]:
                    b_select_level = True
                else:
                    b_select_level = False
            if event.type == pygame.MOUSEBUTTONDOWN and b_select_level:
                running = False
                result = level_select(screen)
                return result


def lose(screen):
    size = width, height = 1440, 900
    screen.fill((0, 0, 0), pygame.Rect(470, 0, 500, 900))

    font = pygame.font.Font(None, 50)
    text_level_failed = font.render("Вы умерли:(", True, pygame.Color("red"))

    text_try_again = font.render("Побробовать снова", True, pygame.Color("yellow"))

    text_b_select_level = font.render("К выбору уровней", True, (19, 108, 191))

    text_x = width // 2 - text_level_failed.get_width() // 2
    text_y = height // 2 - text_level_failed.get_height() // 2

    screen.blit(text_level_failed, (width // 2 - text_level_failed.get_width() // 2, 30))

    screen.blit(text_try_again, (text_x - 60, text_y))
    text_w = text_try_again.get_width()
    text_h = text_try_again.get_height()
    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 70, text_y - 5,
                                                      text_w + 20, text_h + 10), 4)

    screen.blit(text_b_select_level, (text_x - 50, text_y + 300))
    text_w = text_b_select_level.get_width()
    text_h = text_b_select_level.get_height()
    pygame.draw.rect(screen, (19, 108, 191), (text_x - 60, text_y + 290,
                                              text_w + 20, text_h + 20), 4)

    upper_l_angle_b_select_level = (text_x - 60, text_y + 290)
    lower_r_angle_b_select_level = ((text_x - 60) + (text_w + 20), (text_y + 290) + (text_h + 20))

    upper_l_angle_try_again = (text_x - 70, text_y - 5)
    lower_r_angle_try_again = ((text_x - 70) + (text_w + 20), (text_y - 5) + (text_h + 20))

    pygame.mouse.set_visible(True)

    pygame.display.flip()

    running = True
    b_select_level = False
    try_again = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                if upper_l_angle_b_select_level[0] < event.pos[0] < lower_r_angle_b_select_level[0] and \
                        upper_l_angle_b_select_level[1] < event.pos[1] < lower_r_angle_b_select_level[1]:
                    b_select_level = True
                elif upper_l_angle_try_again[0] < event.pos[0] < lower_r_angle_try_again[0] and \
                        upper_l_angle_try_again[1] < event.pos[1] < lower_r_angle_try_again[1]:
                    try_again = True
                else:
                    b_select_level = False
                    try_again = False
            if event.type == pygame.MOUSEBUTTONDOWN and b_select_level:
                running = False
                result = level_select(screen)
                return result
            if event.type == pygame.MOUSEBUTTONDOWN and try_again:
                running = False
                return "try_again"


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1440, 900
    screen = pygame.display.set_mode(size)
    start_menu(screen)
    pygame.display.flip()
