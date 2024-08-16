import random
def wizards(grades, life, sleep): 
    wizards = []
    for i in grades: 
        if(i in life and i in sleep): 
            wizards.append(i)
    return wizards

# print(wizards(['Harry', 'Hermione'], ['Harry', 'Ron'], ['Hermione', 'Ron']))
# print(wizards(['Aragorn', 'Frodo', 'Gandalf'], ['Aragorn', 'Gandalf', 'Gimli', 'Pippin'], ['Gandalf', 'Pippin'])
# )
# print(wizards(['Zelda'], [], ['Ganondorf', 'Link', 'Zelda']))
# print(wizards(['Mary', 'Spock', 'Sue'], ['Kirk', 'Mary', 'Sue'], ['Mary', 'Sue']))


def open_slots(board): 
    indexes = []
    for i in range(len(board)): 
        if board[i] == '-': 
            indexes.append(i)    
    return indexes

def winner(board): 
        
    if (board[0] == board[1] == board[2] == 'X') or (board[0] == board[1] == board[2] == 'O'): 
        return board[0]
    if (board[3] == board[4] == board[5] == 'X') or (board[3] == board[4] == board[5] == 'O'): 
        return board[3]
    if (board[6] == board[7] == board[8] == 'X') or (board[6] == board[7] == board[8] == 'O'): 
        return board[6]
    if (board[0] == board[3] == board[6] == 'X') or (board[0] == board[3] == board[6] == 'O'): 
        return board[0]
    if (board[1] == board[5] == board[7] == 'X') or (board[1] == board[5] == board[7] == 'O'): 
        return board[1]
    if (board[2] == board[6] == board[8] == 'X') or (board[2] == board[6] == board[8] == 'O'): 
        return board[2]
    if (board[0] == board[4] == board[8] == 'X') or (board[0] == board[4] == board[8] == 'O'): 
        return board[0]
    if (board[2] == board[4] == board[6] == 'X') or (board[2] == board[4] == board[6] == 'O'): 
        return board[2]
    for i in board: 
        if i == '-': 
            return '-'
    else: 
        return 'D'
    
def tic_tac_toe(): 
    board = ['-','-', '-', '-', '-', '-', '-', '-', '-']
    while(len(open_slots(board)) > 0): 
        xindex = random.choice(open_slots(board))
        board[xindex] = 'X'
        if (open_slots(board) == []): 
            return winner(board)
        else: 
            oindex = random.choice(open_slots(board))
            board[oindex] = 'O'
            open_slots(board)
    
    return winner(board)

def play_games(n): 
    X = 0
    O = 0
    D = 0
    for i in range(n): 
        if tic_tac_toe() == 'X': 
            X = X + 1 
        if tic_tac_toe() == 'O': 
            O = O + 1 
        if tic_tac_toe() == 'D': 
            D = D + 1 
        
    print("X wins: " + str(X))
    print("O wins: " + str(O))
    print("D wins: " + str(D))
        
        
    
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
print(play_games(10000))

