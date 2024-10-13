import pygame
import sys
import random
from user_management import add_user, get_user_score, update_user_score

# Initializing Pygame
pygame.init()

# Setting up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jumble Japanese : Learn Japanese Game")

# Setting up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Sample Japanese sentences (unarranged)
sentences = [
    ("私は学生です。", "私 (わたし) は 学生 (がくせい) です。", "I am a student."),
    ("今日は天気がいいです。", "今日 (きょう) は 天気 (てんき) が いいです。", "The weather is nice today."),
    ("私は日本語を勉強しています。", "私 (わたし) は 日本語 (にほんご) を 勉強 (べんきょう) しています。", "I am studying Japanese.")
]

#fundtion to shuffle the words of a sentence
def shuffle_sentence(sentences):
    words = sentences.split(" ")
    random.shuffle(words)
    return " ".join(words)
    

#game loop
def main_game():
    running = True
    
    #getting the username. just using input for now
    username = input("Enter your username")
    
    #adding user and getting their score
    add_user(username)
    score = get_user_score(username)
    print(f"Current score: {score}")
    
    #selecting a random sentence
    original_sentence, kanji_sentence, translation = random.choice(sentences)

    #shuffling the words of the kanji sentence
    shuffled_sentence = shuffle_sentence(kanji_sentence)
    
    while running:
        # Filliing the screen with white
        screen.fill(WHITE)
        
        # displaying the shuffled sentence
        shuffled_text = font.render(f"Arrange: {shuffled_sentence}", True, BLACK)
        screen.blit(shuffled_text, (20, 150))
    
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
