import pygame
pygame.init()

screen_h = 400
screen_w = 800
screen = pygame.display.set_mode((screen_w, screen_h))
#vars
ball

run = True
while run:
    screen.fill((100, 255, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(10)
    pygame.display.update()
pygame.quit()


