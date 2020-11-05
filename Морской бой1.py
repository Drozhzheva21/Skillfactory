import random
import os
from random import randint

class Ship:
    def __init__(self, size, orientation, location):
        self.size = size

        if orientation == "по горизонтали" or orientation == "по вертикали":
            self.orientation = orientation
        else:
            raise ValueError('Значение должно быть "по горизонтали" или "по вертикали".')

        if orientation == "по горизонтали":
            if location["строка"] in range(row_size):
                self.coordinates = []
                for index in range(size):
                    if location["столбец"] + index in range(col_size):
                        self.coordinates.append({"строка": location["строка"], "столбец": location["столбец"] + index})
                    else:
                        raise IndexError("Столбец выходит за пределы поля.")
            else:
                raise IndexError("Строка выходит за пределы поля.")
        elif orientation == "по вертикали":
            if location["столбец"] in range(col_size):
                self.coordinates = []
                for index in range(size):
                    if location["строка"] + index in range(row_size):
                        self.coordinates.append({"строка": location["строка"] + index, "столбец": location["столбец"]})
                    else:
                        raise IndexError("Строка выходит за пределы поля.")
            else:
                raise IndexError("Столбец выходит за пределы поля.")

        if self.filled():
            print_board(board)
            print(" ".join(str(coords) for coords in self.coordinates))
            raise IndexError("Корабль уже занимает это место.")
        else:
            self.fillBoard()

    def filled(self):
        for coords in self.coordinates:
            if board[coords["строка"]][coords["столбец"]] == 1:
                return True
        return False

    def fillBoard(self):
        for coords in self.coordinates:
            board[coords["строка"]][coords["столбец"]] = 1

    def contains(self, location):
        for coords in self.coordinates:
            if coords == location:
                return True
        return False

    def destroyed(self):
        for coords in self.coordinates:
            if board_display[coords["строка"]][coords["столбец"]] == "O":
                return False
            elif board_display[coords["строка"]][coords["столбец"]] == "*":
                raise RuntimeError("Поле отображается некорректно.")
        return True

row_size = 9
col_size = 9
num_ships = 5
max_ship_size = 5
min_ship_size = 1
num_turns = 40

ship_list = []

board = [[0] * col_size for x in range(row_size)]
board_display = [["O"] * col_size for x in range(row_size)]

def print_board(board_array):
    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
    for r in range(row_size):
        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
    print()


def search_locations(size, orientation):
    locations = []

    if orientation != "по горизонтали" and orientation != "по вертикали":
        raise ValueError('Значение должно быть "по горизонтали" или "по вертикали".')

    if orientation == "по горизонтали":
        if size <= col_size:
            for r in range(row_size):
                for c in range(col_size - size + 1):
                    if 1 not in board[r][c:c + size]:
                        locations.append({"строка": r, "столбец": c})
    elif orientation == "по вертикали":
        if size <= row_size:
            for c in range(col_size):
                for r in range(row_size - size + 1):
                    if 1 not in [board[i][c] for i in range(r, r + size)]:
                        locations.append({"строка": r, "столбец": c})

    if not locations:
        return "пусто"
    else:
        return locations


def random_location():
    size = randint(min_ship_size, max_ship_size)
    orientation = "по горизонтали" if randint(0, 1) == 0 else "по вертикали"

    locations = search_locations(size, orientation)
    if locations == "пусто":
        return "пусто"
    else:
        return {"расположение": locations[randint(0, len(locations) - 1)], "размер": size,
                "ориентация": orientation}


def get_row():
    while True:
        try:
            guess = int(input("Отгадайте строку: "))
            if guess in range(1, row_size + 1):
                return guess - 1
            else:
                print("\nВы вышли за пределы поля.")
        except ValueError:
            print("\nВведите цифру. ")


def get_col():
    while True:
        try:
            guess = int(input("Отгадайте столбец: "))
            if guess in range(1, col_size + 1):
                return guess - 1
            else:
                print("\nВы вышли за пределы поля.")
        except ValueError:
            print("\nВведите цифру. ")


temp = 0
while temp < num_ships:
    ship_info = random_location()
    if ship_info == "Пусто":
        continue
    else:
        ship_list.append(Ship(ship_info["размер"], ship_info["ориентация"], ship_info["расположение"]))
        temp += 1
del temp


os.system("cls")
print_board(board_display)

for turn in range(num_turns):
    print("Ваш ход:", turn + 1, "из", num_turns)
    print("Осталось кораблей:", len(ship_list))
    print()

    guess_coords = {}
    while True:
        guess_coords["строка"] = get_row()
        guess_coords["столбец"] = get_col()
        if board_display[guess_coords["строка"]][guess_coords["столбец"]] == "X" or board_display[guess_coords["строка"]][guess_coords["столбец"]] == "*":
            print("\nВы уже стреляли в это место.")
        else:
            break

    os.system("cls")

    ship_hit = False
    for ship in ship_list:
        if ship.contains(guess_coords):
            print("Попадание!")
            ship_hit = True
            board_display[guess_coords["строка"]][guess_coords["столбец"]] = "X"
            if ship.destroyed():
                print("Корабль уничтожен!")
                ship_list.remove(ship)
            break
    if not ship_hit:
        board_display[guess_coords["строка"]][guess_coords["столбец"]] = "*"
        print("Мимо!")

    print_board(board_display)

    if not ship_list:
        break


if ship_list:
    print("Вы проиграли!")
else:
    print("Все корабли затоплены. Вы выиграли!")
