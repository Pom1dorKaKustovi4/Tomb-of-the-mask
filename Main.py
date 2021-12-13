import pygame


def start_menu(screen):
    size = width, height = 800, 600
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Играть", True, pygame.Color("yellow"))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, pygame.Color("yellow"), (text_x - 10, text_y - 10,
                                                      text_w + 20, text_h + 20), 1)
    upper_l_angle = (text_x - 10, text_y - 10)
    lower_r_angle = ((text_x - 10) + (text_w + 20), (text_y - 10) + (text_h + 20))

    pygame.display.flip()

    press = False
    start = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEMOTION:
                if upper_l_angle[0] < event.pos[0] < lower_r_angle[0] and \
                        upper_l_angle[1] < event.pos[1] < lower_r_angle[1]:
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
