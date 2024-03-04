import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Concorde Flight Simulator")

# Set up colors
WHITE = (255, 255, 255)
DARK_GREY = (50, 50, 50)
BUTTON_COLOR = (0, 150, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Set up the runway
runway_width = screen_width
runway_height = 25
runway_x = 0
runway_y = screen_height - 50

# Load images
background_image = pygame.image.load('background_pixel.jpg')
start_screen_background = pygame.image.load('start_screen_background.png')
plane_image = pygame.image.load('plane_pixel.png')
original_plane_image = plane_image

# Set up the initial position of the background
background_x = 0

# Set up the plane
plane_width = 50
plane_height = 50
plane_x = 100  # Initial x-coordinate of the plane
plane_y = screen_height // 2  + 100  # Initial y-coordinate of the plane

# Set up game loop
clock = pygame.time.Clock()

# Set up buttons
button_font = pygame.font.Font(None, 36)
start_button_text = button_font.render('START', True, BUTTON_TEXT_COLOR)
start_button_rect = start_button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 225))

# Angle of rotation for the plane
plane_angle = 0

# Main game loop
start_screen = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if start_screen:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    start_screen = False  # Start the game when the start button is clicked

    if not start_screen:  # If not in the start screen
        # Handle key events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            plane_image = pygame.transform.flip(original_plane_image, True, False)  # Flip the plane horizontally
            plane_x -= 5  # Move the plane left by decreasing its x-coordinate
        if keys[pygame.K_RIGHT]:
            plane_image = original_plane_image  # Reset the plane image to its original orientation
            plane_x += 5  # Move the plane right by increasing its x-coordinate
        if keys[pygame.K_UP]:
            plane_y -= 2  # Move the plane up by decreasing its y-coordinate
            # plane_angle = -5  # Adjust the angle of rotation when K_UP is pressed
        if keys[pygame.K_DOWN]:
            plane_y += 5  # Move the plane down by increasing its y-coordinate
            # plane_angle = 5  # Adjust the angle of rotation when K_DOWN is pressed

        # Keep plane within screen boundaries
        plane_x = max(0, min(plane_x, screen_width - plane_width))
        plane_y = max(0, min(plane_y, screen_height - plane_height))

        # Update the position of the background
        background_x -= 1  # Adjust the scrolling speed here

        # If the background has scrolled off the screen, reset its position
        if background_x <= -background_image.get_width():
            background_x = 0

    # Clear the screen
    screen.fill(WHITE)

    if start_screen:
        # Draw start screen background
        screen.blit(start_screen_background, (0, 0))

        # Draw start screen
        pygame.draw.rect(screen, BUTTON_COLOR, start_button_rect)
        pygame.draw.rect(screen, DARK_GREY, start_button_rect, 2)  # Border
        screen.blit(start_button_text, start_button_rect)

    else:  # If not in the start screen
        # Draw background
        screen.blit(background_image, (background_x, 0))
        screen.blit(background_image, (background_x + background_image.get_width(), 0))

        # Draw runway
        pygame.draw.rect(screen, DARK_GREY, (runway_x, runway_y, runway_width, runway_height))

        # Rotate the plane image
        rotated_plane = pygame.transform.rotate(plane_image, plane_angle)

        # Draw plane
        screen.blit(rotated_plane, (plane_x, plane_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
