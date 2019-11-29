def is_good(n, board,x,y):
    print("board", board)
    print("is_good x",x,'y',y,'n',n)
    for i in range(y+1, n):
        if (board[x][i] != 0 or
           board[x + i][i] != 0 or
           board[x - i][i] != 0):
                return False

    board[x][y] = 1
    return True


def search(n, board,x,y):
    print('search x', x, 'y',y,'n',n)
    if x == n or y == n:
       return

    if is_good(n, board,x,y) is False:
        search(n-1,board,x+1,y+1)

    search(n, board, x + 1, y + 1)

def do_search(n,board):

    for i in range(n):
        print('** do search i',i)
        search(n, board, i, 0)

        for i in range(n):
            print(board[i])

        board = [[0] * n for i in range(n)]


def run_problem():
    n = 4
    board = [[0] * n for i in range(n)]
    #b = [0,0,0,0,0]
    # #borad_dict = dict(((i, j), 0) for i in range(n) for j in range(n))
    # search(n,board,0,0)

    do_search(n,board)

    for i in range(n):
         print(board[i])

run_problem()