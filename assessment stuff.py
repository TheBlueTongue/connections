import sys
import time
import random


grid = [               #grid to be printed
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
]

guessed_words = []

guess_grid = grid

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

def typewriter_effect(text): #typewriter function
    for char in text: #loop through each character in text
        sys.stdout.write(char) 
        sys.stdout.flush()   
        time.sleep(0.05)  # Adjust the speed of the typewriter effect
    print()
    
def grid_generator(): #makes the base grid
    random.shuffle(connections) #shuffles the list of connections
    row = 0 #sets row to 0
    col = 0 #sets col to 0
    for connection in connections: # for each of the connections, access the dictionary
        for word in connection["Words"]: # within the dictionary, get each word
            if row < len(grid) and col < len(grid[0]):  # Check if we're still within the grid boundaries of a 4 by 4
                grid[row][col] = word # put the connections word inside the grid 
                col += 1 # moves to the next col
                if col >= len(grid[0]):  # if col exceeds the grid size, reset col to 0 and move to the next row
                    col = 0
                    row += 1
                    if row >= len(grid):  # if row exceeds the grid size of 4, break the loop
                        break
    return grid

def grid_word_spaces(grid): #centres each word and adds spaces
    max_length = 20 #max length for a word and the spaces is 20
    neat_grid = [[word.center(max_length) for word in row] for row in grid]  # Add spaces to make all words the same length of 20 and centres word
    return neat_grid

def grid_shuffle(neat_grid): #shuffles the neat grid
    all_words_flat = [] 
    for row in neat_grid:
        for word in row:
            all_words_flat.append(word) #adds each word from neat grid into a flat array
        
    random.shuffle(all_words_flat) # Shuffle the 1D list of all words

    shuffled_grid = []
    row_length = len(grid[0])  # each row has the same number of words as base grid
    for i in range(0, len(all_words_flat), row_length): 
        row = []
        for j in range(row_length):
            row.append(all_words_flat[i+j]) #creates the words into rows
        shuffled_grid.append(row) #adds each row to shuffled grid
    return shuffled_grid

def print_grid(shuffled_grid): #prints the gameboard grid
    print("________________________________________________________________________________________________")
    print("|                      ||                      ||                      ||                      |")
    print(f"| {shuffled_grid[0][0]} || {shuffled_grid[0][1]} || {shuffled_grid[0][2]} || {shuffled_grid[0][3]} |")
    print("|                      ||                      ||                      ||                      |")
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    print("|                      ||                      ||                      ||                      |")
    print(f"| {shuffled_grid[1][0]} || {shuffled_grid[1][1]} || {shuffled_grid[1][2]} || {shuffled_grid[1][3]} |")
    print("|                      ||                      ||                      ||                      |")
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    print("|                      ||                      ||                      ||                      |")
    print(f"| {shuffled_grid[2][0]} || {shuffled_grid[2][1]} || {shuffled_grid[2][2]} || {shuffled_grid[2][3]} |")
    print("|                      ||                      ||                      ||                      |")
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    print("|                      ||                      ||                      ||                      |")
    print(f"| {shuffled_grid[3][0]} || {shuffled_grid[3][1]} || {shuffled_grid[3][2]} || {shuffled_grid[3][3]} |")
    print("|                      ||                      ||                      ||                      |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def player_guess(lives, categories_remaining, neat_grid): #gets the players guesses
    guessed = False
    while guessed == False:
        print(f"          (lives remaining = {lives})                           (categories remaining = {categories_remaining})          ")
        print("Guess connected categories or Shuffle:")
        guess = input().split(',')  # Split input into a list of guesses
        
        if "Shuffle" in guess:
            shuffled_grid = grid_shuffle(neat_grid)
            print_grid(shuffled_grid)
        else:
            
            guess = [word.strip() for word in guess]  
            guessed = True 
            return guess

def check_if_won(categories_remaining):
    if categories_remaining == 0:
        won = True
    else:
        won = False
    return won

def guess_validator(guess):
    global guessed_words
    correct_guess = False
    global guess_grid
    
    index = 0  # Initialize an index to keep track of row indices
    
    # Iterate over the rows of guess_grid
    for row in guess_grid:
        if set(guess) == set(row) and set(guess) not in guessed_words:
            correct_guess = True
            guessed_words.append(guess)
            guess_grid.pop(index)
            break  # No need to continue once a correct guess is found
        index += 1  # Move to the next row index


    return correct_guess 

def play_game():
    grid = grid_generator()  # Generate the grid
    neat_grid = grid_word_spaces(grid)
    shuffled_grid = grid_shuffle(neat_grid)  # Shuffle the grid
    lives = 4 #gets 4 lives
    categories_remaining = 4
    won = check_if_won(categories_remaining)
    while lives > 0 and won == False :  # Loop until the player runs out of lives or wins
        print_grid(shuffled_grid)
        guess = player_guess(lives, categories_remaining, neat_grid) 
        
        correct_guess = guess_validator(guess)
        if correct_guess == True:
            print("Correct!")
            categories_remaining -= 1
            connections.pop(0)  # Remove the guessed connection
            won = check_if_won(categories_remaining)
            if won == True:
                print("Congratulations! You've guessed all connections.")
                print("Would you like to play again? (Yes/No)")
                play_again_prompt = input()
                if play_again_prompt == "Yes":
                    play_game()   
        else:
            print("Incorrect! You lost one life.")
            lives -= 1
            if lives == 0:
                print("You've run out of lives. Game over.")
                print("Would you like to play again? (Yes/No)")
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

    

    
def start_game():
    typewriter_effect("Welcome to Connections!")            
    typewriter_effect("Would you like to play the tutorial? (Yes/No)...")
    start_prompt = (input())
    if start_prompt == "Yes":
        play_game()
    else:
        tutorial()

start_game()
    

#things to do
#fix validate guess function
#typewriter effect to grid and other text
#tutorial
#colour the writing/grid
#updat grid after corect guess
#add more categories




