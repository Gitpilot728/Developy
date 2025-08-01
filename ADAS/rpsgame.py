# Summarize and concise code 
import sys
import random

def play_game():
    print("\nRock-Paper-Scissors Game")
    print("------------------------")
    Choices = input("Enter ... \n 1. Rock \n 2. Paper \n 3. Scissors..\n\n")
    try:
        player = int(Choices)
        if player < 1 or player > 3:  # Fixed the condition (changed | to or)
            print("You must enter 1, 2, or 3.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    Compch = random.choice("123")
    systm = int(Compch)
    # Mapping numbers to choices for better display
    choices_map = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print("\nYou chose", choices_map[player] + ".")
    print("System chose", choices_map[systm] + ".\n")
    if player == systm:
        print("Wow! It's a Tie!")
    elif (player == 1 and systm == 3) or \
         (player == 2 and systm == 1) or \
         (player == 3 and systm == 2):
        print("You Win!")
    else:
        print("System Wins!")
def main():
    while True:
        play_game()
        # Ask if player wants to continue
        while True:
            play_again = input("\nWould you like to play again? (y/n): ").lower()
            if play_again in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'.")

        if play_again == 'n':
            print("\nThanks for playing! Goodbye!")
            break
if __name__ == "__main__":
    main()
