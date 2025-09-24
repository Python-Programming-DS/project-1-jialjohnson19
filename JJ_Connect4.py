# implement 2D list of tic tac toe with 2 humans on same keyboard 

#screen shows state of board after every players move 

#store board as single 2-D list of strings that has 3 rows and 3 columns 
def resetBoard(board): 
    # initializes and resets game board 
    board = [[" "]*7 for _ in range(6)]  #6 rows and 7 columns 
    printBoard(board)
    return board

def printBoard(board):
    # displays and updates game board
    # print rows 6 to 1
    for r in range(6, 0, -1):
        row = f"| {r} | {board[r-1][0]} | {board[r-1][1]} | {board[r-1][2]} | {board[r-1][3]} | {board[r-1][4]} | {board[r-1][5]} | {board[r-1][6]} |"
        print(row)
        print(" " + "-" * 33)
    
    print("|R\\C| a | b | c | d | e | f | g |")
    print(" " + "-" * 33)

def validateEntry(row, col, board): 
    #return True if the user entered inputs are valid (space empty and abcdefg,123456)
    # rows = len(board)
    # cols = len(board[0]) if rows > 0 else 0

    # if col not in "abcdefg":
    #     print("Invalid entry: column must be a–g.")
    #     return False
    # # bounds check (expects 0-based indices: row 0–5, col 0–6)
    # if not (0 <= row < rows) or not (0 <= col < cols):
    #     print("Invalid entry: try again.\nRows must be 1–6 and columns a–g.")
    #     return False

    # # occupancy check
    # if board[row][col] != " ":
    #     print("That cell is already taken. \nPlease make another selection.")
    #     return False

    print("Thank you for your selection.")
    return True

def availablePosition(board): 
    #returns a 2D list of available positions 
    positions = [] 
    columnLabels = "abcdefg"
    #check each row and if there is an item in the row then print the row above 
    #at the beginning should print "Available positions are: ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1'] "
    for c in range(len(columnLabels)):      #loop over 7 columns
        for r in range(len(board)):       # loop rows bottom → top
            if board[r][c] == " ":
                positions.append(f"{columnLabels[c]}{r+1}")
                break   #need lowest available box per column
    print("Available positions are:", positions)
    return positions

def checkFull(board): 
    # returns True if the board is full, otherwise False
    for row in board: 
        for col in row:   
            if col == " ":  #found empty space
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

    #needs to check all rows
    for r in range(6):
        for c in range(7 - 3):
            if (board[r][c] == turn and board[r][c+1] == turn and
                board[r][c+2] == turn and board[r][c+3] == turn):
                print(f"\n{turn} IS THE WINNER!!!")
                return True

    #cols
    for r in range(6 - 3):
        for c in range(7):
            if (board[r][c] == turn and board[r+1][c] == turn and #checks each position and +1 from bottom up 
                board[r+2][c] == turn and board[r+3][c] == turn):
                print(f"\n{turn} IS THE WINNER!!!")
                return True

    #diag needs to check right diagonals 
    for r in range(6 - 3):
            for c in range(7 - 3):
                if (board[r][c] == turn and board[r+1][c+1] == turn and #checks position and +1 across 
                    board[r+2][c+2] == turn and board[r+3][c+3] == turn):
                    print(f"\n{turn} IS THE WINNER!!!")
                    return True

    #diag needs to check up diags 
    for r in range(3, 6):
            for c in range(7 - 3):
                if (board[r][c] == turn and turn[r-1][c+1] == turn and
                    board[r-2][c+2] == turn and board[r-3][c+3] == turn):
                    print(f"\n{turn} IS THE WINNER!!!")
                    return True        

    return False

def main():
    while True:
        turn = "X"
        print(f"New Game: {turn} goes first.\n")
        
        #define board 
        board = [[" " for _ in range(6)]for _ in range(7)]

        #game begins with a clean board 
        board = resetBoard(board)

        while True:     
            print(f"\n{turn}'s turn.")
            print(f"Where do you want your {turn} placed? ")
            availablePosition(board)
            entry = input("\nPlease enter column-letter and row-number (e.g., a1): ").strip().lower()  
            #split entry to letter and num 
            colLetter = entry[0] 
            rowNum = int(entry[1:])

            
            col = "abcdefgghijklmnopqrstuv".index(colLetter)
            row = rowNum-1

            isValid = validateEntry(row, col, board)
            #run validEntry again if validate Entry is false 
            if not isValid: 
                continue
        
            ## next step put the turns in boxes 

            board[row][col] = turn

            isEnd = checkEnd(board,turn)
            printBoard(board)
    

            if isEnd: 
                again = input("\nAnother game? (y/n)? ")
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
