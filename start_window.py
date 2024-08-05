import pygame
import sys
import networkcontroller

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Football Game')


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.SysFont(None, 55)

background_image = pygame.image.load('balls.webp')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

button_width = 300
button_height = 100
button_color = GREEN
button_hover_color = (150, 255, 150)
button_rect = pygame.Rect((screen_width // 2 - button_width // 2,
                           screen_height // 2 - button_height // 2),
                          (button_width, button_height))

text = font.render('Start Game', True, BLACK)
text_rect = text.get_rect(center=button_rect.center)

def main_menu():
    while True:
        screen.blit(background_image, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, button_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)

        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(mouse_pos):
                    create_game = networkcontroller.network_controller.create_game()
                    print("game started, game_id:", create_game, "game url: https://test-fac11-default-rtdb.europe-west1.firebasedatabase.app/"+str(create_game)+".json")
                    exit()

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
