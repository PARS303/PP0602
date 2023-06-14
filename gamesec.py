import tkinter as tk
from tkinter import messagebox

# Глобальные константы
SIZE = 7  # Размер игрового поля
CELL_SIZE = 50  # Размер ячейки
PLAYER_1_COLOR = "blue"
PLAYER_2_COLOR = "red"

# Создание игрового поля
def create_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    return board

# Проверка победителя
def check_winner(player):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == player:
                if i < SIZE - 3 and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                    return True
                if j < SIZE - 3 and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                    return True
                if i < SIZE - 3 and j < SIZE - 3 and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                    return True
                if i > 2 and j < SIZE - 3 and board[i-1][j+1] == player and board[i-2][j+2] == player and board[i-3][j+3] == player:
                    return True
    return False

# Ход игрока
def make_move(row, col):
    global player_turn
    if board[row][col] == 0:
        board[row][col] = player_turn
        if player_turn == 1:
            draw_token(row, col, PLAYER_1_COLOR)
            if check_winner(player_turn):
                show_winner(player_turn)
                return
            player_turn = 2
        else:
            draw_token(row, col, PLAYER_2_COLOR)
            if check_winner(player_turn):
                show_winner(player_turn)
                return
            player_turn = 1

# Отображение фишки игрока на поле
def draw_token(row, col, color):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2
    token_canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color)

# Показать победителя
def show_winner(player):
    if player == 1:
        winner = "игрок 1"
    else:
        winner = "игрок 2"
    messagebox.showinfo("Победа!", "Победил " + winner)
    reset_game()

# Сброс игры
def reset_game():
    global board, player_turn
    token_canvas.delete("all")
    board = create_board()
    player_turn = 1

# Показать правила
def show_rules():
    messagebox.showinfo("Правила игры", "Правила игры Hexagon:\n\nИграют два игрока, по очереди "
                                        "ставя фишки в свободные клетки поля. Побеждает "
                                        "игрок, который соберет 4 своих фишки в ряд "
                                        "(горизонтально, вертикально или по диагонали).")

# Создание окна
window = tk.Tk()
window.title("Hexagon")
window.resizable(False, False)  # Фиксированные границы окна

# Создание рамки игры
game_frame = tk.LabelFrame(window, text="Жоский Гексагон для настоящик Slave")
game_frame.pack(padx=10, pady=10)


# Создание холста для фишек игрового поля
token_canvas = tk.Canvas(game_frame, width=CELL_SIZE * SIZE, height=CELL_SIZE * SIZE)
token_canvas.pack()

# Создание кнопок
reset_button = tk.Button(window, text="Перезапустить", command=reset_game)
reset_button.pack()

rules_button = tk.Button(window, text="Правила", command=show_rules)
rules_button.pack()

quit_button = tk.Button(window, text="Выйти", command=window.quit)
quit_button.pack()

# Инициализация игрового поля и текущего игрока
board = create_board()
player_turn = 1

# Обработчик клика на поле
def click_handler(event):
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    make_move(row, col)

token_canvas.bind("<Button-1>", click_handler)

# Запуск игры
window.mainloop()
