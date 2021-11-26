import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv('data/to_learn.csv')

except:
    data = pandas.read_csv('data/french_words.csv')

df = pandas.DataFrame(data)
words_dict = df.to_dict(orient='records')

current_card = {}
need_to_learn = []


# ------------------ BUTTONS FUNCTIONALITY --------------- #
def next_card():
    global current_card, card_flip_wait
    window.after_cancel(card_flip_wait)
    if len(words_dict) == 0:
        canvas.itemconfig(title_text, text='')
        canvas.itemconfig(word_text, text='YOU\'VE COMPLETED THE SET OF FLASHCARDS.\nPLEASE EXIT OUT TO TRY AGAIN!',
                          font=('Arial', 20, 'normal'))
    else:
        current_card = random.choice(words_dict)
        french_word = current_card['French']
        current_card
        english_word = current_card['English']
        canvas.itemconfig(canvas_image, image=card_front)
        canvas.itemconfig(title_text, text='French', fill='black')
        canvas.itemconfig(word_text, text=french_word, fill='black')
        card_flip_wait = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


def is_known():
    words_dict.remove(current_card)
    new_data = pandas.DataFrame(words_dict)
    new_data.to_csv('data/to_learn.csv')
    next_card()


# ------------------ UI -------------------- #
window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
card_flip_wait = window.after(3000, flip_card)

canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(450, 300, image=card_front)
title_text = canvas.create_text(450, 150, text='', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(450, 300, text='', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# ------- BUTTONS ---------- #
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card,
                      cursor='hand2')
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=is_known, cursor='hand2')
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
