import tkinter as tk 
import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
]
def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)
root = tk.Tk()
root.title("Steve Jobs Quotes")
root.geometry("400x200")
quote_label = tk.Label(root, text="", wraplength=350, justify="center")
quote_label.pack(pady=20)
show_quote_button = tk.Button(root, text="Show Quote", command=show_quote)
show_quote_button.pack(pady=10)     
root.mainloop()

