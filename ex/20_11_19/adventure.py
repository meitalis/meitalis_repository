def create_rooms(nums, size, rooms, doors):
    print("create_rooms n=", nums,"size=",size)
    for n in range(nums):
        #print(n)
        rooms[n] = [[(i,j) for i in range(10)] for j in range(10)]
        if n != 0 and n != nums:
            doors.append((n-1, n, 9, 0))
        #print("rooms", rooms[n])
        #print("doors", doors)


def go_forward(position):
    #print("go_forward before", position)
    (r, x, y) = tuple(position)
    #print(rooms[r])
    print(rooms[r][1][5])
    print((5,1) in rooms[r][1])
    if list[rooms[r].value()]is not None:
        print("you are in room #", r, "cell x:y", x, y+1)
        return r, x, y+1

    print("you are in the room #", r, "on its last cell x:y", x, y, "there is no room in this direction")
    return r, x, y


def go_backwards(position):
    print("go_backwards", position)


def go_left(position):
    print("go_left before", position)


def go_right(position):
    print("go_right before", position)


def jump_up(position):
    print("jump_up before", position)


def jump_down(position):
    print("jump_down before", position)


def uturn(position):
        print("uturn before", position)


def bend(position):
    print("bend before", position)


def open_door(position):
    print("open_door before", position)


def is_there_a_door(position):
    print("is_there_a_door before", position)


def is_there_a_key(position):
    print("is_there_a_key before", position)


def commands(command, r_position):
    cmds = {
        'gf':go_forward,
        'gb':go_backwards,
        'gl':go_left,
        'gr':go_right,
        'ju':jump_up,
        'jd':jump_down,
        'u':uturn,
        'b':bend,
        'od':open_door
        }
    return cmds.get(command)(r_position)


def questions(question):
    qtns = {
        'is there a door':is_there_a_door,
        'is there a key':is_there_a_key
        }
    qtns.get(question)()


if __name__ == "__main__":
    rooms = {}
    doors = []
    position = [1,0,0] #list = mutable [room,x,y)
    create_rooms(2, 2, rooms, doors)

    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)
    position = commands('gf', position)


