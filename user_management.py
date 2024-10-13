import sqlite3

#fundction to add a new user to the db
def add_user(username):
    connection = sqlite3.connect('game_data.db')
    cursor = connection.cursor()
    
    #insert new user with score 0
    cursor.execute('INSERT INTO users (username, score) VALUES(?,?)',(username, 0))
    connection.commit()
    connection.close()
    print(f"User '{username}' added with a score of 0")
    
#function to get user's score
def get_user_score(username):
    connection = sqlite3.connect('game_data.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT score FROM users WHERE username = ?',(username,))
    result = cursor.fetchone()
    
    if result:
        return result[0]
    else:
        print(f"User '{username}' not found.")
        return None
    
#function to update user's score
def update_user_score(username, score):
    connection = sqlite3.connect('game_data.db')
    cursor = connection.cursor()
    
    cursor.execute('UPDATE users SET score = ? WHERE username = ?', (score, username))
    connection.commit()
    connection.close()
    print(f"User '{username}' score updated to {score}")
    