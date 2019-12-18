from trivia import Trivia

users  = {}

def play():
    Trivia()

def statistics():
    pass

def exit_cli():
    print("exit_cli")
    exit()

if __name__== '__main__':

    commands = {
        '1': play,
        '2': statistics
    }

    cmd = -1
    while cmd != 0:
        user_details = input("enter id & name\n").split()
        id = user_details[0]
        if id in users.keys():
            print("user already exists with name", users[id])
        else:
            users[user_details[0]] = ' '.join(user_details[1:])

        cmd = input("1. play a trivia game\n" 
                    "2. display game statistics\n"
                    )

        commands.get(cmd,exit_cli)()
