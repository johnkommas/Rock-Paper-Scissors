# Write your code here
import random
import pandas as pd

# choices = ("scissors", "fire", "rock", "gun", "lightning", "devil",
#            "dragon", "water", "air", "paper", "sponge", "wolf",
#            "tree", "human", "snake")
accepted_input = ["!exit", "!rating"]


def get_win_loss(user_input, choices):
    first_list = choices[choices.index(user_input) + 1:]
    second_list = choices[:choices.index(user_input)]
    new_list = first_list + second_list
    win = new_list[:len(new_list) // 2]
    # print(win)
    return win


def get_input_from_user():
    user_input = input()
    if user_input in accepted_input or user_input in choices:
        return user_input
    else:
        print("Invalid input\n")
        return get_input_from_user()


def set_output_from_computer():
    return random.choice(choices)


def get_winner(user_choise, computer_choice):
    win= get_win_loss(user_choise, choices)
    if choices.index(user_choise) == choices.index(computer_choice):
        print(f"There is a draw ({computer_choice})")
        return 50
    elif computer_choice in win:
        print(f"Sorry, but the computer chose {computer_choice}")
        return 0
    else:
        print(f"Well done. The computer chose {computer_choice} and failed")
        return 100


def get_data_from_database(name):
    df = pd.read_csv("rating.txt", names=['names', 'score'], sep=" ")
    # print(df)
    if name in df.names.unique():
        return df['score'][df.names == name].values[0]
    return 0


name = input("Enter your name: ")
print(f"Hello, {name}")
choices = [i for i in input().split(',')]
if len(choices) == 1:
    choices = ['scissors', 'rock', 'paper']
# print(choices)
print("Okay, let's start")
score = get_data_from_database(name)
# print(score)
while True:
    user = get_input_from_user()
    if user == '!exit':
        print("Bye!")
        break
    elif user == '!rating':
        print(f"Your rating: {score}")
    else:
        computer = set_output_from_computer()
        score += get_winner(user, computer)
