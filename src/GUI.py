from tkinter import *
from tkinter import ttk

def welcome():
    welcome_label = ttk.Label(
        frm,
        text="Welcome to the fraud detection tool!",
        font=("Times New Roman", 25)
    )

    view_results_label = ttk.Label(
        frm,
        text="View results",
        font=("Times New Roman", 16)
    )

    view_results_button = ttk.Button(
        frm,
        text="View results",
        command=view_results,
    )

    train_a_model_label = ttk.Label(
        frm,
        text="Train model",
        font=("Times New Roman", 16)
    )

    train_a_model_button = ttk.Button(
        frm,
        text="Train model",
        command=train_a_model,
    )

    welcome_label.place(relx=0.5, rely=0.1, anchor="center")

    view_results_label.place(relx=0.21, rely=0.2, anchor="w")
    view_results_button.place(relx=0.50, rely=0.2, anchor="w")

    train_a_model_label.place(relx=0.21, rely=0.3, anchor="w")
    train_a_model_button.place(relx=0.50, rely=0.3, anchor="w")

def view_results():
    print("hi")

def train_a_model():
    print("hello")

root = Tk()
root.geometry("800x600")
root.title("Fraud detection")

frm = ttk.Frame(root)
frm.place(relwidth=1, relheight=1)

welcome()

root.mainloop()