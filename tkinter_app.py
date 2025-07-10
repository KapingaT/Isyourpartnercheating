import tkinter as tk
from tkinter import messagebox

# Backend Logic
class TheoryOne:
    def __init__(self, frequent_messages, current_messages):
        self.frequent_messages = frequent_messages
        self.current_messages = current_messages

    def model(self):
        if self.current_messages < self.frequent_messages:
            return "He might be cheating on you, but give him a chance."
        elif self.current_messages == self.frequent_messages:
            return "There is a 50/50 chance."
        else:
            return "He is definitely not cheating."

# GUI Frontend
def run_model():
    try:
        frequent = int(entry_frequent.get())
        current = int(entry_current.get())

        theory = TheoryOne(frequent, current)
        result = theory.model()
        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers only!")

# Main Window
root = tk.Tk()
root.title("Cheat Checker - TikTok Style")
root.geometry("400x300")
root.configure(bg="#121212")  # Black background

# Styling
LABEL_COLOR = "#ADD8E6"  # Light blue
TEXT_COLOR = "#FFFFFF"

title_label = tk.Label(root, text="Cheat Checker", font=("Arial", 20, "bold"), fg=LABEL_COLOR, bg="#121212")
title_label.pack(pady=10)

tk.Label(root, text="How often did they used to message you?", fg=TEXT_COLOR, bg="#121212").pack()
entry_frequent = tk.Entry(root, font=("Arial", 14))
entry_frequent.pack(pady=5)

tk.Label(root, text="How often do they message you now?", fg=TEXT_COLOR, bg="#121212").pack()
entry_current = tk.Entry(root, font=("Arial", 14))
entry_current.pack(pady=5)

check_button = tk.Button(root, text="Check Now", command=run_model, bg=LABEL_COLOR, fg="black", font=("Arial", 12, "bold"))
check_button.pack(pady=15)

result_label = tk.Label(root, text="", fg=LABEL_COLOR, bg="#121212", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
