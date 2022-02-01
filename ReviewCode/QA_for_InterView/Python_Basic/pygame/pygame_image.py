import pygame


def game_image():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((255, 255, 255))
    ball_image = pygame.image.load(r'E:\李震祥\PYGIT\PYref\ReviewCode\QA_for_InterView'
                                   r'\Python_Basic\pygame\img\ball.png')
    screen.blit(ball_image, (50, 50))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
game_image()