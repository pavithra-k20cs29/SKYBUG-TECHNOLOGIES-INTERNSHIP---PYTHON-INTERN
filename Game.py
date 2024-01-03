import random
from unittest import result

def play_game():
    # Prompt user for their choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Generate computer's choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "paper":
            result = "You lose!"
        else:
            result = "You win!"
    elif user_choice == "paper":
        if computer_choice == "scissors":
            result = "You lose!"
        else:
            result = "You win!"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            result = "You lose!"
        else:
            result = "You win!"
    else:
        result = "Invalid choice. Please choose rock, paper, or scissors."
        
    # Display the user's choice, computer's choice, and the result
    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)
    print(result)

def play_again():
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again == "yes":
        return True
    else:
        return False

def update_score(user_score, computer_score, result):
    # Update the scores based on the result
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
        
    return user_score, computer_score

# Initialize scores
user_score = 0
computer_score = 0

while True:
    play_game()
    user_score, computer_score = update_score(user_score, computer_score,result)
    
    # Display current scores
    print("User Score:", user_score)
    print("Computer Score:", computer_score)
    
    if not play_again():
        break