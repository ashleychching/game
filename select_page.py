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
# choose characters button
choose_button_width = 50
choose_button_height = 50
choose_button_x = (screen_width - choose_button_width) // 30
choose_button_y = (screen_height - choose_button_height) // 30
choose_button_color = Colors.purple
choose_button_hover_color = Colors.green
choose_button_text = ""
choose_button_text_color = Colors.white
choose_button_font = pygame.font.Font(None, 32)
choose_button_rect = pygame.Rect(
    choose_button_x,
    choose_button_y,
    choose_button_width,
    choose_button_height,
)
choose_button_image = pygame.image.load("graphics/icons/white play.png")
choose_button_image = pygame.transform.scale(choose_button_image,
                                             (choose_button_width / 1.3, choose_button_height / 1.3))

choose_button = Button(choose_button_x, choose_button_y, choose_button_width, choose_button_height,
                       choose_button_color,
                       choose_button_hover_color,
                       choose_button_text, choose_button_text_color, choose_button_font,
                       pygame.quit,  # Close the current screen (select page)
                       border_radius=10,
                       image=choose_button_image, shadow_color=Colors.green, shadow_offset=(7, 7))

character_images = [pygame.image.load(f"graphics/doggos/doggo{i}/tile000.png") for i in range(1, 7)]

# Character selection variables
selected_character = 0
characters_rects = []

# Calculate the number of characters that can be displayed on the screen at once
max_characters_displayed = 5
# Calculate the width of the character images on the screen
character_image_width = 100
# Calculate the gap between character images
character_gap = 40
font = pygame.font.Font(None, 40)

# Calculate the total width of the characters section
characters_section_width = (max_characters_displayed * (character_image_width + character_gap)) - character_gap
characters_section_start_x = (screen_width - characters_section_width) // 2


def draw_characters():
    # Calculate the total number of characters available
    total_characters = len(character_images)
    print(len(character_images))

    # Calculate the start and end indices for the characters to be displayed in the viewport
    start_index = max(selected_character - (max_characters_displayed // 2), 0)
    end_index = min(start_index + max_characters_displayed, total_characters)

    # Adjust start_index if there are fewer characters than max_characters_displayed
    start_index = max(end_index - max_characters_displayed, 0)

    for i in range(start_index, end_index):
        image = character_images[i]
        x = characters_section_start_x + i * (character_image_width + character_gap)
        y = 250
        rect = pygame.Rect(x, y, character_image_width, character_image_width)
        characters_rects.append(rect)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_character = max(selected_character - 1, 0)
                elif event.key == pygame.K_RIGHT:
                    selected_character = min(selected_character + 1, len(character_images) - 1)
        select_page_window.fill(Colors.mint)
        return_button.draw(select_page_window)  # Draw the return button on the select page window
        draw_characters()
        for i, image in enumerate(character_images):
            x = characters_section_start_x + i * (character_image_width + character_gap)
            y = 380
            text = font.render(f"Doggo {i + 1}", True, Colors.black)
            window.blit(text, (x, y))
            choose_button.draw(select_page_window)
            if selected_character == i:
                pygame.draw.rect(window, Colors.green, (x, y + 40, character_image_width, 5), border_radius=2)

            # Handle other events specific to the select page

        pygame.display.update()
        print("Selected Character:", selected_character)

    # Return control to the main game loop when the select page is closed
