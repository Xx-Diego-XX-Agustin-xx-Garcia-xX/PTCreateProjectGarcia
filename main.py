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
    mode = input("Please choose a game mode: \n1. Classic (rock, paper, scissors; no unlocks) \n2. Expanded (rock, paper, scissors; unlocks new moves each time you win) \n3. Randomized (randomized set of 3 options; no unlocks) \n4. Challenge (randomized set of 3 options; unlocks new moves each time you win) \n")
    while mode not in ["1", "2", "3", "4", "Classic", "Expanded", "Randomized", "Challenge"]:
        mode = input("Invalid input. Please enter 1, 2, 3, 4, or the names of the difficulties: ")
    return mode

def get_user_difficulty():
    diff = input("Please choose a difficulty: \n1. Normal (computer chooses from your options) \n2. Medium (computer chooses from all options) \n3. Hard (computer chooses from all options excluding your options) \n")
    while diff not in ["1", "2", "3", "Normal", "Medium", "Hard"]:
        diff = input("Invalid input. Please enter 1, 2, 3, or the names of the difficulties: ")
    return diff

def get_user_instadeath_option():
    death = input("Play in instadeath mode? (You will be unable to play again if you lose.) (y/n): ")
    while death not in ["y", "n"]:
        death = input("Invalid input. Please enter y or n: ")
    return death

def get_user_deathscore_option():
    score = input("Play in deathscore mode? (Each loss results in a score decrease; if your score reaches 0, you will be unable to play again if you have a negative score.) (y/n): ")
    while score not in ["y", "n"]:
        score = input("Invalid input. Please enter y or n: ")
    return score

def get_user_quickdraw_option():
    quick = input("Play in quickdraw mode? (Each tie is randomly chosen as a win or loss.) (y/n): ")
    while quick not in ["y", "n"]:
        quick = input("Invalid input. Please enter y or n: ")
    return quick

def get_user_choice():
    choice = input(f"Choose one ({', '.join(player_options)}): ").lower()
    while choice not in player_options:
        choice = input("Invalid input. Try again: ").lower()
    return choice

def get_random_choice(diff, player_options):
    if (diff == "1") or (diff == "Normal"):
        return rand.choice(player_options)
    elif (diff == "2") or (diff == "Medium"):
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
    if (mode == "1") or (mode == "Classic"):
        player_options = ["rock", "paper", "scissors"]
        remaining_options = []
        print("You have chosen the classic mode.")
    elif (mode == "2") or (mode == "Expanded"):
        player_options = ["rock", "paper", "scissors"]
        remaining_options = ["hand", "ball", "salt", "glue"]
        rand.shuffle(remaining_options)
        print("You have chosen the expanded mode.")
    elif (mode == "3") or (mode == "Randomized"):
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
    score = get_user_deathscore_option()
    quick = get_user_quickdraw_option()
    while True:
        user = get_user_choice()
        computer = get_random_choice(diff, player_options)
        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")
        result = determine_winner(user, computer)
        if result == "tie":
            if quick == 'y':
                result = rand.choice(["win", "lose"])
                print(f"Tie broken randomly as {result}")
            else:
                print("It's a tie!")
        if result == "win":
            print("You win!")
            points += 1
            print(f"Your current score: {points}")
            print(f"Your current lives: {lives}")
            if remaining_options and mode in ["2", "4"]:
                new_move = remaining_options.pop()
                player_options.append(new_move)
                print(f"New move unlocked: {new_move}!")
            else:
                print("All moves unlocked!")
        elif result == "lose":
            print("You lose!")
            lives -= 1
            if score == 'y':
                lives += 1
                points -= 1
            print(f"Your current score: {points}")
            print(f"Your current lives: {lives}")
            if (death == 'y') or (lives == 0) or (points < 0):
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