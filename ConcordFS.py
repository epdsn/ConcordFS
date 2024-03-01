import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flight Simulator")

# Set up colors
WHITE = (255, 255, 255)

# Load images
background_image = pygame.image.load('background.jpg')
plane_image = pygame.image.load('plane.png')

# Set up the plane
plane_width = 50
plane_height = 50
plane_x = screen_width // 2 - plane_width // 2
plane_y = screen_height - 100

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
    if keys[pygame.K_LEFT]:
        plane_x -= 5
    if keys[pygame.K_RIGHT]:
        plane_x += 5
    if keys[pygame.K_UP]:
        plane_y -= 5
    if keys[pygame.K_DOWN]:
        plane_y += 5

    # Keep plane within screen boundaries
    plane_x = max(0, min(plane_x, screen_width - plane_width))
    plane_y = max(0, min(plane_y, screen_height - plane_height))

    # Clear the screen
    screen.fill(WHITE)

    # Draw background and plane
    screen.blit(background_image, (0, 0))
    screen.blit(plane_image, (plane_x, plane_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
