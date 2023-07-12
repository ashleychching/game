import pygame

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Start Screen")
play_again = pygame.image.load('graphics/play again text.png')
play_again = pygame.transform.scale_by(play_again, (.5, .5))
playRect = play_again.get_rect()
playRect.center = (screen_width / 2, screen_height / 3)


def end_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

        window.fill([255, 255, 255])  # Fill the window with white color

        # Draw start screen elements
        # ...
        window.blit(play_again, playRect.topleft)
        pygame.display.flip()


# Call the start_screen() function when the module is executed directly
if __name__ == "__main__":
    end_screen()
