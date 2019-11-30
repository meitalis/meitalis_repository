def isSafe(board,row,col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveutil(board,col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board,i,col):
            board[i][col] = 1
        if solveutil(board,col +1) == True:
            return True

        board[i][col] = 0

    return False


N = 4


def print_sol(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end = ' ')


def solve():
    board = [[0] * N for i in range(N) ]
    print(board)
    if solveutil(board,0) == False:
        return False

        print_sol(board)

    return True



solve()