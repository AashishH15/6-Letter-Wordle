import csv
import random

with open('words.txt') as file:
    reader = csv.reader(file)
    words = list(reader)
    
words = [item for sublist in words for item in sublist]

# Pick random word as answer
answer = random.choice(words).lower()  # Convert answer to lowercase for case-insensitive comparison

# Game variables
guesses = []
max_guesses = 6

# Print header
print("{:<10} {:<}".format("Guess #", "Guess"))
print("{:-<21}".format(""))

# Main game loop
for guess_num in range(max_guesses):

    # Get player's guess
    guess = input("{:<10} ".format(guess_num+1)).strip().lower()  # Convert guess to lowercase and remove leading/trailing spaces

    # Validate guess
    if len(guess) != 6:
        print("Invalid guess - must be 6 letters!")
        continue

    if not guess.isalpha():
        print("Invalid guess - letters only!")
        continue

    # Check if already guessed
    if guess in guesses:
        print("You already guessed that word!")
        continue

    # Add valid guess
    guesses.append(guess)

    # Print guess
    print(guess)

    # Check for winning guess
    if guess == answer:
        print("You got it! The word was", answer)
        break
        
    # Give feedback on incorrect guess
    else:
        print("Correct position of guess:")
        
        # Track correct letters and positions
        correct_letters = set()
        letter_positions = {}
        
        for i, letter in enumerate(guess):
            if letter == answer[i]:
                letter_positions[i] = letter
            elif letter in answer:
                correct_letters.add(letter)
                
        # Print position matches  
        for i in range(6):
            if i in letter_positions:
                print(f"{letter_positions[i]} is in position {i+1}")
                
        # Print correct letters
        if correct_letters:
            print("Incorrect Position of Letters:", ", ".join(correct_letters))  
            
        print()
        
# Game over message
if len(guesses) == max_guesses:
    print("You ran out of guesses. The word was", answer)
