from trivia import Trivia
from user import User

users  = {}

def play(trivia):
    trivia.play()

def statistics(trivia):
    trivia.show_statistics()

def exit_cli():
    print("exit_cli")
    exit()

if __name__== '__main__':

    trivia = Trivia()

    commands = {
        '1': play,
        '2': statistics
    }

    cmd = -1
    while cmd != 0:

        login_name = input("enter login name \n").split()

        if login_name in users:
            print(f"user {login_name} already exists ")
        else:
            users.add(User(login_name))

        trivia.user_id = id
        cmd = input("1. play a trivia game\n" 
                    "2. display game statistics\n"
                    )

        commands.get(cmd,exit_cli)(trivia)
