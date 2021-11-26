import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('data/french_words.csv')
df = pandas.DataFrame(data)
words_dict = df.to_dict(orient='records')

current_card = {}


# ------------------ BUTTONS FUNCTIONALITY --------------- #
def next_card():
    global current_card
    global card_flip_wait
    current_card = random.choice(words_dict)
    french_word = current_card['French']
    english_word = current_card['English']
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=french_word, fill='black')
    card_flip_wait = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')
    window.after_cancel(card_flip_wait)


# ------------------ UI -------------------- #
window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_flip_wait = None

canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(450, 300, image=card_front)
title_text = canvas.create_text(450, 150, text='', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(450, 300, text='', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# ------- BUTTONS ---------- #
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card, cursor='hand2')
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=next_card, cursor='hand2')
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
