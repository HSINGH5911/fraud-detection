from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
from queue import Queue
from threading import Thread
import traceback

from App import run_training


CLEANED_RESULTS_PATH = Path("cleaned_results.txt")
training_queue = Queue()

def welcome():
    global train_a_model_button, status_label

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

    status_label = ttk.Label(
        frm,
        text="Ready.",
        font=("Times New Roman", 12)
    )

    welcome_label.place(relx=0.5, rely=0.1, anchor="center")

    view_results_label.place(relx=0.21, rely=0.2, anchor="w")
    view_results_button.place(relx=0.50, rely=0.2, anchor="w")

    train_a_model_label.place(relx=0.21, rely=0.3, anchor="w")
    train_a_model_button.place(relx=0.50, rely=0.3, anchor="w")

    status_label.place(relx=0.21, rely=0.4, anchor="w")


def view_results():
    if not CLEANED_RESULTS_PATH.exists():
        messagebox.showerror(
            "Results not found",
            f"Could not find {CLEANED_RESULTS_PATH}. Train a model first."
        )
        return

    results_window = Toplevel(root)
    results_window.geometry("900x600")
    results_window.title("Cleaned Results")

    results_frame = ttk.Frame(results_window, padding=10)
    results_frame.pack(fill=BOTH, expand=True)

    scrollbar = ttk.Scrollbar(results_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    results_text = Text(
        results_frame,
        wrap=WORD,
        yscrollcommand=scrollbar.set,
        font=("Consolas", 10)
    )
    results_text.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=results_text.yview)

    results = CLEANED_RESULTS_PATH.read_text(encoding="utf-8")
    results_text.insert("1.0", results)
    results_text.config(state=DISABLED)


def set_status(message):
    status_label.config(text=message or "Working...")


def train_a_model():
    train_a_model_button.config(state=DISABLED)
    set_status("Starting training...")
    root.after(100, check_training_queue)

    def update_status(message):
        training_queue.put(("status", message))

    def worker():
        try:
            cleaned_results_path = run_training(update_status)
        except Exception as error:
            traceback.print_exc()
            training_queue.put(("error", error))
        else:
            training_queue.put(("done", cleaned_results_path))

    Thread(target=worker, daemon=True).start()


def check_training_queue():
    while not training_queue.empty():
        message_type, payload = training_queue.get()

        if message_type == "status":
            set_status(payload)
        elif message_type == "done":
            training_finished(payload)
            return
        elif message_type == "error":
            training_failed(payload)
            return

    if str(train_a_model_button["state"]) == DISABLED:
        root.after(100, check_training_queue)


def training_finished(cleaned_results_path):
    train_a_model_button.config(state=NORMAL)
    set_status(f"Training complete. Saved cleaned results to {cleaned_results_path}.")
    messagebox.showinfo("Training complete", "Model trained and results saved.")


def training_failed(error):
    train_a_model_button.config(state=NORMAL)
    set_status("Training failed.")
    messagebox.showerror("Training failed", str(error))


root = Tk()
root.geometry("800x600")
root.title("Fraud detection")

frm = ttk.Frame(root)
frm.place(relwidth=1, relheight=1)

welcome()

root.mainloop()
