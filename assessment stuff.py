import sys
import time
import random


def typewriter_effect(text): #typewriter function
    for char in text: #loop through each character in text
        sys.stdout.write(char) 
        sys.stdout.flush()   
        time.sleep(0.05)  # Adjust the speed of the typewriter effect
    print()

def typewriter_effect_fast(text): #fast typewriter effect
    for char in text: #loop through each character in text
        sys.stdout.write(char) 
        sys.stdout.flush()   
        time.sleep(0.0005)  # Adjust the speed of the typewriter effect
    print()
    
def grid_generator(connections, grid): #makes the base grid
    random.shuffle(connections) #shuffles the list of connections
    row = 0 #sets row to 0
    col = 0 #sets col to 0
    for connection in connections: 
        for word in connection["Words"]: # within the dictionary, get each word
            if row < len(grid) and col < len(grid[0]):  # Check if we're still within the grid boundaries of a 4 by 4
                grid[row][col] = word # put the word inside the grid 
                col += 1 # moves to the next col
                if col >= len(grid[0]):  # if col exceeds the grid size  
                    col = 0 #reset col to 0
                    row += 1 #move to the next row
                    if row >= len(grid):  # if row exceeds the grid size of 4
                        break # break the loop
    return grid  

def words_the_same_length(grid): #centres each word and adds spaces
    max_length = 20 #max length for a word and the spaces is 20
    neat_grid = [[word.center(max_length) for word in row] for row in grid]  # Add spaces to make all words the same length of 20 and centres word
    return neat_grid

def words_the_same_length_1(guessed_words): #centres each word and adds spaces
    max_length = 20 #max length for a word and the spaces is 20
    guessed_words = [[word.center(max_length) for word in row] for row in guessed_words]  # Add spaces to make all words the same length of 20 and centres word
    return guessed_words

def grid_shuffle(neat_grid): #shuffles the neat grid
    all_words_flat = [] 
    for row in neat_grid:
        for word in row: 
            all_words_flat.append(word) #adds each word from neat grid into a flat array
        
    random.shuffle(all_words_flat) # Shuffle the 1D list of all words

    shuffled_grid = []
    row_length = len(neat_grid[0])  # each row has the same number of words as base grid
    for i in range(0, len(all_words_flat), row_length): 
        row = []
        for j in range(row_length):
            row.append(all_words_flat[i+j]) #creates the words into rows
        shuffled_grid.append(row) #adds each row to shuffled grid
    return shuffled_grid

