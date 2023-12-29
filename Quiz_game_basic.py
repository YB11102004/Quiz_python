from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import math
import pandas as pd
import random
final_score=0
mat=pd.read_excel("Quiz_Ques.xlsx")
shuffled_index = list(range(len(mat)))
random.shuffle(shuffled_index)
def select_random_question():
    global shuffled_index
    if not shuffled_index:
        shuffled_index = list(range(len(mat)))
        random.shuffle(shuffled_index)
    random_index = shuffled_index.pop()
    random_question = mat.iloc[random_index]
    return random_question
def quizoptions():
    root = Tk()
    root.title('Quiz game')
    root.state('zoomed')
    root.configure(bg='#0187A8')
    question=select_random_question()
    var=question[5]
    oplabel = Label(root, text=question[0], font=("Comic Sans MS", 30,"bold"),bg='#0187A8',anchor="center")
    oplabel.grid(row=0, column=0, columnspan=4, padx=20, pady=10)
    selected_radio = IntVar()
    radio_font = ("Comic Sans MS", 18)
    radio_bg='#0187A8'
    radio_options = [question[1], question[2], question[3], question[4]]
    for i in range(4):
        radio = Radiobutton(root, text=f"{chr(65+i)}) {radio_options[i]}", variable=selected_radio, value=i+1, font=radio_font, bg=radio_bg)
        radio.grid(row=1, column=i, padx=(20, 5), pady=5)
    def on_submit():
        global final_score
        correct_answer = var
        user_answer = selected_radio.get()
        if user_answer == correct_answer:
            final_score += 1
            messagebox.showinfo("Feedback", "Correct! Well done!")
        else:
            messagebox.showinfo("Feedback", f"Sorry, the correct answer is {chr(64 + correct_answer)}. Better luck next time.")

        if selected_radio.get() == 0:
            messagebox.showwarning("Warning", "Please select an option before submitting.")
        else:
            root.destroy()
    submit_button = Button(root, text="S U B M I T", command=on_submit, width=10, height=2,bg='#FF0080',font=("Comic Sans MS", 14,"bold"),relief=SOLID,justify=CENTER)
    submit_button.grid(row=2, column=0, columnspan=4, pady=10)
    mainloop()
    return selected_radio.get()

for i in range(3):
    n=quizoptions()

def create_window(final_score):
    extra=Tk()
    extra.title('Final Score')
    extra.state('zoomed')
    extra.configure(background='#0187A8')
    label=Label(extra,text=f'The final score is: {final_score}\nThe Percentage of correct answer is: \n {math.trunc((final_score/3)*100)} %',font=("Comic Sans MS", 30,"bold"))
    label.configure(background='#0187A8')
    label.pack()
    quit_button = Button(extra, text="Q U I T", command=extra.destroy, width=10, height=2,bg='#FF0080',font=("Comic Sans MS", 14,"bold"),relief=SOLID,justify=CENTER)
    quit_button.pack()
    mainloop()

create_window(final_score)