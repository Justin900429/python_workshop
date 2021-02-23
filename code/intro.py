import pygame

# Init the pygame
pygame.init()

# Set the display window
screen = pygame.display.set_mode((500, 500))

# Run until the user asks to quit
running = True
while running:

    # Run through all the events
    for event in pygame.event.get():
        # If event type is QUIT
        if event.type == pygame.QUIT:
            running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()

# Quit the pygame
#  to release the resource
pygame.quit()

