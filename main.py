import time
from RandomBot import RandomBot

# Board dimensions in cells
BOARD_WIDTH = 7
BOARD_HEIGHT = 6

def calculate_move_row(board, move_column):
    for i in range(BOARD_HEIGHT):
        if board[i][move_column] == 0:
            return i
        
def update_board(board, move_column, move_row, turn):
    board[move_row][move_column] = turn
    return board

def is_legal_move(board, move_column):
    if move_column not in range(0, BOARD_WIDTH):  # tried to play outside board
        return False
    if board[BOARD_HEIGHT - 1][move_column] != 0:  # tried to play in full column
        return False
    else:
        return True
    
def get_surrounding_elements(board, row, col):
    # Dimensions of the board
    rows = len(board)
    cols = len(board[0])
    
    # Define the directions and their corresponding names
    directions = {
        "horizontal_right": (0, 1),
        "vertical_down": (1, 0),
        "diagonal_down_right": (1, 1),
        "diagonal_down_left": (1, -1)
    }
    
    def get_elements_in_direction(start_row, start_col, delta_row, delta_col):
        elements = []
        for i in range(-3, 4):  # Collect 7 elements, from -3 to +3
            r = start_row + i * delta_row
            c = start_col + i * delta_col
            if 0 <= r < rows and 0 <= c < cols:
                elements.append(board[r][c])
            else:
                elements.append(None)  # Use None to indicate out-of-bounds
        return elements
    
    results = {}
    
    # Check all directions
    for direction_name, (delta_row, delta_col) in directions.items():
        results[direction_name] = get_elements_in_direction(row, col, delta_row, delta_col)
    
    return results

def has_four_in_a_row(lst):
    for i in range(len(lst) - 3):
        if lst[i] == lst[i + 1] == lst[i + 2] == lst[i + 3]:
            return True
    return False
  
def game_is_won(board, move_column, move_row):
    directional_lists = get_surrounding_elements(board, move_row, move_column)
    for lst in directional_lists.values():
        if has_four_in_a_row(lst):
            return True
    return False

def display_board(board):
    for i in range(BOARD_HEIGHT):
        print(board[BOARD_HEIGHT - i - 1])

def simulate_game(playerOne, playerTwo):
    board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    # display_board(board)
    turn = 1
    move_counter = 0

    game_summary = {
        'winner' : None, 
        'exit_status' : 0,
    }

    game_ended = False
    while game_ended == False:
        board_copy = board.copy()
        if turn == 1:
            move_column = playerOne.decide_move(board_copy, turn) # Maximum computation time?
        else:
            move_column = playerTwo.decide_move(board_copy, turn)
            
        if not is_legal_move(board, move_column):
            game_summary['winner'] = 3 - turn
            game_summary['exit_status'] = 'Illegal move'
            return game_summary
        
        move_row = calculate_move_row(board=board, move_column=move_column)        
        board = update_board(board=board, move_column=move_column, move_row=move_row, turn=turn)
        # display_board(board)
        if game_is_won(board, move_column, move_row):
            game_summary['winner'] = turn
            return game_summary

        turn = 3 - turn
        move_counter += 1
        if move_counter == BOARD_HEIGHT * BOARD_WIDTH:
            game_summary['winner'] = 3
            return game_summary

from tqdm import tqdm

iterations = 100000
player_one_wins = 0
player_two_wins = 0
draws = 0
player_one_illegal_moves = 0
player_two_illegal_moves = 0

for i in tqdm(range(iterations)):
    playerOne = RandomBot()
    playerTwo = RandomBot()
    game_summary = simulate_game(playerOne, playerTwo)
    if game_summary['winner'] == 1:
        player_one_wins += 1
    elif game_summary['winner'] == 2:
        player_two_wins += 1
    else:
        draws += 1
    
    if (game_summary['winner'] == 1)&(game_summary['exit_status'] == "Illegal move"):
        player_two_illegal_moves += 1
    if (game_summary['winner'] == 2)&(game_summary['exit_status'] == "Illegal move"):
        player_one_illegal_moves += 1
    
print('Win rate: ', player_one_wins/iterations)
print('Loss rate: ', player_two_wins/iterations)
print('Draw rate: ', draws/iterations)
print('Actual draws: ', draws)
print('P1 illegal moves: ', player_one_illegal_moves)
print('P2 illegal moves: ', player_two_illegal_moves)