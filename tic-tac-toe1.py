import random

def enter_move(board, player):
    print("Enter your move: ")
    move = input().strip()
    while ((move in player) or (move not in board)):
        print("Invalid Input")
        print("Enter your move: ")
        move = input().strip()
    else:
        player.add(int(move))
        board1 = board.replace(move, "O")
        print(player)
    return board1, player

def computer_move(board, computer):
    move = random.randrange(1,9)
    while (move in computer) or (str(move) not in board): 
        move = random.randrange(1,9)
    computer.add(move)
    board1 = board.replace(str(move), "X")
    return board1, computer
#Initial board, with the computer's move already made
board = "+-------+-------+-------+\n|       |       |       |\n|   1   |   2   |   3   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   4   |   X   |   6   |\n|       |       |       |\n+-------+-------+-------+\n|       |       |       |\n|   7   |   8   |   9   |\n|       |       |       |\n+-------+-------+-------+\n"

computer = {5}
player = set()
print("****************************It's time for tic tac toe!****************************")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("**********************************TIC TAC TOE*************************************\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print("The computer will play its move now. Computer plays the X and you play the O.\n")
print(board)
print("The computer has played the move, now it's your turn:)")

Winner = ""

while('1' in board or '2' in board or '3'in board or '4' in board or '6' in board or '7' in board or '8' in board or '9' in board):
    
    board, player = enter_move(board, player)
    board, computer = computer_move(board, computer)
    print(board)

    if ((len([i for i in computer if i in [1,5,9]]) == 3) or (len([i for i in computer if i in [2,5,8]]) == 3) or (len([i for i in computer if i in [3,5,7]]) == 3) or (len([i for i in computer if i in [4,5,6]]) == 3) or (len([i for i in computer if i in [7,8,9]]) == 3) or (len([i for i in computer if i in [3,6,9]]) == 3) or (len([i for i in computer if i in [1,4,7]]) == 3) or (len([i for i in computer if i in [1,2,3]]) == 3)):
        Winner = "Computer"
        break
    elif((len([i for i in player if i in [7,8,9]]) == 3) or (len([i for i in player if i in [3,6,9]]) == 3) or (len([i for i in player if i in [1,4,7]]) == 3) or (len([i for i in player if i in [1,2,3]]) == 3)):
        Winner ="Player"
        break
        
if Winner=="":
    print("it's a tie. :)")
else:
    print("The winner is:", Winner)