import tkinter as tk
import random
import time
# ^^^^Imports the libraries required
# Class to Create whack a mole components, you can edit values to change the shape size colour even add images if you wish i negated these to simplify the code.
class WhackAMole:
    def __init__(self, root):
        self.root = root
        self.root.title("Whack-a-Mole Game")

        self.score = 0
        self.time_left = 30

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=('Ariel', 14))
        self.score_label.pack()

        self.time_label = tk.Label(self.root, text=f"Time left: {self.time_left}s", font=('Ariel', 14))
        self.time_label.pack()

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='lightgreen')
        self.canvas.pack()

        self.mole = self.canvas.create_oval(0, 0, 50, 50, fill='brown')

        self.root.bind("<Button-1>", self.hit_mole)

        self.move_mole()
        self.update_timer()
# Randomly position a mole around the window
    def move_mole(self):
        if self.time_left > 0:
            x = random.randint(0, 350)
            y = random.randint(0, 350)
            self.canvas.coords(self.mole, x, y, x+50, y+50)
            self.root.after(1000, self.move_mole)
# Binds mouse click and position
    def hit_mole(self, event):
        if self.time_left > 0:
            x1, y1, x2, y2 = self.canvas.coords(self.mole)
            if x1 < event.x < x2 and y1 < event.y < y2:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
# Creates a count down timer, values can be edited to extend or shorten the duration of the game
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()
# Displays Game Over screen
    def end_game(self):
        self.canvas.create_text(200, 200, text="Game Over", font=('Helvetica', 24), fill='red')
        self.root.unbind("<Button-1>")

if __name__ == "__main__":
    root = tk.Tk()
    game = WhackAMole(root)
    root.mainloop()
