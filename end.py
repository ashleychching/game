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

game_over = False


def end_screen():
    global game_over
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the left mouse button is clicked
                mouse_pos = pygame.mouse.get_pos()
                if replayRect.collidepoint(mouse_pos):
                    return True

        window.fill([255, 255, 255])  # Fill the window with white color
        window.blit(replay, replayRect)
        # Draw start screen elements
        # ...
        window.blit(play_again, playRect.topleft)
        pygame.display.flip()


