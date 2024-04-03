import sys
import time
import random

def typewriter_effect(text): #typewriter function
    for char in text: #loop through each character in text and print one at a time with 0.05 delay
        sys.stdout.write(char) 
        sys.stdout.flush()   
        time.sleep(0.05)  
    print()

def typewriter_effect_fast(text): #fast typewriter effect
    for char in text: #loop through each character in text and print one at a time with 0.0005
        sys.stdout.write(char) 
        sys.stdout.flush()   
        time.sleep(0.0005) 
    print()
    
def grid_generator(connections, grid, different_categories): #makes the base grid
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
    
    i = 0 
    for i in range(4): #adds the connecting word of each of the categories used to different categories
        different_categories.append(connections[i]["Connecting Word"])

    return grid, different_categories  

def words_the_same_length(grid): #centres each word and adds spaces for grid
    max_length = 20 #max length for a word and the spaces is 20
    neat_grid = [[word.center(max_length) for word in row] for row in grid]  # Add spaces to make all words the same length of 20 and centres word for each word in each row in grid
    return neat_grid

def words_the_same_length_1(guessed_words): #centres each word and adds spaces for guessed words
    max_length = 20 
    guessed_words = [[word.center(max_length) for word in row] for row in guessed_words] 
    return guessed_words

def words_the_same_length_2(shuffled_grid): #centres each word and adds spaces for shuffled grid
    max_length = 20 
    shuffled_grid = [[word.center(max_length) for word in row] for row in shuffled_grid] 
    return shuffled_grid

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
    
    guessed_words = words_the_same_length_1(guessed_words) #makes the guessed words centred and spaces added
    remaining_words = [] #empty array

    for row in shuffled_grid:
        for word in row:
            if word.strip() not in [word.strip() for row in guessed_words for word in row]: #for each word in shuffled grid, if its not in guessed words, add it to remaining words
                remaining_words.append(word)  

    if len(guessed_words) == 0: #if 0 rows have been guessed
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
    
    elif len(guessed_words) == 1: #if one row has been guessed
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
    
    elif len(guessed_words) == 2: #if 2 rows have been guessed
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
    
    elif len(guessed_words) == 3: #if 3 rows have been guessed
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
    
    elif len(guessed_words) == 4: #if 4 rows have been guessed
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
        typewriter_effect_fast("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\033[0m")

def get_player_guess(lives, categories_remaining, neat_grid, guessed_words): #gets the players guesses
    has_player_guessed = False 
    
    while has_player_guessed == False: 
        typewriter_effect(f"\033[31mlives remaining = {lives}")
        typewriter_effect(f"\033[92mcategories remaining = {categories_remaining}\033[0m")
        typewriter_effect("\033[96mGuess connected categories or Shuffle:\033[0m")
        guess = input().upper().split(',')  # Split input into a list of words and uppercases it
        
        if "SHUFFLE" in guess: #if the guess contains shuffle, shuffle the grid
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

def valid_guess_checker(guess, grid): #is it a valid guess
    valid_guess = False
    valid_words = 0

    if len(guess) == 4:
        for word in guess:
            if word in grid[0] or grid[1] or grid[2] or grid[3]: #if word is in a row in grid it is a valid guess
                valid_words += 1
        if valid_words == 4:
            valid_guess = True

    return valid_guess

def is_guess_correct(guess, guessed_words, guess_validator_grid, connections,): #is guess correct
    
    correct_guess = False
    connecting_word = None
    
    i = 0 #sets it to the first row of the connections dictionary 
    
    for row in guess_validator_grid:
        if set(guess) == set(row) and set(guess) not in guessed_words: #if the guess matches a row in the grid and hasn't been guessed
            correct_guess = True
            guessed_words.append(guess)
            connecting_word = connections[i]["Connecting Word"] 
            
            break  # No need to continue once a correct guess is found
        i += 1  # Move to the next row of connections

    return correct_guess, connecting_word, guessed_words, guess_validator_grid

