import random
import tkinter as tk
from tkinter import messagebox

# Create the game board
board = [[' ' for _ in range(7)] for _ in range(6)]

# Function to check for a winning move
def check_win(symbol):
    # Check rows
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == symbol:
                return True

    # Check columns
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == symbol:
                return True

    # Check diagonals (positive slope)
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == symbol:
                return True

    # Check diagonals (negative slope)
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == symbol:
                return True

    return False

# Function for two players to play the game
def play_two_player_game():
    player1 = 'X'
    player2 = 'O'
    current_player = player1

    messagebox.showinfo("Connect Four", "Welcome to Connect Four (Two-Player Mode)!")

    def on_button_click(column):
        nonlocal current_player

        if all(cell != ' ' for cell in board[0]):
            messagebox.showinfo("Connect Four", "It's a tie!")
            reset_game()
            return

        for row in range(5, -1, -1):
            if board[row][column] == ' ':
                board[row][column] = current_player
                button = buttons[row][column]
                button.config(text=current_player, bg='yellow' if current_player == player1 else 'red')

                if check_win(current_player):
                    messagebox.showinfo("Connect Four", f"Player {current_player} wins!")
                    reset_game()
                    return

                current_player = player2 if current_player == player1 else player1
                break

    def reset_game():
        nonlocal current_player

        for row in range(6):
            for col in range(7):
                board[row][col] = ' '
                button = buttons[row][col]
                button.config(text=' ', bg='white')

        current_player = player1

    # Create the GUI
    window = tk.Tk()
    window.title("Connect Four")
    window.config(bg='blue')  # Set window background color
    buttons = []

    for row in range(6):
        row_buttons = []
        for col in range(7):
            button = tk.Button(window, text=' ', width=7, height=3,
                               command=lambda col=col: on_button_click(col), bg='blue')
            button.grid(row=row, column=col)
            row_buttons.append(button)
        buttons.append(row_buttons)

    window.mainloop()

# Function for playing against the AI
def play_ai_game():
    player = 'X'
    ai = 'O'
    current_player = player

    messagebox.showinfo("Connect Four", "Welcome to Connect Four (AI Mode)!")

    def on_button_click(column):
        nonlocal current_player

        if all(cell != ' ' for cell in board[0]):
            messagebox.showinfo("Connect Four", "It's a tie!")
            reset_game()
            return

        for row in range(5, -1, -1):
            if board[row][column] == ' ':
                board[row][column] = current_player
                button = buttons[row][column]
                button.config(text=current_player, bg='yellow' if current_player == player else 'red')

                if check_win(current_player):
                    messagebox.showinfo("Connect Four", f"Player {current_player} wins!")
                    reset_game()
                    return

                current_player = player if current_player == ai else ai
                if current_player == ai:
                    ai_move()
                break

    def reset_game():
        nonlocal current_player

        for row in range(6):
            for col in range(7):
                board[row][col] = ' '
                button = buttons[row][col]
                button.config(text=' ', bg='blue')

        current_player = player

    def ai_move():
        if all(cell != ' ' for cell in board[0]):
            return

        available_columns = [col for col in range(7) if board[0][col] == ' ']
        col = random.randint(0, len(available_columns) - 1)
        selected_column = available_columns[col]
        on_button_click(selected_column)

    # Create the GUI
    window = tk.Tk()
    window.title("Connect Four")
    window.config(bg='blue')  # Set window background color
    buttons = []

    for row in range(6):
        row_buttons = []
        for col in range(7):
            button = tk.Button(window, text=' ', width=7, height=3,
                               command=lambda col=col: on_button_click(col), bg='blue')
            button.grid(row=row, column=col)
            row_buttons.append(button)
        buttons.append(row_buttons)

    window.mainloop()

# Function to choose game mode
def choose_game_mode():
    window = tk.Tk()
    window.title("Connect Four")
    window.geometry("300x150")
    window.config(bg='blue')  # Set window background color

    label = tk.Label(window, text="Choose game mode:", bg='blue')
    label.pack(pady=10)

    def on_mode_selected(mode):
        window.destroy()
        if mode == 1:
            play_two_player_game()
        elif mode == 2:
            play_ai_game()

    btn_two_player = tk.Button(window, text="Two-Player Mode", command=lambda: on_mode_selected(1), bg='white')
    btn_two_player.pack()

    btn_ai = tk.Button(window, text="AI Mode", command=lambda: on_mode_selected(2), bg='white')
    btn_ai.pack()

    window.mainloop()

# Start the game
choose_game_mode()