def print_grid(shuffled_grid, guessed_words): #prints the gameboard grid
    
    guessed_words = words_the_same_length_1(guessed_words)
    remaining_words = []

    for row in shuffled_grid:
        for word in row:
            if word.strip() not in [word.strip() for row in guessed_words for word in row]:
                remaining_words.append(word)  

    if len(guessed_words) == 0:
        typewriter_effect_fast("\033[01m________________________________________________________________________________________________")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {shuffled_grid[0][0]} || {shuffled_grid[0][1]} || {shuffled_grid[0][2]} || {shuffled_grid[0][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {shuffled_grid[1][0]} || {shuffled_grid[1][1]} || {shuffled_grid[1][2]} || {shuffled_grid[1][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {shuffled_grid[2][0]} || {shuffled_grid[2][1]} || {shuffled_grid[2][2]} || {shuffled_grid[2][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {shuffled_grid[3][0]} || {shuffled_grid[3][1]} || {shuffled_grid[3][2]} || {shuffled_grid[3][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\033[0m")
    
    elif len(guessed_words) == 1:
        typewriter_effect_fast(f"\033[92m________________________________________________________________________________________________")
        typewriter_effect_fast(f"|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[0][0]} || {guessed_words[0][1]} || {guessed_words[0][2]} || {guessed_words[0][3]} |")
        typewriter_effect_fast(f"|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"------------------------------------------------------------------------------------------------\033[00m")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {remaining_words[0]} || {remaining_words[1]} || {remaining_words[2]} || {remaining_words[3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {remaining_words[4]} || {remaining_words[5]} || {remaining_words[6]} || {remaining_words[7]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {remaining_words[8]} || {remaining_words[9]} || {remaining_words[10]} || {remaining_words[11]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    
    elif len(guessed_words) == 2:
        typewriter_effect_fast("\033[92m________________________________________________________________________________________________")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[0][0]} || {guessed_words[0][1]} || {guessed_words[0][2]} || {guessed_words[0][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("\033[33m------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[1][0]} || {guessed_words[1][1]} || {guessed_words[1][2]} || {guessed_words[1][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------\033[00m")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {remaining_words[0]} || {remaining_words[1]} || {remaining_words[2]} || {remaining_words[3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {remaining_words[4]} || {remaining_words[5]} || {remaining_words[6]} || {remaining_words[7]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    
    elif len(guessed_words) == 3:
        typewriter_effect_fast("\033[92m________________________________________________________________________________________________")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[0][0]} || {guessed_words[0][1]} || {guessed_words[0][2]} || {guessed_words[0][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("\033[33m------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[1][0]} || {guessed_words[1][1]} || {guessed_words[1][2]} || {guessed_words[1][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("\033[34m------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[2][0]} || {guessed_words[2][1]} || {guessed_words[2][2]} || {guessed_words[2][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------\033[00m")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {remaining_words[0]} || {remaining_words[1]} || {remaining_words[2]} || {remaining_words[3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    
    elif len(guessed_words) == 4:
        typewriter_effect_fast("\033[92m________________________________________________________________________________________________")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[0][0]} || {guessed_words[0][1]} || {guessed_words[0][2]} || {guessed_words[0][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("\033[33m------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[1][0]} || {guessed_words[1][1]} || {guessed_words[1][2]} || {guessed_words[1][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("\033[34m------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[2][0]} || {guessed_words[2][1]} || {guessed_words[2][2]} || {guessed_words[2][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("\033[95m------------------------------------------------------------------------------------------------")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast(f"| {guessed_words[3][0]} || {guessed_words[3][1]} || {guessed_words[3][2]} || {guessed_words[3][3]} |")
        typewriter_effect_fast("|                      ||                      ||                      ||                      |")
        typewriter_effect_fast("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\033[00m\033[02m")

def get_player_guess(lives, categories_remaining, neat_grid, guessed_words): #gets the players guesses
    has_player_guessed = False
    
    while has_player_guessed == False:
        typewriter_effect(f"\033[31mlives remaining = {lives}")
        typewriter_effect(f"\033[35mcategories remaining = {categories_remaining}\033[0m")
        typewriter_effect("Guess connected categories or Shuffle:")
        guess = input().split(',')  # Split input into a list of words
        
        if "Shuffle" in guess:
            shuffled_grid = grid_shuffle(neat_grid)
            print_grid(shuffled_grid, guessed_words)
            
        else:
            guess = [word.strip() for word in guess]  
            has_player_guessed = True 
            return guess

def check_if_won(categories_remaining):
    if categories_remaining == 0:
        won = True
    else:
        won = False
    return won

def guess_validator(guess, guessed_words, guess_validator_grid, connections, different_categories):
    
    correct_guess = False
    connecting_word = None
    
    i = 0  # Initialize an index to keep track of row indices
    
    for row in guess_validator_grid:
        if set(guess) == set(row) and set(guess) not in guessed_words:
            correct_guess = True
            guessed_words.append(guess)
            connecting_word = connections[i]["Connecting Word"] 
            different_categories.append(connecting_word)
            break  # No need to continue once a correct guess is found
        i += 1  # Move to the next row

    return correct_guess, connecting_word, guessed_words, guess_validator_grid, different_categories

def initialize_game():
    grid = [ #grid to store connections being used
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ]

    guessed_words = [] #array to store words that have been guessed
    
    different_categories = []

    guess_validator_grid = grid

    connections = [        #different categories
    {"Connecting Word": "Colours", "Words" : ["Red", "Green", "Yellow", "Blue"]}, 
    {"Connecting Word": "Days", "Words" : ["Monday", "Friday", "Tuesday", "Sunday"]}, 
    {"Connecting Word": "Movies", "Words" : ["Avatar", "Titanic", "Star Wars", "The Lion King"]}, 
    {"Connecting Word": "Beaches", "Words" : ["Manly", "Longreef", "Freshwater", "Bondi"]}, 
    {"Connecting Word": "Fruit", "Words" : ["Apple", "Orange", "Pear", "Banana"]}, 
    {"Connecting Word": "Shapes", "Words" : ["Circle", "Triangle", "Square", "Rectangle"]}, 
    {"Connecting Word": "Countries", "Words" : ["Australia", "America", "Germany", "Fiji"]}, 
    {"Connecting Word": "Sports", "Words" : ["Rugby", "Basketball", "Cricket", "Surfing"]},
    ]

    return grid, guessed_words, guess_validator_grid, connections, different_categories

def play_game():
    
    grid, guessed_words, guess_validator_grid, connections, different_categories = initialize_game() #sets all the variables to default
    grid = grid_generator(connections, grid)  # Generate the grid
    neat_grid = words_the_same_length(grid)  # Makes all the words the same length by adding spaces and centering the word
    shuffled_grid = grid_shuffle(neat_grid)  # Shuffles the grid
    
    lives = 4 
    categories_remaining = 4
    
    won = check_if_won(categories_remaining)
    
    while lives > 0 and won == False :  # Loop until the player runs out of lives or wins
        
        print_grid(shuffled_grid, guessed_words) #prints the grid based off categories guessed and remaing
        guess = get_player_guess(lives, categories_remaining, neat_grid, guessed_words) #gets the players guess and lets them shuffle the grid
        correct_guess, connecting_word, guessed_words, guess_validator_grid, different_categories = guess_validator(guess, guessed_words, guess_validator_grid, connections, different_categories)
        
        if correct_guess == True:
            typewriter_effect(f"\033[96mCorrect! The category is: {connecting_word}")
            categories_remaining -= 1
            won = check_if_won(categories_remaining)
            
            if won == True and lives == 1:
                print_grid(shuffled_grid, guessed_words)
                typewriter_effect("\033[96mPhew! You've guessed all connections.")
                typewriter_effect("Would you like to play again? (Yes/No)\033[0m")
                play_again_prompt = input()
                if play_again_prompt == "Yes":
                    
                    play_game()   
            elif won == True:
                print_grid(shuffled_grid, guessed_words)
                typewriter_effect("\033[96mCongratulations! You've guessed all connections.")
                typewriter_effect("Would you like to play again? (Yes/No)\033[0m")
                play_again_prompt = input()
                if play_again_prompt == "Yes":
                    
                    play_game()

        else:
            typewriter_effect("\033[96mIncorrect! You lost one life.")
            lives -= 1
            if lives == 0:
                typewriter_effect("\033[96mYou've run out of lives. Game over.")
                typewriter_effect("\033[96mThe categories were...")
                print(different_categories)
                typewriter_effect("\033[96mWould you like to play again? (Yes/No)\033[0m")
                play_again_prompt = input()
                if play_again_prompt == "Yes":
                    play_game()

def tutorial_grid():
    shuffled_grid = [["Red", "Square", "Rectangle", "Star Wars"],["Surfing", "Blue", "Avatar", "Circle"],["Triangle"],["Titanic",],]
    print_grid(shuffled_grid)

def tutorial():
    print()
    typewriter_effect("This is a game where you need to guess the four sets of associated words")
    typewriter_effect("Each round four categories are randomly chosen and printed in the grid")
    typewriter_effect("You can either guess the associated words by typing them, adding commas to sepperate them E.g (Red, Blue, Green, Yellow), or type 'shuffle' to shuffle the grid")
    typewriter_effect("You get 4 wrong guesses and need to guess the 4 categories to win")
    typewriter_effect("Here is an example:")
    tutorial_grid()

    start_promt = input()
    if start_promt == "Yes":
        play_game

def start_game():
    typewriter_effect("\033[96mWelcome to Synergies!")
    print()
    print()
    typewriter_effect_fast("""\033[34m  ██████▓██   ██▓ ███▄    █ ▓█████  ██▀███    ▄████  ██▓▓█████   ██████ 
▒██    ▒ ▒██  ██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒ ██▒ ▀█▒▓██▒▓█   ▀ ▒██    ▒ 
░ ▓██▄    ▒██ ██░▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██░▄▄▄░▒██▒▒███   ░ ▓██▄   
  ▒   ██▒ ░ ▐██▓░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░▓█  ██▓░██░▒▓█  ▄   ▒   ██▒
▒██████▒▒ ░ ██▒▓░▒██░   ▓██░░▒████▒░██▓ ▒██▒░▒▓███▀▒░██░░▒████▒▒██████▒▒
▒ ▒▓▒ ▒ ░  ██▒▒▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ░▒   ▒ ░▓  ░░ ▒░ ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░▓██ ░▒░ ░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ░   ░  ▒ ░ ░ ░  ░░ ░▒  ░ ░
░  ░  ░  ▒ ▒ ░░     ░   ░ ░    ░     ░░   ░ ░ ░   ░  ▒ ░   ░   ░  ░  ░  
      ░  ░ ░              ░    ░  ░   ░           ░  ░     ░  ░      ░  
         ░ ░                                                            \033[00m """)  
    print()
    print()
    typewriter_effect("\033[96mWould you like to play the tutorial? (Yes/No)...\033[0m")
    start_prompt = (input())
    if start_prompt == "No":
        play_game()
    elif start_prompt == "Yes" :
        tutorial()
    else: 
        start_game()

start_game()


#things to do


#tutorial
#colour the writing/grid
#add more categories
#validate each guess to make sure it is an english word
#converts each input to all lowercase




