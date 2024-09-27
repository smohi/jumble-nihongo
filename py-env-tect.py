import pygame
import sys
import sqlite3

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jumble Japanese")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to set up the SQLite database
def setup_database():
    # Connect to SQLite database (it will create a new file if it doesn't exist)
    connection = sqlite3.connect('game_data.db')
    
    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    
    # Create a table for users (only runs the first time)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        score INTEGER
    )
    ''')
    
    # Commit changes and close the connection
    connection.commit()
    connection.close()

# Set up the database
setup_database()

# Game loop
while True:
    # Fill the screen with white
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Display a message for confirmation
    font = pygame.font.Font(None, 36)
    text = font.render("Environment is set up! Press X to quit.", True, BLACK)
    screen.blit(text, (100, 250))
    
    # Update the display
    pygame.display.update()
