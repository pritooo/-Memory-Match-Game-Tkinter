import tkinter as tk
import random
import time

# -----------------------------
# Memory Match Game (Concentration)
# -----------------------------

# Create main window
root = tk.Tk()
root.title("🧠 Memory Match Game")
root.geometry("400x450")
root.resizable(False, False)

# Game variables
buttons = []
first_card = None
second_card = None
flipped = 0
pairs = 8

# Generate pairs of emojis (or letters)
symbols = ['🍎', '🍌', '🍇', '🍓', '🍒', '🍉', '🥝', '🍋']
cards = symbols * 2
random.shuffle(cards)

# Label for messages
status_label = tk.Label(root, text="Find all matching pairs!", font=("Arial", 14))
status_label.pack(pady=10)

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Helper functions
def on_click(i):
    global first_card, second_card, flipped

    button = buttons[i]

    # Ignore clicks on already matched cards
    if not button["state"] == tk.NORMAL:
        return

    # Flip the card
    button.config(text=cards[i], state=tk.DISABLED, disabledforeground="black")

    if first_card is None:
        first_card = i
    elif second_card is None:
        second_card = i
        root.after(500, check_match)  # wait half second before checking

def check_match():
    global first_card, second_card, flipped

    if cards[first_card] == cards[second_card]:
        # Match found!
        buttons[first_card].config(bg="lightgreen")
        buttons[second_card].config(bg="lightgreen")
        flipped += 1
        status_label.config(text=f"Matched! Pairs found: {flipped}/{pairs}")
        if flipped == pairs:
            status_label.config(text="🎉 You matched all pairs! Great memory!")
    else:
        # Not a match — flip them back
        buttons[first_card].config(text="", state=tk.NORMAL)
        buttons[second_card].config(text="", state=tk.NORMAL)

    first_card = None
    second_card = None


# Create grid of buttons (4x4)
for i in range(16):
    b = tk.Button(frame, text="", width=6, height=3,
                  command=lambda i=i: on_click(i),
                  font=("Arial", 18), bg="lightblue")
    b.grid(row=i // 4, column=i % 4, padx=5, pady=5)
    buttons.append(b)

# Restart button
def restart_game():
    global cards, flipped, first_card, second_card
    random.shuffle(cards)
    flipped = 0
    first_card = None
    second_card = None
    status_label.config(text="Find all matching pairs!")
    for b in buttons:
        b.config(text="", bg="lightblue", state=tk.NORMAL)

tk.Button(root, text="🔄 Restart Game", font=("Arial", 12),
          command=restart_game).pack(pady=10)

# Run the game
root.mainloop()