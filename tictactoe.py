def creation():
    symbols = input()

    list_symbols = []
    for i in range(3):
        list_symbols.append(symbols[i*3:(i+1)*3])

    for i in range(3):
        row = " ".join(list_symbols[i])
        print("| "+row+" |")

    #print(list_symbols[1][0])
    return list_symbols


def horizontal_check(list_game):
    x_win, o_win = 0, 0
    if list_game[0][0] == 'X' and list_game[0][1] == 'X' and list_game[0][2] == 'X':
        x_win = 1
    elif list_game[1][0] == 'X' and list_game[1][1] == 'X' and list_game[1][2] == 'X':
        x_win = 1
    elif list_game[2][0] == 'X' and list_game[2][1] == 'X' and list_game[2][2] == 'X':
        x_win = 1

    if list_game[0][0] == 'O' and list_game[0][1] == 'O' and list_game[0][2] == 'O':
        o_win = 1
    elif list_game[1][0] == 'O' and list_game[1][1] == 'O' and list_game[1][2] == 'O':
        o_win = 1
    elif list_game[2][0] == 'O' and list_game[2][1] == 'O' and list_game[2][2] == 'O':
        o_win = 1

    if x_win == 1 and o_win == 0:
        return "X wins"
    elif o_win == 1 and x_win == 0:
        return "O wins"
    elif x_win == 1 and o_win == 1:
        return "Impossible"


def vertical_check(list_game):
    x_win, o_win = 0, 0
    if list_game[0][0] == 'X' and list_game[1][0] == 'X' and list_game[2][0] == 'X':
        x_win = 1
    elif list_game[0][1] == 'X' and list_game[1][1] == 'X' and list_game[2][1] == 'X':
        x_win = 1
    elif list_game[0][2] == 'X' and list_game[1][2] == 'X' and list_game[2][2] == 'X':
        x_win = 1

    if list_game[0][0] == 'O' and list_game[1][0] == 'O' and list_game[2][0] == 'O':
        o_win = 1
    elif list_game[0][1] == 'O' and list_game[1][1] == 'O' and list_game[2][1] == 'O':
        o_win = 1
    elif list_game[0][2] == 'O' and list_game[1][2] == 'O' and list_game[2][2] == 'O':
        o_win = 1

    if x_win == 1 and o_win == 0:
        return "X wins"
    elif o_win == 1 and x_win == 0:
        return "O wins"
    elif x_win == 1 and o_win == 1:
        return "Impossible"


def diagonal_check(list_game):
    x_win, o_win = 0, 0

    if list_game[0][0] == 'X' and list_game[1][1] == 'X' and list_game[2][2] == 'X':
        x_win = 1
    elif list_game[0][2] == 'X' and list_game[1][1] == 'X' and list_game[2][0] == 'X':
        x_win = 1

    if list_game[0][0] == 'O' and list_game[1][1] == 'O' and list_game[2][2] == 'O':
        o_win = 1
    elif list_game[0][2] == 'O' and list_game[1][1] == 'O' and list_game[2][0] == 'O':
        o_win = 1

    if x_win == 1 and o_win == 0:
        return "X wins"
    elif o_win == 1 and x_win == 0:
        return "O wins"
    elif x_win == 1 and o_win == 1:
        return "Impossible"


def counter_x_o(list_game):
    cpt_x = 0
    cpt_o = 0
    cpt_ = 0
    for i in range(len(list_game)):
        for c in list_game[i]:
            if c == 'X':
                cpt_x += 1
            if c == 'O':
                cpt_o += 1
            if c == '_':
                cpt_ += 1
    #print(cpt_o, cpt_x, cpt_)
    if cpt_x - cpt_o >= 2 or cpt_o - cpt_x >= 2:
        return 'Impossible'

    if (cpt_x - cpt_o < 2) or (cpt_o - cpt_x < 2):
        if cpt_ > 0 and horizontal_check(list_game) is None and vertical_check(list_game) is None and diagonal_check(list_game) is None:
            return "Game not finished"


def move(list_game, play):
    b = True

    coordinates = list(input())
    coordinates.pop(1)

    while not (coordinates[0].isdigit() and coordinates[1].isdigit()):
        print("You should enter numbers!")
        coordinates = list(input())
        coordinates.pop(1)

    row = int(coordinates[0])
    col = int(coordinates[1])
    print(row, col)

    while b:
        if (3 < row or row < 1) or (3 < col or col < 1):
            print("Coordinates should be from 1 to 3!")
            b = False
            break

        if list_game[row-1][col-1] != '_':
            print("This cell is occupied! Choose another one!")
            b = False
            break
        else:
            row_game = list(list_game[row-1])
            row_game[col-1] = play
            new_row_game = "".join(row_game)

            list_game[row-1] = new_row_game
            return list_game

    if not b:
        move(list_game, play)


def print_tab(list_game):
    print("---------")
    for i in range(3):
        row = " ".join(list_game[i])
        print("| " + row + " |")
    print("---------")


def new_game():
    new_game = ['___', '___', '___']
    print_tab(new_game)
    return new_game


def main():
    turn = 0
    L = new_game()


    while counter_x_o(L) is not None:
        #print(counter_x_o(L))
        if turn % 2 == 0:
            move(L, 'X')
            print_tab(L)
            turn += 1
        else:
            move(L, 'O')
            print_tab(L)
            turn += 1

        if horizontal_check(L) is not None:
            print(horizontal_check(L))
            break

        if vertical_check(L) is not None:
            print(vertical_check(L))
            break

        if diagonal_check(L) is not None:
            print(diagonal_check(L))
            break

        elif horizontal_check(L) is None and vertical_check(L) is None and diagonal_check(L) is None and counter_x_o(
                L) is None:
            print('Draw')
            break


if __name__ == "__main__":
    main()
