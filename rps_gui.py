# file: rps_gui.py

import tkinter as tk
from rps_backend import get_computer_choice, determine_winner

user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score

    computer = get_computer_choice()
    result = determine_winner(user_choice, computer)

    if result == "User":
        user_score += 1
        result_text = "You Win!"
    elif result == "Computer":
        comp_score += 1
        result_text = "You Lose!"
    else:
        result_text = "It's a Tie!"

    result_label.config(
        text=f"You: {user_choice} | Computer: {computer}\n{result_text}"
    )
    score_label.config(
        text=f"Score → You: {user_score} | Computer: {comp_score}"
    )

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose:").pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", pady=10)
result_label.pack()

score_label = tk.Label(root, text="Score → You: 0 | Computer: 0")
score_label.pack()

root.mainloop()
