from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ------------------ BUTTONS FUNCTIONALITY --------------- #
# ----------RIGHT BUTTON ------------#
def right():
    print('correct')


# ----------WRONG BUTTON-------------#
def wrong():
    print('incorrect')


# ------------------ UI -------------------- #
window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ------------- CARD FRONT and BACK --------- #
canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
canvas.create_image(450, 300, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# ------- BUTTONS ---------- #
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=right)
right_button.grid(column=1, row=1)

window.mainloop()
