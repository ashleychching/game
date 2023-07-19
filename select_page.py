import pygame
from screen_setup import setup_screen
from colors import Colors
from button import Button
window, screen_width, screen_height = setup_screen()

# return characters button
return_button_width = 50
return_button_height = 50
return_button_x = (screen_width - return_button_width) // 1.03
return_button_y = (screen_height - return_button_height) // 30
return_button_color = Colors.purple
return_button_hover_color = Colors.green
return_button_text = ""
return_button_text_color = Colors.white
return_button_font = pygame.font.Font(None, 32)
return_button_rect = pygame.Rect(
    return_button_x,
    return_button_y,
    return_button_width,
    return_button_height,
)
return_button_image = pygame.image.load("graphics/icons/white return.png")
return_button_image = pygame.transform.scale(return_button_image,
                                             (return_button_width / 1.3, return_button_height / 1.3))

def open_select_page():
    select_page_window = pygame.display.set_mode((screen_width, screen_height))
    select_page_running = True

    while select_page_running:
        select_page_window.fill(Colors.mint)
        return_button = Button(return_button_x, return_button_y, return_button_width, return_button_height,
                               return_button_color,
                               return_button_hover_color,
                               return_button_text, return_button_text_color, return_button_font,
                               pygame.quit,  # Close the current screen (select page)
                               border_radius=10,
                               image=return_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))
        return_button.draw(select_page_window)  # Draw the return button on the select page window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                select_page_running = False  # Exit the select page loop and close the screen
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if return_button_rect.collidepoint(mouse_pos):
                    select_page_running = False  # Exit the select page loop and close the screen

            # Handle other events specific to the select page

        pygame.display.update()

    # Return control to the main game loop when the select page is closed