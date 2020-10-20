game_board = {"1": " ", "2": " ", "3": " ",
            "4": " ", "5": " ", "6": " ",
            "7": " ", "8": " ", "9": " "}

board_keys = []

for key in game_board:
    board_keys.append(key)

def printGBoard(board):
    print("\t     |     |")
    print("\t  " + board["1"] + "  |  " + board["2"] + "  |  " + board["3"])
    print("\t_____|_____|_____")

    print("\t     |     |")
    print("\t  " + board["4"] + "  |  " + board["5"] + "  |  " + board["6"])
    print("\t_____|_____|_____")

    print("\t     |     |")
    print("\t  " + board["7"] + "  |  " + board["8"] + "  |  " + board["9"])
    print("\t     |     |")

def game():
    turn = "X"
    count = 0

    for i in range(10):
        printGBoard(game_board)
        print("Сейчас ходит " + turn + ". Выберите клетку.")

        move = input()

        if game_board[move] == " ":
            game_board[move] = turn
            count += 1
        else:
            print("Эта клетка уже занята.\nВыберите другую клетку.")
            continue

        if count >= 5:
            if game_board["1"] == game_board["2"] == game_board["3"] != " ":
                printGBoard(game_board)
                print("\nИгра завершена.\n")
                print(" * " + turn + " выиграл. *")
                break
            elif game_board["4"] == game_board["5"] == game_board["6"] != " ":
                printGBoard(game_board)
                print("\nИгра завершена.\n")
                print(" * " + turn + " выиграл. *")
                break
            elif game_board["7"] == game_board["8"] == game_board["9"] != " ":
                printGBoard(game_board)
                print("\nИгра завершена.\n")
                print(" * " + turn + " выиграл. *")
                break
            elif game_board["1"] == game_board["4"] == game_board["7"] != " ":
                printGBoard(game_board)
                print("\nИгра завершена.\n")
                print(" * " + turn + " выиграл. *")
                break
            elif game_board["2"] == game_board["5"] == game_board["8"] != " ":
                printGBoard(game_board)
                print("\nИгра завершена.\n")
                print(" * " + turn + " выиграл. *")
                break
            elif game_board["3"] == game_board["6"] == game_board["9"] != " ":
                printGBoard(game_board)
                print("\nИгра завершена.\n")
                print(" *" + turn + " выиграл. *")
                break
            elif game_board["7"] == game_board["5"] == game_board["3"] != " ":
                printGBoard(game_board)
                print("\nИгра завершена.\n")
                print(" * " + turn + " выиграл. *")
                break
            elif game_board["1"] == game_board["5"] == game_board["9"] != " ":
                printGBoard(game_board)
                print("\nИгра завершена.\n")
                print(" * " + turn + " выиграл. *")
                break

        if count == 9:
            print("\nИгра завершена.\n")
            print("Ничья!")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart = input("Хотите сыграть еще раз? (Да/Нет) ")
    if restart == "Да" or restart == "да":
        for key in board_keys:
            game_board[key] = " "

        game()

game()
