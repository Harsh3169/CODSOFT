import tkinter as tk
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI")
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.create_ui()

    def create_ui(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.window, text=" ", font=("Arial", 20), width=5, height=2,
                                command=lambda row=i, col=j: self.player_move(row, col))
                btn.grid(row=i, column=j)
                self.buttons.append(btn)

        self.status_label = tk.Label(self.window, text="Your Turn", font=("Arial", 14))
        self.status_label.grid(row=3, columnspan=3)

        self.play_again_button = tk.Button(self.window, text="Play Again", font=("Arial", 14),
                                           command=self.reset_game, state="disabled")
        self.play_again_button.grid(row=4, columnspan=3)

    def player_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = "X"
            self.buttons[index].config(text="X", state="disabled")
            if self.check_winner():
                self.status_label.config(text="Player Wins!")
                self.disable_buttons()
                return
            if self.is_full():
                self.status_label.config(text="It's a Draw!")
                self.play_again_button.config(state="normal")
                return
            self.ai_move()

    def ai_move(self):
        empty_indices = [i for i, x in enumerate(self.board) if x == " "]
        if empty_indices:
            move = random.choice(empty_indices)
            self.board[move] = "O"
            self.buttons[move].config(text="O", state="disabled")
            if self.check_winner():
                self.status_label.config(text="AI Wins!")
                self.disable_buttons()

    def check_winner(self):
        winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for (x, y, z) in winning_combinations:
            if self.board[x] == self.board[y] == self.board[z] and self.board[x] != " ":
                self.play_again_button.config(state="normal")
                return True
        return False

    def is_full(self):
        return " " not in self.board

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")
        self.play_again_button.config(state="normal")

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for btn in self.buttons:
            btn.config(text=" ", state="normal")
        self.status_label.config(text="Your Turn")
        self.play_again_button.config(state="disabled")

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()