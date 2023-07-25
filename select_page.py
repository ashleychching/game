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
return_button = Button(return_button_x, return_button_y, return_button_width, return_button_height,
                       return_button_color,
                       return_button_hover_color,
                       return_button_text, return_button_text_color, return_button_font,
                       pygame.quit,  # Close the current screen (select page)
                       border_radius=10,
                       image=return_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))

character_images = [pygame.image.load(f"graphics/doggos/doggo{i}/tile000.png") for i in range(1, 7)]

# Character selection variables
selected_character = 0
characters_rects = []

# Calculate the number of characters per row and column
characters_per_row = 3
characters_per_column = 2

# Calculate the width and height of the character images on the screen
character_image_width = 100
character_image_height = 100

# Calculate the gap between character images
character_gap_x = 40
character_gap_y = 40

# Calculate the total width and height of the characters section
characters_section_width = characters_per_row * (character_image_width + character_gap_x) - character_gap_x
characters_section_height = characters_per_column * (character_image_height + character_gap_y) - character_gap_y

# Calculate the starting position of the characters section
characters_section_start_x = (screen_width - characters_section_width) // 2
characters_section_start_y = (screen_height - characters_section_height) // 2
font = pygame.font.Font(None, 24)


def draw_characters():
    for i, image in enumerate(character_images):
        row = i // characters_per_row
        col = i % characters_per_row
        x = characters_section_start_x + col * (character_image_width + character_gap_x)
        y = characters_section_start_y + row * (character_image_height + character_gap_y)
        rect = pygame.Rect(x, y, character_image_width, character_image_height)
        characters_rects.append(rect)
        pygame.draw.rect(window, Colors.green, rect)
        window.blit(image, (x + 5, y + 5))


def open_select_page():
    select_page_window = pygame.display.set_mode((screen_width, screen_height))
    select_page_running = True
    global selected_character
    clock = pygame.time.Clock()

    while select_page_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                select_page_running = False  # Exit the select page loop and close the screen
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if return_button_rect.collidepoint(mouse_pos):
                    select_page_running = False  # Exit the select page loop and close the screen
                for i, rect in enumerate(characters_rects):
                    if rect.collidepoint(mouse_pos):
                        selected_character = i
                        select_page_running = False

        select_page_window.fill(Colors.mint)
        return_button.draw(select_page_window)  # Draw the return button on the select page window
        draw_characters()
        for i, image in enumerate(character_images):
            row = i // characters_per_row
            col = i % characters_per_row
            x = characters_section_start_x + col * (character_image_width + character_gap_x)
            y = characters_section_start_y + row * (character_image_height + character_gap_y)
            text = font.render(f"Doggo {i + 1}", True, Colors.black)
            window.blit(text, (x, y + character_image_height + 5))

            if selected_character == i:
                pygame.draw.rect(select_page_window, Colors.green,
                                 (x, y, character_image_width, character_image_height), 2)

        pygame.display.update()
        print("Selected Character:", selected_character)
    return selected_character
