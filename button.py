import pygame
from screen_setup import setup_screen

window, screen_width, screen_height = setup_screen()


class Button:
    def __init__(self, x, y, width, height, color, hover_color, text, text_color, font, action, border_radius=0,
                 image=None, shadow_color=None, shadow_offset=(2, 2)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.hovered = False
        self.action = action
        self.border_radius = border_radius
        self.image = image
        self.shadow_color = shadow_color
        self.shadow_offset = shadow_offset

    def draw(self, surface):
        if self.shadow_color:
            shadow_rect = self.rect.move(self.shadow_offset)
            pygame.draw.rect(surface, self.shadow_color, shadow_rect, border_radius= self.border_radius)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, self.hover_color, self.rect, border_radius=self.border_radius)
        else:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=self.border_radius)
        if self.image:
            image_rect = self.image.get_rect(center=self.rect.center)
            surface.blit(self.image, image_rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()
