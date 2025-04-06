import tkinter as tk
from tkinter import messagebox

# Questions and options
questions = [
    'What is the capital of India?',
    'How many faces does a cube have?',
    'When did partition of Bengal take place?'
]

options = [
    ['Delhi', 'Mumbai', 'Kolkata', 'Chennai'],
    ['8', '12', '4', '6'],
    ['1940', '1857', '1905', '1947']
]

answers = ['Delhi', '6', '1905']

class QuizGame:
    def __init__(self, root):  # Fixed constructor
        self.root = root
        self.root.title("Quiz Game")
        self.q_index = 0
        self.score = 0
        self.name = ""

        self.name_label = tk.Label(root, text="Hello! Please enter your name:")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        self.name = self.name_entry.get()
        if not self.name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return

        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        self.show_question()

    def show_question(self):
        if self.q_index < len(questions):
            self.clear_screen()
            self.question_label = tk.Label(self.root, text=questions[self.q_index], font=("Arial", 14))
            self.question_label.pack(pady=10)

            self.option_buttons = []
            for option in options[self.q_index]:
                btn = tk.Button(self.root, text=option, width=20, command=lambda opt=option: self.check_answer(opt))
                btn.pack(pady=5)
                self.option_buttons.append(btn)

            self.quit_button = tk.Button(self.root, text="I quit", command=self.quit_game)
            self.quit_button.pack(pady=10)
        else:
            self.end_game()

    def check_answer(self, selected):
        correct_answer = answers[self.q_index]

        if selected == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", f"Congrats, {self.name}, your answer is right! You win {self.score * 10}L")
            self.q_index += 1
            self.show_question()
        else:
            messagebox.showinfo("Wrong", "Unfortunately, your answer is wrong. You take home nothing.")
            self.end_game()

    def quit_game(self):
        messagebox.showinfo("Quit", f"Okay {self.name}, your winnings are: {self.score * 10}L")
        self.end_game()

    def end_game(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Thanks for playing, {self.name}!", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=f"You won: {self.score * 10}L", font=("Arial", 12)).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Create and run the app
root = tk.Tk()
root.geometry("400x300")
app = QuizGame(root)
root.mainloop()

