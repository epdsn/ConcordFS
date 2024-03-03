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
plane_image = pygame.image.load('plane_pixel.png')
original_plane_image = plane_image

# Set up the initial position of the background
background_x = 0

# Set up the plane
plane_width = 50
plane_height = 50
plane_x = 100  # Initial x-coordinate of the plane
plane_y = screen_height - 62  # Initial y-coordinate of the plane

# Set up game loop
clock = pygame.time.Clock()

# Set up buttons
button_font = pygame.font.Font(None, 36)
stop_button_text = button_font.render('STOP', True, BUTTON_TEXT_COLOR)
stop_button_rect = stop_button_text.get_rect(topright=(screen_width - 10, 10))
reset_button_text = button_font.render('RESET', True, BUTTON_TEXT_COLOR)
reset_button_rect = reset_button_text.get_rect(topright=(screen_width - 10, 50))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the stop button is clicked
            if stop_button_rect.collidepoint(event.pos):
                # Pause the game (do nothing for now)
                pass
            # Check if the reset button is clicked
            elif reset_button_rect.collidepoint(event.pos):
                # Reset the game state (do nothing for now)
                pass

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
    if keys[pygame.K_DOWN]:
        plane_y += 5  # Move the plane down by increasing its y-coordinate

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

    # Draw background
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_image.get_width(), 0))

    # Draw runway
    pygame.draw.rect(screen, DARK_GREY, (runway_x, runway_y, runway_width, runway_height))

    # Draw plane
    screen.blit(plane_image, (plane_x, plane_y))

    # Draw buttons
    pygame.draw.rect(screen, BUTTON_COLOR, stop_button_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, reset_button_rect)
    pygame.draw.rect(screen, DARK_GREY, stop_button_rect, 2)  # Border
    pygame.draw.rect(screen, DARK_GREY, reset_button_rect, 2)  # Border
    screen.blit(stop_button_text, stop_button_rect)
    screen.blit(reset_button_text, reset_button_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
