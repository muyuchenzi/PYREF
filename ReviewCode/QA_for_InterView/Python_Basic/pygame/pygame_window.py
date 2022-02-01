import pygame


def game_window():
    '''
    初始化pyGame 模块
    '''
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("大球吃小球")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

game_window()