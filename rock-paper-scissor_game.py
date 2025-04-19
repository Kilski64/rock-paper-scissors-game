import random

def get_random_string(computer_moves):
    if not computer_moves:
        return None
    return random.choice(computer_moves)

computer_moves = ['rock', 'paper', 'scissors']
computer_selection = get_random_string(computer_moves)


def play_game():
    round = 0
    user = 0
    computer = 0
    while True:
        print("Rock, Paper, Scissors Game")
        menu_input = int(input("Insert '1' to start game, '2' to quit application: "))

        if menu_input == 1:
            while True:
                
                print(f"Round: {round}")
                print(f"User score: {user}")
                print(f"Computer score: {computer}")
            
                player_move = input("Select your move (rock, paper, scissors): ").lower()

                if player_move == computer_selection:
                    print("It's a tie!")
                    round += 1

                elif player_move == "rock" and computer_selection == "scissors":
                    print("You win! Rock crushes scissors.")
                    user += 1
                    round += 1

                elif player_move == "rock" and computer_selection == "paper":
                    print("Computer wins! Paper covers rock.")
                    computer += 1
                    round += 1

                elif player_move == "paper" and computer_selection == "rock":
                    print("You win! Paper covers rock.")
                    user += 1
                    round += 1

                elif player_move == "paper" and computer_selection == "scissors":
                    print("Computer wins! Scissors cuts paper.")
                    computer += 1
                    round += 1

                elif player_move == "scissors" and computer_selection == "paper":
                    print("You win! Scissors cuts paper.")
                    user += 1
                    round += 1

                elif player_move == "scissors" and computer_selection == "rock":
                    print("Computer wins! Rock crushes scissors.")
                    computer += 1
                    round += 1

                elif player_move not in computer_moves:
                    print("Must select either 'rock', 'paper', or 'scissors'.")

                else:
                    print("Invalid command.")

        elif menu_input == 2:
            quit_app = input("Are you sure you want to quit application (Y/N)?: ")
            if quit_app == 'Y' or quit_app == 'y':
                print("Goodbye. Have a good day.")
                exit()
            elif quit_app == 'N' or quit_app == 'n':
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    play_game()



