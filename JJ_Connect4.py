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
    print(" " + "-" * 33)

    # print rows 6 → 1
    for r in range(6, 0, -1):
        row = f"| {r} | {board[r-1][0]} | {board[r-1][1]} | {board[r-1][2]} | {board[r-1][3]} | {board[r-1][4]} | {board[r-1][5]} | {board[r-1][6]} |"
        print(row)
        print(" " + "-" * 33)
    
    print("|R\\C| a | b | c | d | e | f | g |")
    print(" " + "-" * 33)

def validateEntry(row,col,board): 
    #returns true if user entered inputs are valid, otherwise returns False
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
            if col == " ":  # found an empty space
                return False
    
    print("DRAW! NOBODY WINS!")
    return True

# def checkEnd(board, turn): 
#     #returns True if game is over, otherwise False
#     if checkFull(board) or checkWin(board,turn): 
#         return True
#     else: 
#         return False

# def checkWin(board,turn): 
#     #returns True when 'X' or 'O' becomes winner, otherwise False 

#     #rows
#     for r in range(3):
#         if board[r][0] == board[r][1] == board[r][2] == turn:
#             print(f"{turn} IS THE WINNER!!!")
#             return True

#     #cols
#     for c in range(3):
#         if board[0][c] == board[1][c] == board[2][c] == turn:
#             print(f"{turn} IS THE WINNER!!!")
#             return True

#     #diag
#     if (board[0][0] == board[1][1] == board[2][2] == turn) or \
#        (board[0][2] == board[1][1] == board[2][0] == turn):
#         print(f"{turn} IS THE WINNER!!!")
#         return True

#     return False

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
            entry = input("Please enter column-letter and row-number (e.g., a1): ").strip().lower()  
            col = entry[0]
            row = int(entry[1:])

            isValid = validateEntry(row, col, board)
            #run validEntry again if validate Entry is false 
            if not isValid: 
                continue
        
            ## next step put the turns in boxes 
            
            # board[row][col] = turn

            # isEnd = checkEnd(board,turn)
            # printBoard(board)
            

            # if isEnd: 
            #     again = input("\nAnother game? Enter Y or y for yes.\n")
            #     if again.lower() == "y":
            #         break 
            #     else: 
            #         print("Thank you for playing!")
            #         return 
                
            #switch players 
            if turn == "X":
                turn ="O"
            else: 
                turn = "X"

        


#calls main function 
if __name__ == "__main__": 
    main() 
