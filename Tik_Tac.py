import os

def print_board(x_state, z_state):
    board = [' ' if x_state[i] == 0 and z_state[i] == 0 else 'X' if x_state[i] == 1 else 'O' for i in range(9)]
    
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(x_state, z_state):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    
    for win in wins:
        if x_state[win[0]] == x_state[win[1]] == x_state[win[2]] == 1:
            return "X"
        if z_state[win[0]] == z_state[win[1]] == z_state[win[2]] == 1:
            return "O"
    if 0 not in x_state and 0 not in z_state:
        return "Tie"
    return None

if __name__ == "__main__":
    x_state = [0] * 9
    z_state = [0] * 9
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')
        print_board(x_state, z_state)
        
        if turn == 1:
            player = 'X'
        else:
            player = 'O'
        
        print(f"{player}'s Chance")
        value = int(input("Please enter a value (0-8): "))
        
        if value < 0 or value > 8 or x_state[value] == 1 or z_state[value] == 1:
            print("Invalid move. Try again.")
            continue
        
        if turn == 1:
            x_state[value] = 1
        else:
            z_state[value] = 1
        
        winner = check_win(x_state, z_state)
        if winner:
            if winner == "Tie":
                print("It's a Tie!")
            else:
                print(f"{winner} won the match!")
            break
        
        turn = 1 - turn
