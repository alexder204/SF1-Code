from random import randint


# Get the player's name and ensure it is a valid input
def user_name():
    while True:
        name = input("What is your name? ")
        if name.strip():
            return name.title()  # Capitalizes first letter of each word
        else:
            print("Please enter a valid name.")


# Get a valid guess from the user
def user_input():
    while True:
        try:
            guess = int(input("Guess a number: "))
            if 1 <= guess <= 100:  # Ensure guess is within valid range
                return guess
            else:
                print("Please enter a number within the valid range.")
        except ValueError:
            print("That's not a valid integer. Please try again.")


# Scoring system based on remaining turns
def user_score(turns):
    return turns * 10


# Provide hints to the player
def hint(ans, turns, a, b, c, d):
    if turns == 7:  # First hint
        print(f"Hint: The answer is between {ans - c} and {ans + d}")
    elif turns == 3:  # Second hint
        print(f"Hint: The answer is between {ans - a} and {ans + b}")


# Function to display the result of the game
def game_result(is_winner, name, score, ans):
    if is_winner:
        print(f"Congratulations {name}, you won the game! Your score is {score}.")
    else:
        print(f"Sorry {name}, you lost the game. Better luck next time.")
        print(f"The correct answer was {ans}. Your score is {score}.")


# Function to choose difficulty level
def choose_difficulty():
    while True:
        print("\nChoose a difficulty level:")
        print("1. Easy (1 to 30, 10 turns)")
        print("2. Medium (1 to 50, 8 turns)")
        print("3. Hard (1 to 100, 6 turns)")
        
        choice = input("Enter 1, 2, or 3: ")
        
        if choice == "1":
            return 30, 10  # Easy difficulty
        elif choice == "2":
            return 50, 8  # Medium difficulty
        elif choice == "3":
            return 100, 6  # Hard difficulty
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# Main function to run the game
def play_game():
    name = user_name()
    
    # Choose difficulty level
    print("\n")
    max_number, turns = choose_difficulty()  # Get number range and turns based on difficulty
    
    # Variables used for the hint system
    c = randint(1, 10)
    d = 10 - c
    a = randint(1, 5)
    b = 5 - a
    ans = randint(1, max_number)  # Set answer within the difficulty range
    
    print(f"\nWelcome, {name}! Let's play the number guessing game.")
    print(f"I have selected a number between 1 and {max_number}. Can you guess it?")
    
    while turns > 0:
        guess = user_input()  # Get the user's guess

        # Check if the guess is correct
        if guess == ans:
            print("You guessed the correct number!")
            score = user_score(turns)  # Calculate the score based on remaining turns
            game_result(True, name, score, ans)  # Display result
            break

        # If the guess is incorrect, provide feedback and hints
        if guess != ans:
            turns -= 1  # Reduce a turn on each wrong guess
            
            if abs(guess - ans) > 5:
                print("You're far from the correct answer.")
            else:
                print("You're getting closer to the correct answer.")
            
            print(f"You have {turns} turns left.")

            # Give hints when needed
            hint(ans, turns, a, b, c, d)

    if turns == 0:
        score = user_score(turns)
        game_result(False, name, score, ans)  # If out of turns, display the result

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()  # Restart the game
    else:
        print("Thank you for playing! Goodbye.")


# Start the game
if __name__ == "__main__":
    play_game()

