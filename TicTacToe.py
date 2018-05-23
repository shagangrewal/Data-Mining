import random

def drawBoard(board):
    # to draw a 3*3 matrix board to represent a tic tiac toe board
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def selectLetter():
    # selecting the letter the player will play with
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Select which letter you will play with: X or O')
        letter = input().upper()
        
    #returning the choices made
    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def firstMove():
    # randomly selecting the player to make the first move
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'user'

def anotherGame():
    # asking the user if he/she wants to  play another game
    print('Do you want to play again or not?? Yes or No')
    return input().lower().startswith('y')

def move(board, letter, place):
    board[place] = letter

def hasWon(bo, le):
    # checking all combinations if either of the two players has won the game or not
    # minimum moves required to check this condition is 5(total moves made by both the players)
    # first line checks for horizontal condition, second one takes the vertical combinations and last is for the two diagnol cases
    return ((bo[1]==le and bo[2]==le and bo[3]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[7]==le and bo[8]==le and bo[9]==le) or
            (bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le) or
            (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le))
    
def dupBoard(board):
    dupliBoard = []
    for i in board:
        dupliBoard.append(i)

    return dupliBoard

def checkFreeSpace(board,place):
    # checking for the space, if you can make a move or not
    return board[place]==' '

def getPlayerMove(board):
    # keeping the track of the move made by the user
    moveMade = ' '
    while moveMade not in '1 2 3 4 5 6 7 8 9'.split() or not checkFreeSpace(board,int(moveMade)):
        print('Whats ur next move?(1-9)')
        moveMade = input()
    return int(moveMade)
            
def getRandomMove(board, movesList):
    # selecting a random move from the board to make a move
    possiblemove = []
    for i in movesList:
        if checkFreeSpace(board, i):
            possiblemove.append(i)

    if len(possiblemove)!=0:
        return random.choice(possiblemove)
    else:
        return None

    
def computerMoves(board, cLetter):
    if cLetter == 'X':
        pLetter = 'O'
    else:
        cLetter = 'O'
        pLetter = 'X'

    #check if we can win in the next possible move, so the computer will try to make a move in order to win the game in the next move
    for i in range(1,10):
        # create the copy board in order to check next moves and keep the original board accordingly
        copy = dupBoard(board)
        if checkFreeSpace(copy, i):
            move(copy, cLetter, i)
            if hasWon(copy,cLetter):
                return i

    # if the user is winning on the next move we try to block the move of the user
    for i in range(1,10):
        copy = dupBoard(board)
        if checkFreeSpace(copy,i):
            move(copy, pLetter, i)
            if hasWon(copy, pLetter):
                return i
    
    # try to make a move to the edge cases
    m = getRandomMove(board,[1,3,7,9])
    if m!=None:
        return m

    # try to occupy the center of the board
    if checkFreeSpace(board, 5):
        return 5

    # if both the above cases are not met, try to occupy the remaining of the cases
    return getRandomMove(board , [2,4,6,8])

def checkFull(board):
    # we see if the board is full or not
    for i in range(1,10):
        if checkFreeSpace(board,i):
            return False
    return True

print("Welcome to The Tic Tac Toe Game!!!")

while True:
    # intialise the board
    theBoard = [' ']*10
    # assign player and computer the respective letters
    plyrLetter, compLetter = selectLetter()
    # select the player who will go first
    turn = firstMove()
    print("The "+turn+" will make the first Move")
    gamePlayed = True

    # the gamePlayed will be true as long as we dont have the winner or the board is not full
    while gamePlayed:
        if turn == 'user':
            drawBoard(theBoard)
            makeMove = getPlayerMove(theBoard)
            move(theBoard, plyrLetter, makeMove)

            if hasWon(theBoard, plyrLetter):
                drawBoard(theBoard)
                print("Congratulations!!! you have won the game!!!")
                gamePlayed = False
            else:
                if checkFull(theBoard):
                    print("Phew!!!The game is a time")
                    break
                else:
                    turn = 'computer'
        else:
            M = computerMoves(theBoard, compLetter)
            move(theBoard, compLetter, M)

            if hasWon(theBoard, compLetter):
                drawBoard(theBoard)
                print("Sorry! the computer has defeated you. Better luck next time")
                gamePlayed = False
            else:
                if checkFull(theBoard):
                    print("Phew!! the game is draw")
                    break
                else:
                    turn = 'user'
    if not anotherGame():
        break
    
