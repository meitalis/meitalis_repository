from trivia import Trivia

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

        user_details = input("enter id & name\n").split()
        id = int(user_details[0])
        if id in users.keys():
            print("user already exists with name", users[id])
        else:
            users[id] = ' '.join(user_details[1:])


        trivia.user_id = id
        cmd = input("1. play a trivia game\n" 
                    "2. display game statistics\n"
                    )

        commands.get(cmd,exit_cli)(trivia)
