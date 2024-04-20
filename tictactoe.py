def board() : 
    play_board = [["1", "2", "3"],
                  ["4", "5", "6"],
                  ["7", "8", "9"]]

    return play_board

# func to take input from user and input it in the game board    
def board_input(player) : 
    # play_board = board()
    
    correct_pos = False
    #position = int(input("Enter the position : "))
    while correct_pos == False : 
        position = int(input("Enter the position : "))
        illegal = check_illegal(position, player)
        if illegal == 1 : 
            continue
        if position == 1 : 
            play_board[0][0] = player
            correct_pos = True
        elif position == 2 : 
            play_board[0][1] = player
            correct_pos = True
        elif position == 3 : 
            play_board[0][2] = player
            correct_pos = True
        elif position == 4 : 
            play_board[1][0] = player
            correct_pos = True
        elif position == 5 : 
            play_board[1][1] = player
            correct_pos = True
        elif position == 6 : 
            play_board[1][2] = player
            correct_pos = True
        elif position == 7 : 
            play_board[2][0] = player
            correct_pos = True
        elif position == 8 : 
            play_board[2][1] = player
            correct_pos = True
        elif position == 9 : 
            play_board[2][2] = player
            correct_pos = True
        else : 
            print("INVALID POSITION")
            correct_pos = False
    
    
    
    display_board(play_board)
    
    # check win condition by sending playboard and current player(X or O)
    win_condition = check_win(play_board, player)
    
    # declare winner accordingly or move on to next player
    if(win_condition == 1) : 
        print(str(player)+" IS THE WINNER")
        exit(1)
    else : 
        return 0

    
def player_turn(count) : 
    #print("There are two players : Player O and Player X") 
    if count == 9 : 
        print("TIE")
        exit(1)
    if count % 2 != 0 : 
        print("Player X turn : ")
        board_input("X")
    else : 
        print("Player O")
        board_input("O")

def check_win(play_board, player) :
        
    # check rows for win
    row = 0
    while row < 3 : 
        if (play_board[row][0] == play_board[row][1] == play_board[row][2] == player) : 
            flag = 1
            return flag
        else : 
            flag = 0
        row += 1
        
    # check columns for win
    column = 0
    while column < 3 : 
        if (play_board[0][column] == play_board[1][column] == play_board[2][column] == player) : 
            flag = 1
            return flag
        else : 
            flag = 0
        column += 1
    
    # check diagonals for win
    if (play_board[0][0] == play_board[1][1] == play_board[2][2] == player) : 
        flag = 1
    elif (play_board[0][2] == play_board[1][1] == play_board[2][0] == player) : 
        flag = 1
    else : 
        flag = 0
		
    # return flag which indicates the win condition (1 is win ; 0 is no win)
    return flag
    
    
    
def display_board(play_board)  :
    for i in play_board : 
        for j in i : 
            print(j, end="  |  ")
        print()
    
    
def check_illegal(position, player) : 
    row = 0
    column = 0
    while row < 3 : 
        while column < 3 : 
            if play_board[row][column] == position == player : 
                print("Square is already filled! Choose another one")
                return 1
            else : 
                return 0
            column += 1
        row += 1
    
def main() : 


    print("There are 2 players : Player O and Player X")
    count = 0
    while count < 10 : 
        player_turn(count)
        count += 1
    print(count)
            
            
            
            
            
            
            
            
            
            
            
# play_board is a global variable  
play_board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]  
            
main()