def initialize_game():
    grid = [ #grid to store connections being used
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ["word", "word", "word", "word"], 
    ]

    guessed_words = [] #array to store words that have been guessed
    
    different_categories = [] #array to store what the different categories are

    guess_validator_grid = grid 

    connections = [ #dictionary of the different connections chat gpt generated
    {"Connecting Word": "COLOURS", "Words": ["RED", "GREEN", "YELLOW", "BLUE"]},
    {"Connecting Word": "DAYS", "Words": ["MONDAY", "FRIDAY", "TUESDAY", "SUNDAY"]},
    {"Connecting Word": "MOVIES", "Words": ["AVATAR", "TITANIC", "STAR WARS", "THE LION KING"]},
    {"Connecting Word": "BEACHES", "Words": ["MANLY", "LONGREEF", "FRESHWATER", "BONDI"]},
    {"Connecting Word": "FRUIT", "Words": ["APPLE", "ORANGE", "PEAR", "BANANA"]},
    {"Connecting Word": "SHAPES", "Words": ["CIRCLE", "TRIANGLE", "SQUARE", "RECTANGLE"]},
    {"Connecting Word": "COUNTRIES", "Words": ["AUSTRALIA", "AMERICA", "GERMANY", "FIJI"]},
    {"Connecting Word": "SPORTS", "Words": ["RUGBY", "BASKETBALL", "CRICKET", "SURFING"]},
    {"Connecting Word": "COLORS", "Words": ["MAGENTA", "CYAN", "YELLOW", "BLACK"]},
    {"Connecting Word": "VEHICLES", "Words": ["CAR", "BIKE", "PLANE", "SHIP"]},
    {"Connecting Word": "WEATHER", "Words": ["SUNNY", "RAIN", "SNOW", "WINDY"]},
    {"Connecting Word": "INSTRUMENTS", "Words": ["GUITAR", "VIOLIN", "PIANO", "FLUTE"]},
    {"Connecting Word": "BOOKS", "Words": ["NOVEL", "BIOGRAPHY", "FANTASY", "MYSTERY"]},
    {"Connecting Word": "CLOTHING", "Words": ["SHIRT", "PANTS", "DRESS", "JACKET"]},
    {"Connecting Word": "FURNITURE", "Words": ["CHAIR", "TABLE", "SOFA", "BED"]},
    {"Connecting Word": "TECHNOLOGY", "Words": ["COMPUTER", "PHONE", "TABLET", "CAMERA"]},
    {"Connecting Word": "VEGETABLES", "Words": ["CARROT", "BROCCOLI", "POTATO", "TOMATO"]},
    {"Connecting Word": "ANIMALS", "Words": ["DOG", "CAT", "ELEPHANT", "LION"]},
    {"Connecting Word": "CITIES", "Words": ["NEW YORK", "LONDON", "PARIS", "TOKYO"]},
    {"Connecting Word": "PLANETS", "Words": ["MARS", "VENUS", "EARTH", "JUPITER"]},
    {"Connecting Word": "FLOWERS", "Words": ["ROSE", "DAISY", "TULIP", "SUNFLOWER"]},
    {"Connecting Word": "MUSIC", "Words": ["ROCK", "POP", "JAZZ", "CLASSICAL"]},
    {"Connecting Word": "FOOD", "Words": ["PIZZA", "SUSHI", "BURGER", "PASTA"]},
    {"Connecting Word": "DRINKS", "Words": ["COFFEE", "TEA", "WATER", "JUICE"]},
    {"Connecting Word": "ANATOMY", "Words": ["HEART", "LUNGS", "BRAIN", "STOMACH"]},
    {"Connecting Word": "HOBBIES", "Words": ["PAINTING", "READING", "GARDENING", "COOKING"]},
    {"Connecting Word": "MOUNTAINS", "Words": ["EVEREST", "K2", "MATTERHORN", "KILIMANJARO"]},
    {"Connecting Word": "ELEMENTS", "Words": ["HYDROGEN", "OXYGEN", "CARBON", "NITROGEN"]},
    {"Connecting Word": "MAMMALS", "Words": ["ELEPHANT", "TIGER", "WHALE", "GIRAFFE"]},
    {"Connecting Word": "UNIVERSITIES", "Words": ["HARVARD", "OXFORD", "STANFORD", "CAMBRIDGE"]},
    {"Connecting Word": "INSECTS", "Words": ["ANT", "BEE", "BUTTERFLY", "MOSQUITO"]},
    {"Connecting Word": "TOOLS", "Words": ["HAMMER", "SCREWDRIVER", "PLIERS", "WRENCH"]},
    {"Connecting Word": "MUSICAL INSTRUMENTS", "Words": ["VIOLIN", "GUITAR", "PIANO", "FLUTE"]},
    {"Connecting Word": "CONTINENTS", "Words": ["ASIA", "AFRICA", "EUROPE", "NORTH AMERICA"]},
    {"Connecting Word": "HOLIDAYS", "Words": ["CHRISTMAS", "HALLOWEEN", "THANKSGIVING", "EASTER"]},
    {"Connecting Word": "DRINKWARE", "Words": ["MUG", "GLASS", "CUP", "FLASK"]},
    {"Connecting Word": "DINOSAURS", "Words": ["TYRANNOSAURUS", "TRICERATOPS", "STEGOSAURUS", "BRACHIOSAURUS"]},
    {"Connecting Word": "KITCHEN APPLIANCES", "Words": ["BLENDER", "TOASTER", "MICROWAVE", "COFFEE MAKER"]},
    ]

    return grid, guessed_words, guess_validator_grid, connections, different_categories

