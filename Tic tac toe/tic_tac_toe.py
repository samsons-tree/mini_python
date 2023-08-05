from random import choice
from time import sleep

def create_grid() -> dict:
    ''' Initialise grid dictionary. 
    Output: dict of 1:None, 2:None, ... 9:None.'''
    grid = dict()
    for n in range(1,10):
        grid[n] = f'{n}'
    return grid

def display_grid(grid) -> None:
    ''' 1,2,3 represent first row; 4,5,6 the second and 7,8,9 the third.'''
    output = f'''
     --- --- ---
    | {grid[1]} | {grid[2]} | {grid[3]} |
     --- --- ---
    | {grid[4]} | {grid[5]} | {grid[6]} |
     --- --- ---
    | {grid[7]} | {grid[8]} | {grid[9]} |
     --- --- ---'''
    print(output)

def next_move(grid: dict, player: str) -> None:
    square = input('Choose you move. Input: 1 - 9\n')
    square = int(square)
    if grid[square] == 'X' or grid[square] == 'O':
        print("This move has already been taken... Try again.")
        next_move(grid, player)
    else:
        if player == 'X':
            grid[square] = 'X'
        if player == 'O':
            grid[square] = 'O'
            
def bot_move(grid: dict, player) -> None:
    ''' Bot will choose a random valid square to place marker. '''
    square = choice(range(1,10))
    if grid[square] == 'X' or grid[square] == 'O':
        bot_move(grid, player)
    else:
        if player == 'O':
         grid[square] = 'O'
        elif player == 'X':
            grid[square] = 'X'

def smart_bot(grid, player):
    ''' Bot will look for moves to stop player from winning, or if it can win, on next move.
    If there is no best move, bot will use bot_move() to choose random square.'''
    combinations = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
    move = False
    for element in combinations:
        check = []
        for n in range(3):
            check.append(grid[element[n]])
        if (check[0:2] == ['X', 'X'] or check[0:2] == ['O', 'O']) and (grid[element[2]] != 'X' and grid[element[2]] != 'O'):
            if player == 'O':
                grid[element[2]] = 'O'
            elif player == 'X':
                grid[element[2]] = 'X'
            move = True
            break
        elif (check[1:3] == ['X', 'X'] or check[1:3] == ['O', 'O']) and (grid[element[0]] != 'X' and grid[element[0]] != 'O'):
            if player == 'O':
                grid[element[0]] = 'O'
            elif player == 'X':
                grid[element[0]] = 'X'
            move = True
            break
        elif ((check[0] == 'X' and check[2] == 'X') or check[0] == 'O' and check[2] == 'O') and (grid[element[1]] != 'X' and grid[element[1]] != 'O'):
            if player == 'O':
                grid[element[1]] = 'O'
            elif player == 'X':
                grid[element[1]] = 'X'
            move = True
            break
    if move == False:
        bot_move(grid, player)

def check_win(grid) -> str:
    ''' Check against all combinations which mean a player/bot has won. '''
    combinations = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
    for element in combinations:
        check = []
        for n in range(3):
            check.append(grid[element[n]])
        if check == ['X','X','X']:
           return 'X'
        elif check == ['O','O','O']:
            return 'O'
    return 'no' 
        
def choose_player() -> str:
    ''' Choose a player to begin the game as 'X'. '''
    X = choice(['Human', 'Bot'])
    print(f'{X} will begin as "X".')
    return X

def tic_tac_toe(start = 'Human'):
    ''' Structure the game.
    Default game starter (as X) is Human. '''
    grid = create_grid()
    if start == 'Human':
        display_grid(grid)
    count = 0
    win = ''
    if start == 'Human':
        while count < 9:
            if count % 2 == 0:
                next_move(grid,'X')
                display_grid(grid)
                win = check_win(grid)
            if count % 2 == 1:
                sleep(0.5)
                smart_bot(grid, 'O')
                display_grid(grid)
                win = check_win(grid)
            if win != 'no':
                break
            count += 1
    elif start == 'Bot':
        while count < 9:
            
            if count % 2 == 0:
                sleep(0.5)
                smart_bot(grid, 'X')
                display_grid(grid)
                win = check_win(grid)
            if count % 2 == 1:
                next_move(grid,'O')
                display_grid(grid)
                win = check_win(grid)
            if win != 'no':
                break
            count += 1
    if win != 'no':
        numbers = '0123456789'
        for n in range(1,10):
            if grid[n] in numbers:
                grid[n] = ''
        print(f'{win} wins!')
    else:
        print("Ends in a draw...")

def play():
    starter = choose_player()
    sleep(1)
    tic_tac_toe(starter)
    again = int(input('''Want to play again? (1 = yes /2 = no)'''))
    if again == 1:
        play()

if __name__ == '__main__':
    play()
