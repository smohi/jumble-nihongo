import pygame
import sys

# Initializing Pygame
pygame.init()

# Setting up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Learn Japanese Game")

# Setting up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
while True:
    # Filliing the screen with white
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Updating the display
    pygame.display.update()
