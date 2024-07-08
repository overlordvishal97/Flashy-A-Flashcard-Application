from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
words = {}
to_learn = {}
#-----------------------------function----------------------------#
# Read the Csv file and error management
try:
    df = pandas.read_csv(r"data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def random_word():
    global words, flip_timer
    window.after_cancel(flip_timer)
    words = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word,text=words["French"],fill="black")
    canvas.itemconfig(canvas_image,image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = "English",fill="white")
    canvas.itemconfig(card_word, text = words["English"],fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def is_known():
    to_learn.remove(words)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    random_word()
#-----------------------------UI setup----------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR,highlightthickness=0)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(height=526, width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR)

card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="", font=("Ariel",60,"italic"))
canvas.grid(row=0, column=1,columnspan = 2)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right,highlightthickness=0,command=is_known)
right_button.grid(column=2,row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong,highlightthickness=0,command=random_word)
wrong_button.grid(column=1,row=1)

random_word()



window.mainloop()