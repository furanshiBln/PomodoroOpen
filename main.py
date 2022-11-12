from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#9C0F48"
RED = "#470D21"
GREEN = "#D67D3E"
YELLOW = "#F9E4D4"
FONT_NAME = "Arial"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    window.after_cancel(timer)
    title_label.config(text="Timer!", fg=GREEN)
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global reps
    reps += 1

    working_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="shivers from head to-ma-toes\n take a break", bg=YELLOW, fg=RED, font=(FONT_NAME, 14,
                                                                                                  "bold"))
    # if rep 2,4,6:
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="tomato, tomaaahto\n take a break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 14, "bold"))
    # if rep 1,3,5,7:
    else:
        count_down(working_seconds)
        title_label.config(text="to the tomatoes!", bg=YELLOW,fg=GREEN, font=(FONT_NAME, 14, "bold"))
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_minute = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds <10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_pomodoro()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += " ✅ "
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)


#canvas background image and text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img =PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

#Headline
title_label = Label(text="Timer!", bg=YELLOW, font=(FONT_NAME, 20, "bold"))
title_label.config(fg=GREEN, padx=10, pady=40)
title_label.grid(column=1, row=0)

#Start Button
start_button = Button(text="s t a r t", command=start_pomodoro, font=(FONT_NAME,10, "bold"))
start_button.grid(column=0, row=2)
start_button.config(padx=10, pady=10)

#Reset Button
reset_button = Button(text="r e s e t", command=reset_pomodoro, font=(FONT_NAME,10, "bold"))
reset_button.grid(column=2, row=2)
reset_button.config(padx=10, pady=10)

#checkmark Box

checkmark = Label(bg=YELLOW, highlightthickness=0,fg=GREEN,font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=3)
checkmark.config(padx=10, pady=10)





window.mainloop()
