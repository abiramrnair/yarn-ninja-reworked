import pygame
pygame.init()

# Set screen size and create display surface
SCREEN_HEIGHT, SCREEN_WIDTH = 700, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load background image and scale it to fit the screen size
background_image = pygame.image.load('../../../PycharmProjects/yarn-ninja-reworked/Assets/Images/game_background.jpg')
background_image = pygame.transform.scale(background_image, (800, 800))

# Set font and render text
# font = pygame.font.SysFont('Arial', 20,bold=True)
font = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 40)

text = font.render("Yarn Ninja", True, (0, 0, 0)) # black
text_rect = text.get_rect()
text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100)

# Set Start button properties
button_color = (50, 200, 70) # green
button_text = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 14).render('Start', True, (255, 255, 255)) # white
button_text_rect = button_text.get_rect()
button_rect = pygame.Rect(SCREEN_WIDTH/2-100, SCREEN_HEIGHT-200, 200, 50)
button_text_rect.center = button_rect.center  # center the button text on the button

# Quit button
quit_button_text = pygame.font.Font('./Assets/Fonts/8-BIT WONDER.ttf', 14).render('  Exit', True, (255, 255, 255)) # white
quit_button_text_rect = button_text.get_rect()
quit_button_rect = pygame.Rect(SCREEN_WIDTH/2-100, SCREEN_HEIGHT-100, 200, 50)
quit_button_text_rect.center = quit_button_rect.center  # center the button text on the button




# Update display and wait for user input
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                # Route to another scene
                print('Routing to Level 1.')
                import game
                x = game.main()
                if x == "end":
                    pygame.quit()
                    quit()
            elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

    # Blit background image, text, and button onto display surface
    screen.blit(background_image, (0, 0))
    screen.blit(text, text_rect)
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect)

    pygame.draw.rect(screen, button_color, quit_button_rect)
    screen.blit(quit_button_text, quit_button_text_rect)


    # screen.blit(text_surface, (60, screen_height-20))

    # Update the display using flip
    pygame.display.update()