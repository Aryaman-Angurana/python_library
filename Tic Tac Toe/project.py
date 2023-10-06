matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

player = "X"

values = []


def draw():
    for i in range(0, 3):
        for j in range(0, 3):
            print(matrix[i][j], end="   ")
        print()


def insert(entered_values):
    while True:
        value = int(input("It's the turn of player " + player + ". please enter the value"))
        if value > 9 or value < 0 or value in entered_values:
            print("Invalid value")
            continue
        entered_values += [value]
        break
    value -= 1
    matrix[int(value / 3)][value % 3] = player


def toggle_player(playing):
    if playing == "X":
        return "O"
    else:
        return "X"


def win():
    for i in range(0, 3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] or matrix[0][i] == matrix[1][i] == matrix[2][i]:
            return matrix[i][i]
    if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[1][1]
    return " "


draw()
count = 0
while True:
    insert(values)
    player = toggle_player(player)
    draw()
    if count == 9:
        break
    if win() == "X" or win() == "O":
        print("player", win(), "has won the game")
        break
    count += 1
