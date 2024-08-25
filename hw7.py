def collatz(n):
    seq = [n]
    if n == 1 and len(seq) <= 1: 
        return seq
    if n % 2 == 0: 
        new = n//2
        seq = [n] + collatz(new)
    else:
        new = n * 3 + 1
        seq = [n] + collatz(new)
    return seq 

# print(collatz(5))  
# print(collatz(1))  
# print(collatz(123))  

def find_min(num_list): 
    if len(num_list) == 1: 
        min = num_list[0]
        return min
    min = num_list[0]
    if find_min(num_list[1:]) > min: 
        return min
    else: 
        min  = find_min(num_list[1:])
    return min
 
# print(find_min([8]))  
# print(find_min([0, 2, -5, -2, 5, -1, 4, 0, -5, -1]))
# print(find_min([30, 40, 20, 34, 32, 34, 48, 43, 21]))  
        
import random
# returns a list of indexes where there are open slots 
def open_slots(board): 
    indexes = []
    for i in range(len(board)): 
        if board[i] == '-': 
            indexes.append(i)    
    return indexes

# returns the winner if there is one, a draw or - space depending on situation 
def winner(board):
    win_conditions = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Center column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal
        (2, 4, 6)   # Diagonal
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != '-':
            return board[a]
    
    if '-' in board:
        return '-'  # Game is still ongoing
    
    return 'D'  # Draw

# Testing the winner function
# print(winner(['X', 'X', 'X', '-', '-', '-', '-', '-', '-']))  # Should return 'X'
# print(winner(['O', 'O', 'O', '-', '-', '-', '-', '-', '-']))  # Should return 'O'
# print(winner(['X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X']))  # Should return 'X'
# print(winner(['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O']))  # Should return 'D'

# finishes the game and forces a winner 
def force_win(board): 
    index_list = open_slots(board)
    
    if (len(index_list)) % 2 == 0: 
        turn = 'O'
    else:
        turn = 'X'
         
    result = winner(board)
    if result != '-': 
        if result == 'X':
            return 1
        if result == 'O': 
            return -1
        if result == 'D': 
            return 0
    
    state_list = []
    
    if turn == 'X':
        for val in index_list:
            board_copy = board[:]  
            board_copy[val] = 'X' 
            state = force_win(board_copy)
            state_list.append(state)
        return max(state_list)
    
    if turn == 'O':
        for val in index_list:
            board_copy = board[:]  
            board_copy[val] = 'O'
            state = force_win(board_copy)
            state_list.append(state)
        return min(state_list) 

# Will automatically always make 'O' win 
# finding the optimal index to place 'O' to force a win or draw for 'O'
def tic_tac_toe():
    board = ['-'] * 9
    while open_slots(board):
        xindex = random.choice(open_slots(board))
        board[xindex] = 'X'
        if winner(board) != '-':
            return winner(board)
        
        if not open_slots(board):  # Check if the board is full
            return winner(board)
        
        option = []
        slots = open_slots(board) # [5,6]
        for val in slots:
            board_copy = board[:]  
            board_copy[val] = 'O'
            option.append(force_win(board_copy))
        for i in range(len(option)): 
            if option[i] == min(option): 
                oindex = slots[i]
                board[oindex] = 'O'
            
        if winner(board) != '-':
            return winner(board)
    
    return winner(board)

# Testing tic_tac_toe function
#print(tic_tac_toe())  # Should print the result of a random game


def play_games(n):
    X = O = D = 0
    for _ in range(n):
        result = tic_tac_toe()
        if result == 'X':
            X += 1
        elif result == 'O':
            O += 1
        elif result == 'D':
            D += 1
        
    print("X wins: " + str(X))
    print("O wins: " + str(O))
    print("D wins: " + str(D))

# Testing play_games function
# print(play_games(1))    # Should print results for a single game
# print(play_games(100))  # Should print results for 100 games
# print(play_games(10000))  # Should print results for 10000 games

    
# print(open_slots(['-', '-', '-', '-', '-', '-', '-', '-', '-']))
# print(open_slots(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O']))
# print(open_slots(['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']))
# print(open_slots(['X', 'X', 'O', '-', 'X', '-', 'X', 'O', 'O']))

# print(winner(['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O']))
# print(winner(['X', '-', 'O', 'X', 'O', '-', 'O', '-', 'X']))
# print(winner(['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']))
# print(winner(['X', 'X', 'O', '-', 'X', '-', 'X', 'O', 'O']))
# print(winner(['-', '-', '-', 'X', 'X', 'X', 'O', 'O', '-']))

# print(tic_tac_toe())
# print(tic_tac_toe())
# print(tic_tac_toe())

print(play_games(1))
print(play_games(100))
# print(play_games(10000))


# print(force_win(['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']))
# print(force_win(['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O']))
# print(force_win(['X', '-', 'O', 'X', 'O', '-', 'O', '-', 'X']))
# print(force_win(['X', 'O', 'X', 'X', 'O', 'X', '-', '-', 'O'])) # equaling 0 instead of -1
# print(force_win(['X', 'O', 'X', 'X', 'O', '-', '-', 'X', 'O']))
# print(force_win(['-', 'O', '-', '-', 'X', 'X', '-', 'O', 'X']))
# print(force_win(['-', 'O', '-', '-', 'X', '-', '-', '-', '-']))
# print(force_win(['-', '-', '-', '-', '-', '-', '-', '-', '-'])) #equaling 1 instead of 0
