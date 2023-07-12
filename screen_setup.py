import pygame


def setup_screen():
    # Initialize pygame
    pygame.init()

    # Set up the screen
    screen_width = 800
    screen_height = 600
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Park Run")

    return window,screen_width, screen_height
