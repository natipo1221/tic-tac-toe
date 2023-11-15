import tkinter as tk
import random
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        global able
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.configure(bg="#F5F5DC")
        self.current_player = "X"
        self.board = ["", "", "", "", "", "", "", "", ""]
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, fg="black", text="", font=("Helvetica", 24), width=10, height=4,
                               command=lambda i=i: self.play(i), bg="#F5F5DC")
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        restart_button = tk.Button(self.master, text="משחק חדש", font=("Helvetica", 16), width=12, command=self.restart)
        restart_button.grid(row=3, column=0, columnspan=3, pady=10)

    def play(self, position):
        if self.board[position] != "":
            return
        self.board[position] = self.current_player
        self.buttons[position].configure(text=self.current_player)

        winner = self.check_winner()
        if winner:
            messagebox.showinfo("ניצחון!", f"{winner} המנצח הוא ")
            self.restart()
            return

        if "" not in self.board:
            messagebox.showinfo("Tie", "The game is a tie!")
            self.restart()
            return

        self.current_player = "O" if self.current_player == "X" else "X"


    def computer(self):
        choice = random.randint(0, 8)
        while self.board[choice] == "":
            choice = random.randint(0, 8)
    def check_winner(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != "":
                self.buttons[i].configure(text=self.board[i], fg="green")
                self.buttons[i + 1].configure(text=self.board[i], fg="green")
                self.buttons[i + 2].configure(text=self.board[i], fg="green")
                return self.board[i]

        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                self.buttons[i].configure(text=self.board[i], fg="green")
                self.buttons[i + 3].configure(text=self.board[i], fg="green")
                self.buttons[i + 6].configure(text=self.board[i], fg="green")
                return self.board[i]

        if self.board[0] == self.board[4] == self.board[8] != "":
            self.buttons[0].configure(text=self.board[0], fg="green")
            self.buttons[4].configure(text=self.board[4], fg="green")
            self.buttons[8].configure(text=self.board[8], fg="green")
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != "":
            self.buttons[2].configure(text=self.board[2], fg="green")
            self.buttons[4].configure(text=self.board[4], fg="green")
            self.buttons[6].configure(text=self.board[6], fg="green")
            return self.board[2]

        return None

    def restart(self):
        self.current_player = "X"
        self.board = ["", "", "", "", "", "", "", "", ""]
        for button in self.buttons:
            button.configure(text="", fg="black")


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
