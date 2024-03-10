import sys
import time
import random

grid = [               #grid to be printed
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
]

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
    
def grid_generator(): #makes and prints the grid randomly
    random.shuffle(connections) #shuffles the list of connections
    row = 0 #sets row to 0
    col = 0 #sets col to 0
    for connection in connections: # for each of the connections, access the dictionary
        for word in connection["Words"]: # within the dictionary, get each word
            if row < len(grid) and col < len(grid[0]):  # Check if we're still within the grid boundaries of a 4 by 4
                grid[row][col] = word # put the connections words inside the grid 
                col += 1 # moves to the next col
                if col >= len(grid[0]):  # if col exceeds the grid size, reset col to 0 and move to the next row
                    col = 0
                    row += 1
                    if row >= len(grid):  # if row exceeds the grid size of 4, break the loop
                        break
    return grid

def grid_word_spaces(grid):
    max_length = 13  # Find the maximum length of words in the grid
    neat_grid = [[word.ljust(max_length) for word in row] for row in grid]  # Add spaces to make all words the same length
    return neat_grid

def grid_shuffle(neat_grid):
    all_words_flat = []
    for row in neat_grid:
        for word in row:
            all_words_flat.append(word)
        
    # Shuffle the 1D list of all words
    random.shuffle(all_words_flat)

    # Recreate the 2D array structure with shuffled words
    shuffled_grid = []
    row_length = len(grid[0])  # Assuming each row has the same number of elements
    for i in range(0, len(all_words_flat), row_length):
        row = []
        for j in range(row_length):
            row.append(all_words_flat[i+j])
        shuffled_grid.append(row)   
    return shuffled_grid

def print_grid(shuffled_grid):
    print("_________________________________________________________________")
    print(f"| {shuffled_grid[0][0]} | {shuffled_grid[0][1]} | {shuffled_grid[0][2]} | {shuffled_grid[0][3]} |")
    print(f"| {shuffled_grid[1][0]} | {shuffled_grid[1][1]} | {shuffled_grid[1][2]} | {shuffled_grid[1][3]} |")
    print(f"| {shuffled_grid[2][0]} | {shuffled_grid[2][1]} | {shuffled_grid[2][2]} | {shuffled_grid[2][3]} |")
    print(f"| {shuffled_grid[3][0]} | {shuffled_grid[3][1]} | {shuffled_grid[3][2]} | {shuffled_grid[3][3]} |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def player_guess(lives, categories_remaining, neat_grid): #gets the players guesses
    guessed = False
    while guessed == False:
        print(f"(lives remaining = {lives}) (categories remaining = {categories_remaining})")
        print("Guess connected categories or (Shuffle)")
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

def play_game():
    grid = grid_generator()  # Generate the grid
    neat_grid = grid_word_spaces(grid)
    shuffled_grid = grid_shuffle(neat_grid)  # Shuffle the grid
    lives = 4 #gets 4 lives
    categories_remaining = 4
    won = check_if_won(categories_remaining)
    while lives > 0 and won == False :  # Loop until the player runs out of lives or wins
        print_grid(shuffled_grid)
        guess= player_guess(lives, categories_remaining, neat_grid) 
        print(grid)
        if set(guess) in set(grid):
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

def start_game():
    typewriter_effect("Welcome to Connections!")            #
    typewriter_effect("To play, type in the four words that you think are connected.")
    typewriter_effect("Once all 4 groups of Words have been guessed, you win :)")
    typewriter_effect("You only get 4 wrong guesses or you lose.")
    typewriter_effect("Would you like to begin? (Yes/No)...")
    start_prompt = (input())
    if start_prompt == "Yes":
        play_game()
    else:
        start_game()

start_game()
    

#things to do
#fix error where player can guess connections not displayed in grid
#typewriter effect
#tutorial
#colour the writing/grid
#updat grid after corect guess
#add more categories




