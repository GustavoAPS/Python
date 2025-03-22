# Print ticTacToe matrix
def print_matrix(values):
    print(f" {values[0][0]} | {values[0][1]} | {values[0][2]} ")
    print(f" {values[1][0]} | {values[1][1]} | {values[1][2]} ")
    print(f" {values[2][0]} | {values[2][1]} | {values[2][2]} ")


# Variables
player_one_turn = True
game_over = False
values_matrix = [['_', '_', '_'],
                 ['_', '_', '_'],
                 ['_', '_', '_']]

# Game Loop
while not game_over:
    print_matrix(values_matrix)
    row = int(input("Player x what row do you want? [0-2]"))
    col = int(input("Player x what col do you want? [0-2]"))
    values_matrix[row][col] = 'x'
