import random
# 常量参数
# 空棋盘(1-9)
NEWBOARD = ['-1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# x字棋和o字棋子
FIRST = "x"
SECOND = "o"

# 打印棋盘
def drawBoard(board):
    print('┌──┬──┬──┐')
    print('│' + board[1] + ' │' + board[2] + ' │' + board[3] + ' │')
    print('├──┼──┼──┤')
    print('│' + board[4] + ' │' + board[5] + ' │' + board[6] + ' │')
    print('├──┼──┼──┤')
    print('│' + board[7] + ' │' + board[8] + ' │' + board[9] + ' │')
    print('└──┴──┴──┘')


# 选择棋子
def choicepiece():
    global playerpiece
    global aipiece
    print('x棋子先手，o棋子后手')
    playerpiece = input('请选择你的棋子:')
    if playerpiece == FIRST:
        aipiece = SECOND
    elif playerpiece == SECOND:
        aipiece = FIRST
    else:
        print("选择的棋子有误，请重新选择")
        choicepiece()
    return


# 可下棋位置 able[i]=1 表示可以落子
def abletoplace(board):
    able = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 10):
        if board[i] == ' ':
            able[i] = 1
    return able


# 玩家落子 playermove(棋盘,落子位置)
def playermove(board, place):
    global palyerpiece
    able = abletoplace(board)
    if able[place] != 1:  # 当前位置不可下棋
        print('当前位置不可下棋')
        place = int(input('请选择你要下的位置(1-9)'))
        playermove(board, place)

    else:
        board[place] = playerpiece
    return


# ai落子
def aimove(board):
    global playerpiece
    global aipiece
    able = abletoplace(board)
    # 情况1：ai落子到m即可获胜
    for m in range(1, 10):
        boardcopy = board.copy()
        if able[m] == 1:
            boardcopy[m] = aipiece
            if winner(boardcopy, aipiece):
                board[m] = aipiece
                return
    # 情况2：玩家落子到m玩家胜
    for m in range(1, 10):
        boardcopy = board.copy()
        if able[m] == 1:
            boardcopy[m] = playerpiece
            if winner(boardcopy, playerpiece):
                board[m] = aipiece
                return
    # 情况3：落到m无人胜利
    t=0
    while (t < 1000):
        t += 1
        m = random.randint(1,9)
        if able[m] == 1:
            board[m] = aipiece
            return
    # for m in (5, 1, 3, 7, 9, 2, 4, 6, 8):
    #     if able[m] == 1:
    #         board[m] = aipiece
    #         return


# 判断所给棋子是否获胜
def winner(board, piece):
    # _to_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    _to_win = {(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)}
    for r in _to_win:
        if board[r[0]] == board[r[1]] == board[r[2]] == piece:
            return True
    return False


# 判断是否平局
def tie(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


# 主程序
while True:
    board = NEWBOARD.copy()
    playerpiece = ''
    aipiece = ''
    choicepiece()
    print('你的棋子是{}，ai的棋子是{}，开始下棋'.format(playerpiece, aipiece))
    if playerpiece == SECOND:
        aimove(board)
        drawBoard(board)
    else:
        drawBoard(board)
    while winner(board, playerpiece)==False and winner(board, aipiece)==False and tie(board)==False:

        place=int(input('请选择你要下的位置(1-9)'))
        playermove(board, place)

        aimove(board)
        print('AI完成下棋')
        drawBoard(board)

    if winner(board, playerpiece):
        print('*****玩家胜利*****\n')
    elif winner(board, aipiece):
        print('*****AI胜利*****\n')
    else:
        print('*****平局*****\n')