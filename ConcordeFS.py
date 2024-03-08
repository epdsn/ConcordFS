import pygame
import sys
import logging

# Configure logging
logging.basicConfig(filename='debug.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


# Initialize Pygame
pygame.init()

# Set up game loop
clock = pygame.time.Clock()

# Set up the screen
screen_width = 1000
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Concorde Flight Simulator 8-bit")

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
background_image = pygame.image.load('assets/images/background_pixel_001.jpg')
start_screen_background = pygame.image.load('assets/images/start_screen_image.png')
plane_image = pygame.image.load('assets/images/plane_pixel.png')
original_plane_image = plane_image
mountain_image = pygame.image.load('assets/images/mountain.png')

# Set up buttons
button_font = pygame.font.Font(None, 36)
start_button_text = button_font.render('START', True, BUTTON_TEXT_COLOR)
start_button_rect = start_button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 225))

# Set up the plane
plane_width = 50
plane_height = 50
plane_x = 100  # Initial x-coordinate of the plane
plane_y = screen_height // 2 + 100  # Initial y-coordinate of the plane

# Angle of rotation for the plane
plane_angle = 0

# Set up the initial position of the background
background_x = 0

# Set up speed values
forward_speed = 5
left_speed = 3
right_speed = 8

# Define obstacle class
class Obstacle:
    def __init__(self, x, y):
        self.image = mountain_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self, speed):
        self.rect.x -= speed

# Create a list to hold obstacles
obstacles = []
obstacle_frequency = 2000  # Add an obstacle every 100 pixels

# Main game loop
start_screen = True
running = True
rotated_plane = None  # Initialize rotated_plane outside of the game loop
plane_rect = None  # Initialize plane_rect outside of the game loop

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if start_screen:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if start_button_rect.collidepoint(event.pos):
                        start_screen = False  # Start the game when the start button is clicked
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    start_screen = False  # Start the game when the return key is pressed           
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    start_screen = True  # Go back to the start screen if Escape is pressed

                # Adjust speeds based on key presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        forward_speed = 50  # Set forward speed to 3 for mock speed 1
                    elif event.key == pygame.K_2:
                        forward_speed = 100  # Set forward speed to 5 for mock speed 2
                    elif event.key == pygame.K_3:
                        forward_speed = 200  # Set forward speed to 8 for mock speed 3
                    elif event.key == pygame.K_0:
                        forward_speed = 5  # back to normal speed

        if not start_screen:  # If not in the start screen
            # Handle key events
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                plane_x -= left_speed  # Move the plane left by decreasing its x-coordinate
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                plane_x += right_speed  # Move the plane right by increasing its x-coordinate
            if keys[pygame.K_s] or keys[pygame.K_UP]:
                plane_y -= 5.0  # Move the plane up by decreasing its y-coordinate
                plane_angle = 5  # Adjust the angle of rotation when K_UP is pressed
            if keys[pygame.K_w] or keys[pygame.K_DOWN]:
                plane_y = min(plane_y + 5, screen_height - plane_height - 25)  # Move the plane down by increasing its y-coordinate, but not below the bottom boundary
                plane_angle = -5  # Adjust the angle of rotation when K_DOWN is pressed

            # Keep plane within screen boundaries
            plane_x = max(0, min(plane_x, screen_width - plane_width))
            plane_y = max(0, min(plane_y, screen_height - plane_height))

            # Update the position of the background
            background_x -= forward_speed  # Adjust the scrolling speed here

            # If the background has scrolled off the screen, reset its position
            if background_x <= -background_image.get_width():
                background_x = 0

            # Add obstacles
            if len(obstacles) == 0 or obstacles[-1].rect.right < screen_width - obstacle_frequency:
                obstacles.append(Obstacle(screen_width, screen_height - mountain_image.get_height() - (runway_height * 2 + 10)))

            # Move obstacles
            for obstacle in obstacles:
                obstacle.move(forward_speed)

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

            # Inside the main game loop, after drawing the obstacles but before updating the display
            for obstacle in obstacles:
                if plane_rect and plane_rect.colliderect(obstacle.rect):
                    # Collision detected
                    # Implement collision response here
                    # For simplicity, let's reset the plane position
                    plane_x = 100
                    plane_y = screen_height // 2 + 100

            # Get the bounding rectangle of the rotated plane image
            plane_rect = rotated_plane.get_rect()
            # Set its position
            plane_rect.topleft = (plane_x, plane_y)

            # Draw plane
            screen.blit(rotated_plane, plane_rect)

            # Reset the angle when neither UP nor DOWN key is pressed
            if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                plane_angle = 0

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

except Exception as e:
    # Log errors to the file
    logging.error("An error occurred:", e)

# Quit Pygame
pygame.quit()
sys.exit()
