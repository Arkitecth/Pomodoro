import time
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel()
    canvas.itemconfig(timer_text, text="0:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If its the 1st/3rd/5th/7th rep
    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work")
    # If its the 8th rep
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # if its the 2nd/4th/6th rep:
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in work_session:
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN,
                    highlightthickness=0, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
tomato_img = canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Buttons
start_button = Button(text="Start", highlightthickness=0,
                      bg=YELLOW, highlightbackground=YELLOW, fg="black", command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0,
                      bg=YELLOW, highlightbackground=YELLOW, fg="black", command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmark
check_marks = Label(text="", highlightthickness=0, bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()