def play_game():
    
    grid, guessed_words, guess_validator_grid, connections, different_categories = initialize_game() #sets all the variables to default
    grid, different_categories = grid_generator(connections, grid, different_categories)  # Generate the grid
    neat_grid = words_the_same_length(grid)  # Makes all the words the same length by adding spaces and centering the word
    shuffled_grid = grid_shuffle(neat_grid)  # Shuffles the grid
    
    lives = 4 
    categories_remaining = 4
       
    won = check_if_won(categories_remaining)

    while lives > 0 and won == False :  # Loop until the player runs out of lives or wins
        
        print_grid(shuffled_grid, guessed_words) #prints the grid based off categories guessed and remaing
        guess = get_player_guess(lives, categories_remaining, neat_grid, guessed_words) #gets the players guess and lets them shuffle the grid
        valid_guess = valid_guess_checker(guess, grid)
        if valid_guess == True:
            correct_guess, connecting_word, guessed_words, guess_validator_grid, = is_guess_correct(guess, guessed_words, guess_validator_grid, connections)
        
            if correct_guess == True:
                typewriter_effect(f"\033[96mCorrect! The category is: {connecting_word}")
                categories_remaining -= 1
                won = check_if_won(categories_remaining)
            
                if won == True and lives == 1:
                    print_grid(shuffled_grid, guessed_words)
                    typewriter_effect("\033[96mPhew! You've guessed all connections.")
                    typewriter_effect("Would you like to play again? (Yes/No)\033[0m")
                    play_again_prompt = input().upper()
                    if play_again_prompt == "YES":
                        play_game()   
                    else:
                        typewriter_effect("\033[96mGoodbye!")
                elif won == True:
                    print_grid(shuffled_grid, guessed_words)
                    typewriter_effect("\033[96mCongratulations! You've guessed all connections.")
                    typewriter_effect("Would you like to play again? (Yes/No)\033[0m")
                    play_again_prompt = input().upper()
                    if play_again_prompt == "YES":
                        play_game()
                    else:
                        typewriter_effect("\033[96mGoodbye!")  

            else:
                typewriter_effect("\033[31mIncorrect! You lost one life.\033[0m")
                lives -= 1
                if lives == 0:
                    typewriter_effect("\033[96mYou've run out of lives. Game over.")
                    typewriter_effect("\033[96mThe categories were...")
                    i = 0 
                    for i in range(4):
                        print(different_categories[i])
                    typewriter_effect("\033[96mWould you like to play again? (Yes/No)\033[0m")
                    play_again_prompt = input().upper()
                    if play_again_prompt == "YES":
                        play_game()
                    else:
                        typewriter_effect("Goodbye!")  
        else: 
            typewriter_effect("\033[31mGuess is not valid try again\033[0m")

def tutorial_grid():
    guessed_words = []
    shuffled_grid = [["Red", "Square", "Rectangle", "Star Wars"],
                     ["Surfing", "Blue", "Avatar", "Circle"],
                     ["Triangle", "Green", "The Lion King", "Basketball"],
                     ["Titanic", "Rugby", "Cricket", "Yellow"],]
    shuffled_grid = words_the_same_length_2(shuffled_grid)
    print_grid(shuffled_grid, guessed_words)

def tutorial():
    print()
    typewriter_effect("\033[96mThis is a game where you need to guess the four sets of associated words.")
    typewriter_effect("Each round four categories are randomly chosen and printed in the grid.")
    print()
    typewriter_effect("You can guess the associated words by typing them.")
    typewriter_effect("Add commas to sepperate the individual words.")
    print()
    typewriter_effect("You get 4 lives before you lose.")
    typewriter_effect("Here is an example:\033[0m")
    print()
    tutorial_grid()
    print()
    typewriter_effect("\033[96mAn example guess would be:\033[0m")
    typewriter_effect("red, blue, yellow, green")
    typewriter_effect("\033[96mWould you like to begin?\033[0m")

    start_promt = input().upper()
    
    if start_promt == "YES":
        play_game()
    else:
        start_game()

def start_game():
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
    start_prompt = input().upper()
    
    
    if start_prompt == "YES":
        tutorial()
    else: 
        play_game()

start_game()





