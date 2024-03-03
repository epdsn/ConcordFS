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

# Set up the rectangle
rect_width = screen_width / 2
rect_height = 25
rect_x = 10
rect_y = screen_height - 50

# Load images
background_image = pygame.image.load('background_pixel.jpg')
plane_image = pygame.image.load('plane_pixel.png')

# Set up the initial position of the background
background_x = 0

# Set up the plane
plane_width = 50
plane_height = 50
plane_x = 100 #screen_width // 2 - plane_width // 2
plane_y = screen_height - 62

# Set up game loop
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key events
    keys = pygame.key.get_pressed()
    #Turning off left
    #if keys[pygame.K_LEFT]:
        #plane_x -= 5
    if keys[pygame.K_RIGHT]:
        plane_x += 5
    if keys[pygame.K_UP]:
        plane_y -= 2
    if keys[pygame.K_DOWN]:
        plane_y += 5

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
    pygame.draw.rect(screen, DARK_GREY, (rect_x, rect_y, rect_width, rect_height))

    # Draw plane
    screen.blit(plane_image, (plane_x, plane_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
