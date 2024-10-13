import pygame
import sys
from user_management import add_user, get_user_score, update_user_score

# Initializing Pygame
pygame.init()

# Setting up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jumble Japanese : Learn Japanese Game")

# Setting up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#game loop
def main_game():
    running = True
    
    #getting the username. just using input for now
    username = input("Enter your username")
    
    #adding user and getting their score
    add_user(username)
    score = get_user_score(username)
    print(f"Current score: {score}")
    
    while running:
        # Filliing the screen with white
        screen.fill(WHITE)
    
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Updating the display
        pygame.display.update()
    
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main_game()
