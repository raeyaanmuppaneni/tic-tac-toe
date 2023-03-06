def show_board():
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")

def checkForWin(player):
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    else:
        return False

def checkDraw():
    for i in board.keys():
        if board[i] == ' ':
            return False

    return True


def player1():
    while True:

        position = input("Which position for player x?")
        if position.isnumeric():
            position = int(position)
            if position > 9 or position < 1 :
                print("The position hs to be an integer from 1 to 9.")
                continue
            else:
                break
            
        else:
            print("The position has to be an integer from 1 to 9.")
            continue

       

    if board[position] == ' ':
        board[position] = "x"
    else:
        print("This position has already been taken.\n")
        player1()
    show_board()
    if checkForWin("x"):
        print("x is the winner.")
        return True

def player2():

    while True:

        position = input("Which position for player x?")
        if position.isnumeric():
            position = int(position)
            if position > 9 or position < 1 :
                print("The position has to be an integer from 1 to 9.")
                continue
            else:
                break
                
        else:
            print("The position has to be an integer from 1 to 9.")
            continue

        if board[position] == ' ':
            board[position] = "o"
        else:
            print("This position has already been taken.\n")
            player2()
        show_board()
        if checkForWin("o"):
            print("o is the winner.")
            return True


board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}

show_board()


while True:
    if player1():break
    checkDraw()
    if player2():break
    checkDraw()
        
   
    



   

