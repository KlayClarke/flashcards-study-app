from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ------------------ UI -------------------- #
window = Tk()
window.title('Flashcards')

# ------------- CARD FRONT and BACK --------- #


# ------- BUTTONS ---------- #
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0)

window.mainloop()
