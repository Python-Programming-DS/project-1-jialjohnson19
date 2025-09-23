# implement 2D list of tic tac toe with 2 humans on same keyboard 

#screen shows state of board after every players move 

#store board as single 2-D list of strings that has 3 rows and 3 columns 
def resetBoard(board): 
    #initalizes and resets game board 
    printBoard(board)
    return [[" "]*3 for _ in range(3)]  # brand new 3x3 empty board

def printBoard(board): 
    #displays and updates game board 
    print(" " + "-" *18)
    print("|R\\C| 0 | 1 | 2 |") 
    print(" " + "-"*18)

    for r in range(3):
        row = f"| {r} | {board[r][0]} | {board[r][1]} | {board[r][2]} |"
        print(row)
        print(" " + "-"*18)

def validateEntry(row,col,board): 
    #returns true if user entered inputs are valid, otherwise returns False

    #prints the row and col number regardless of valid entry 
    print(f"You have entered row #{row}\n\t  and column #{col}")

    if row not in (0, 1, 2) and col not in (0, 1, 2):
        print("Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.")
        return False
    if board[row][col] != " ":
        print("That cell is already taken. \nPlease make another selection.")
        return False
    else: 
        print("Thank you for your selection.") 
        return True 

def checkFull(board): 
    # returns True if the board is full, otherwise False
    for row in board: 
        for col in row:   
            if col == " ":  # found an empty space
                return False
    
    print("DRAW! NOBODY WINS!")
    return True

def checkEnd(board, turn): 
    #returns True if game is over, otherwise False
    if checkFull(board) or checkWin(board,turn): 
        return True
    else: 
        return False

def checkWin(board,turn): 
    #returns True when 'X' or 'O' becomes winner, otherwise False 

    #rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == turn:
            print(f"{turn} IS THE WINNER!!!")
            return True

    #cols
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == turn:
            print(f"{turn} IS THE WINNER!!!")
            return True

    #diag
    if (board[0][0] == board[1][1] == board[2][2] == turn) or \
       (board[0][2] == board[1][1] == board[2][0] == turn):
        print(f"{turn} IS THE WINNER!!!")
        return True

    return False

def main():
    while True:
        turn = "X"
        print(f"New Game: {turn} goes first.\n")
        
        #define board 3x3 2d list of strings 
        board = [[" " for _ in range(3)]for _ in range(3)]

        #game begins with a clean board 
        board = resetBoard(board)

        while True:     
            print(f"\n{turn}'s turn.")
            print(f"Where do you want your {turn} placed? ")
            entry = input("Please enter row number and column number separated by a comma.\n").split(",")
            row = int(entry[0])
            col = int(entry[1])

            isValid = validateEntry(row, col, board)
            #run validEntry again if validate Entry is false 
            if not isValid: 
                continue
        
        
            board[row][col] = turn

            isEnd = checkEnd(board,turn)
            printBoard(board)
            

            if isEnd: 
                again = input("\nAnother game? Enter Y or y for yes.\n")
                if again.lower() == "y":
                    break 
                else: 
                    print("Thank you for playing!")
                    return 
                
            #switch players 
            if turn == "X":
                turn ="O"
            else: 
                turn = "X"

        


#calls main function 
if __name__ == "__main__": 
    main() 
