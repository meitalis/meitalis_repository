from trivia import Trivia


def play(trivia):
    trivia.play()


def statistics(trivia):
    trivia.show_statistics()


def set_user(trivia):
    trivia.set_user()


def exit_cli(trivia):
    print("EXIT GAME")
    exit()

if __name__== '__main__':

    trivia = Trivia()

    set_user(trivia)

    commands = {
        '1': play,
        '2': set_user,
        '3': statistics,
        '4': exit_cli
    }

    cmd = -1
    while cmd != 0:
        cmd = input("Choose:\n"
                    "1. play a trivia game\n"
                    "2. switch user\n"
                    "3. display game statistics\n"
                    "4. exit game\n"
                    )
        if cmd=='':
            continue

        commands.get(cmd, exit_cli)(trivia)



