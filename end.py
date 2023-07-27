import pygame
from screen_setup import setup_screen

# Initialize pygame
pygame.init()
window, screen_width, screen_height = setup_screen()

play_again = pygame.image.load('graphics/play again text.png')
play_again = pygame.transform.scale_by(play_again, (.5, .5))
playRect = play_again.get_rect()
playRect.center = (screen_width / 2, screen_height / 3)

replay = pygame.image.load('graphics/icons/replay.png')
replay = pygame.transform.scale_by(replay, (.15, .15))
replayRect = replay.get_rect()
replayRect.center = (screen_width / 2, screen_height / 1.7)


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
        window.blit(replay, replayRect)
        # Draw start screen elements
        # ...
        window.blit(play_again, playRect.topleft)
        pygame.display.flip()


# Call the start_screen() function when the module is executed directly
if __name__ == "__main__":
    end_screen()
