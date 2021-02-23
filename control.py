import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Run through all the events
    for event in pygame.event.get():
        # The key user hit
        if event.type == KEYDOWN:
            # User can also press ESC to leave
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                print("Detect up key!")
            elif event.key == K_DOWN:
                print("Detect down key!")
            elif event.key == K_LEFT:
                print("Detect left key!")
            elif event.key == K_RIGHT:
                print("Detect right key!")
        # User click the exit window
        elif event.type == QUIT:
            running = False

# Remember to quit the pygame
#  to release the pygame resource
pygame.quit()
