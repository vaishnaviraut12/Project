import random

# ASCII representations of Rock, Paper, and Scissors
Rock = """
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
"""

Paper = """
     _______
---'    ___)___
           ______)
          _______)
         _______)
---.)
"""

Scissors = """
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
"""

ascii_images = [Rock, Paper, Scissors]

# Function to get user input
def get_user_choice():
    while True:
        try:
            userinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
            if userinput >= 0 and userinput <= 2:
                return userinput
            else:
                print("Invalid input, please choose 0, 1, or 2.")
        except ValueError:
            print("Invalid input, please enter a number (0, 1, or 2).")

# Function to determine the winner of the round
def determine_winner(userinput, computer_choice):
    # Print choices
    print("\nYour choice:")
    print(ascii_images[userinput])
    print("\nComputer's choice:")
    print(ascii_images[computer_choice])

    # Determine the winner based on the game rules
    if userinput == computer_choice:
        return "It's a tie!"
    elif (userinput == 0 and computer_choice == 2) or (userinput == 1 and computer_choice == 0) or (userinput == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"

# Function to play one round of the game
def play_round():
    userinput = get_user_choice()
    computer_choice = random.randint(0, 2)
    result = determine_winner(userinput, computer_choice)
    print(result)
    return result

# Function to ask if the user wants to play again
def ask_to_play_again():
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            return True
        elif play_again == 'no':
            return False
        else:
            print("Invalid input, please type 'yes' or 'no'.")

# Function to play multiple rounds and keep score
def play_game():
    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds would you like to play? "))

    for _ in range(rounds):
        print("\n--- New Round ---")
        result = play_round()

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

    print("\nFinal Score:")
    print(f"You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("You are the overall winner!")
    elif user_score < computer_score:
        print("The computer is the overall winner!")
    else:
        print("It's a tie overall!")

# Main function to start the game
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")

    # Loop to allow for replay after losing
    while True:
        play_game()
        if not ask_to_play_again():
            print("Thanks for playing! Goodbye!")
            break

