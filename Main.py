import pygame
pygame.init()
from levels import *
# Set screen size and create display surface
SCREEN_HEIGHT, SCREEN_WIDTH = 700, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load background image and scale it to fit the screen size
background_image = pygame.image.load('./Assets/Images/menu.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH+300, SCREEN_HEIGHT+200))
# Set font and render text
# font = pygame.font.SysFont('Arial', 20,bold=True)
font = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 45)

text = font.render("Yarn Ninja", True, (224,102,255))
text_rect = text.get_rect()
text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50)

# Set Start button properties
button_color = (104,34,139) # purple
button_text = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 12).render('    Click to Start     ', True, (255, 255, 255)) # white
button_text_rect = button_text.get_rect()
button_rect = pygame.Rect(SCREEN_WIDTH/2-100, SCREEN_HEIGHT-200, 200, 50)
button_text_rect.center = button_rect.center  # center the button text on the button


# Update display and wait for user input
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            if button_rect.collidepoint(mouse_pos):
                # Route to another scene
                print('Routing to Level 1.')
                from game import Game
                game = Game()
                game.main(2)
                # if x == "end":
                #     pygame.quit()
                #     quit()
            # if quit_button_rect.collidepoint(mouse_pos):
            #         pygame.quit()
            #         quit()

    # Blit background image, text, and button onto display surface
    screen.blit(background_image, (0, 0))
    screen.blit(text, text_rect)
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect)



    # screen.blit(text_surface, (60, screen_height-20))

    # Update the display using flip
    pygame.display.update()
