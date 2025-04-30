import random as rand

final_options = {
    "rock": ["scissors", "ball", "glue"],
    "scissors": ["hand", "salt", "paper"],
    "hand": ["ball", "glue", "rock"],
    "ball": ["salt", "paper", "scissors"],
    "salt": ["glue", "rock", "hand"],
    "glue": ["paper", "scissors", "ball"],
    "paper": ["rock", "hand", "salt"]
}

player_options = rand.sample(list(final_options.keys()), 3)

remaining_options = [move for move in final_options if move not in player_options]
rand.shuffle(remaining_options)

def get_user_gamemode():
    print("Welcome to my Create PT project. This is a game of rock-paper-scissors, with a twist.")
    mode = input("Please choose a game mode: \n1. Classic (rock, paper, scissors; no unlocks) \n2. Expanded (rock, paper, scissors; unlocks new moves each time you win) \n3. Randomized (randomized set of 3 options; no unlocks) \n4. Challenge (randomized set of 3 options; unlocks new moves each time you win)")
    while mode not in ["1", "2", "3", "4"]:
        mode = input("Invalid input. Please enter 1, 2, 3, or 4: ")
    return mode

def get_user_difficulty():
    diff = input("Please choose a difficulty: \n1. Easy (computer chooses from your options) \n2. Medium (computer chooses from all options) \n3. Hard (computer chooses from all options excluding your options)")
    while diff not in ["1", "2", "3"]:
        diff = input("Invalid input. Please enter 1, 2, or 3: ")
    return diff

def get_user_instadeath_option():
    death = input("Play in instadeath mode? (You will be unable to play again if you lose!) (y/n): ")
    while death not in ["y", "n"]:
        death = input("Invalid input. Please enter y or n: ")
    return death

def get_user_scoreloss_option():
    loss = input("Play in scoreloss mode? (Each loss results in a score decrease.) (y/n): ")
    while loss not in ["y", "n"]:
        loss = input("Invalid input. Please enter y or n: ")
    return loss

def get_user_choice():
    choice = input(f"Choose one ({', '.join(player_options)}): ").lower()
    while choice not in player_options:
        choice = input("Invalid input. Try again: ").lower()
    return choice

def get_random_choice(diff, player_options):
    if diff == "1":
        return rand.choice(player_options)
    elif diff == "2":
        return rand.choice(list(final_options.keys()))
    else:
        return rand.choice(remaining_options)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif computer in final_options[user]:
        return "win"
    else:
        return "lose"

def play_game():
    lives = 5
    points = 0
    mode = get_user_gamemode()
    global player_options
    global remaining_options
    if mode == "1":
        player_options = ["rock", "paper", "scissors"]
        remaining_options = []
        print("You have chosen the classic mode.")
    elif mode == "2":
        player_options = ["rock", "paper", "scissors"]
        remaining_options = ["hand", "ball", "salt", "glue"]
        rand.shuffle(remaining_options)
        print("You have chosen the expanded mode.")
    elif mode == "3":
        player_options = rand.sample(list(final_options.keys()), 3)
        remaining_options = []
        print("You have chosen the randomized mode.")
    else:
        player_options = rand.sample(list(final_options.keys()), 3)
        remaining_options = [move for move in final_options if move not in player_options]
        rand.shuffle(remaining_options)
        print("You have chosen the challenge mode.")
    diff = get_user_difficulty()
    death = get_user_instadeath_option()
    loss = get_user_scoreloss_option()
    while True:
        user = get_user_choice()
        computer = get_random_choice(diff, player_options)
        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")
        result = determine_winner(user, computer)
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
            points += 1
            print(f"Your current points: {points}")
            print(f"Your current lives: {lives}")
            if remaining_options:
                new_move = remaining_options.pop()
                player_options.append(new_move)
                print(f"New move unlocked: {new_move}!")
            else:
                print("All moves unlocked!")
        else:
            print("You lose!")
            lives -= 1
            if loss == 'y':
                lives += 1
                score -= 1
            print(f"Your current points: {points}")
            print(f"Your current lives: {lives}")
            if (death == 'y') or (lives == 0) or (score == -1):
                print("Game over!")
                print(f"Final score: {points} point(s)")
                break
        again = input("\nPlay again? (y/n): ").lower()
        while again not in ["y", "n"]:
            again = input("Invalid input. Please enter y or n: ")
        if again != 'y':
            break

def main():
    while True:
        play_game()
        restart = input("\nRestart the game from the beginning? (y/n): ").lower()
        while restart not in ["y", "n"]:
            restart = input("Invalid input. Please enter y or n: ")
        if restart != 'y':
            print("Thanks for playing!")
            break

main()
