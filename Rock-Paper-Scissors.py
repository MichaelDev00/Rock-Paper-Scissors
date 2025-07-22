import random

word_scissors = "scissors"
word_rock = "rock"
word_paper = "paper"
choices = [word_scissors, word_paper, word_rock]
program_guess = random.choice(choices)
max_attempts = 2
# for attempt in range(max_attempts):


def user_choice():
    player_guess = input("Rock, Paper or Scissors:").lower()
    while True:
        if player_guess.lower() not in ['rock', 'paper', 'scissors']:
            print("Wrong choice, please choose between Rock, Paper or Scissors")
            break


def play_game(player_guess):
    while True:
        choices = [word_scissors, word_paper, word_rock]
        if player_guess == word_paper and program_guess == word_rock:
            print("Nice, you WIN!")
        elif player_guess == word_paper and program_guess == word_scissors:
            print("Ahh, you LOSE!")
        elif player_guess == word_paper and program_guess == word_paper:
            print("Not win but DRAW!")
        elif player_guess == word_rock and program_guess == word_scissors:
            print("Nice, you WIN!")
        elif player_guess == word_rock and program_guess == word_paper:
            print("Ahh, you LOSE!")
        elif player_guess == word_rock and program_guess == word_rock:
            print("Not win but DRAW!")
        elif player_guess == word_scissors and program_guess == word_rock:
            print("Ahh, you LOSE!")
        elif player_guess == word_scissors and program_guess == word_paper:
            print("Nice, you WIN!")
        elif player_guess == word_scissors and program_guess == word_scissors:
            print("Not win but DRAW!")
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break


user_choice()
play_game(player_guess)
