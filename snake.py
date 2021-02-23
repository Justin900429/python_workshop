import pygame
import sys
import random
from pygame.locals import *

# Init pygame
pygame.init()
pygame.display.set_caption("Snake")
fps_clock = pygame.time.Clock()
FPS = 10

# Set the screen size
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400

# Make a grid with 10x10 pixels 
GRIDSIZE=10
# Get a grid size
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

# Set up the direction
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)


def draw_box(surf, color, pos):
    """Draw rectangle on surface

    Args:
    surf: Surface to draw rectangle
    color: The color of the rectangle
    pos: The top-left place of rectangle

    Return: None
    """

    # Create a rectangle object
    r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
    # Draw on the surface
    pygame.draw.rect(surf, color, r)


class Snake(object):
    def __init__(self):
        self.restart()
        self.color = (0,0,0)

    def get_head_position(self):
        """Return the head position (index 0) of snake

        Args:
            self: Instance itself

        Return: None
        """
        return self.positions[0]

    def restart(self):
        """Restart the game

        Args:
            self: Instance itself

        Return: None
        """
        # Reset the information of snake
        self.length = 1
        self.positions =  [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def point(self, pt):
        """Set the moving direction of snake

        Args:
            self: Instance itself
            pt: Direction of snake, include "UP", "DOWN", "LEFT" and "RIGHT"
        
        Return: None
        """
        # The snake couldn't change its moving direction oppositely
        #  if the length is greater than 1
        if (self.length <= 1) or \
            ((pt[0] * -1, pt[1] * -1) != self.direction):
            self.direction = pt

    def move(self):
        """Update the snake position according to its moving
        direction

        Args:
            self: Instance itself
        
        Return: None
        """
        # Get current position
        cur = self.positions[0]
        # Direction to move
        point_x, point_y = self.direction
        # New position
        new = (((cur[0]+point_x*GRIDSIZE) % SCREEN_WIDTH), (cur[1]+(point_y*GRIDSIZE)) % SCREEN_HEIGHT)

        # Check whether the snake will crash into itself
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.restart()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def draw(self, surf):
        """Draw the snake on the surface
        
        Args:
            self: Instace itself
            surf:, 
        """
        for p in self.positions:
            draw_box(surf, self.color, p)


class Apple(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (255,0,0)
        self.randomize()

    def randomize(self):
        """Randomly set the position of the apple

        Args:
            self: Instance itself

        Return: None
        """
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

    def draw(self, surf):
        """Draw the apple on the surface

        Args:
            self: Instance itself
            surf: Surface to draw on

        Return: None
        """
        draw_box(surf, self.color, self.position)

def check_eat(snake, apple):
    """Check whether snake eat the apple

    Args:
        snake: Snake object, used to obtain the head position of snake
        apple: Apple object, used to obtain the position of apple

    Return: None
    """

    if snake.get_head_position() == apple.position:
        # After eating an apple, increase length
        #  and regenerate the apple
        snake.length += 1
        apple.randomize()


if __name__ == '__main__':
    snake = Snake()
    apple = Apple()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    # Fill the background with white color
    surface = pygame.Surface(screen.get_size())
    surface.fill((255,255,255))

    # Running game
    while True:
        # Check for event type
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                elif event.key == pygame.K_UP:
                    snake.point(UP)
                elif event.key == pygame.K_DOWN:
                    snake.point(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.point(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.point(RIGHT)


        # Fill the surface
        surface.fill((255,255,255))

        # Move the snake and check whether snake eat the apple
        snake.move()
        check_eat(snake, apple)

        # Draw new snake and apple
        snake.draw(surface)
        apple.draw(surface)

        # Show the score
        font = pygame.font.Font(None, 36)
        text = font.render(str(snake.length), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = 20

        # Add object to the screen
        surface.blit(text, textpos)
        screen.blit(surface, (0,0))

        # Update the screen
        pygame.display.flip()
        pygame.display.update()
        fps_clock.tick(FPS + snake.length/3)
