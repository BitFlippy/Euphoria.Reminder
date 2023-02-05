import tkinter
import random
import time
import requests
import csv
from plyer import notification

# Variables to control appearance
border_radius = 20
bg_color = '#000000'
fg_color = '#FFFFFF'
button_color = '#5b5b5b'

def start_button_click():
    window.withdraw()
    interval = int(interval_slider.get() * 60)
    duration = int(duration_slider.get())
    notification_name = name_entry.get()
    while True:
        message = random.choice(messages)
        notification.notify(
            title=notification_name,
            message=message,
            app_name='<3',
            app_icon='icon.ico',
            timeout=duration
        )
        time.sleep(interval)

window = tkinter.Tk()
window.configure(bg=bg_color)

window.title("Reminder")
window.overrideredirect(1)
window.eval('tk::PlaceWindow . center')

name_label = tkinter.Label(text="Notification Label:", bg=bg_color, fg=fg_color)
name_label.pack()

name_entry = tkinter.Entry(bg=bg_color, fg=fg_color, bd=0, highlightthickness=0, highlightcolor=bg_color, highlightbackground=bg_color, relief='flat', font=("Helvetica", 12))
name_entry.config(highlightcolor=bg_color)
name_entry.insert(0,'Hey, friendly reminder^^')
name_entry.pack()

interval_label = tkinter.Label(text="Interval (minutes):", bg=bg_color, fg=fg_color)
interval_label.pack()

interval_slider = tkinter.Scale(
    window,
    from_=1,
    to=60,
    orient="horizontal",
    length=400,
    resolution=1,
    bg=bg_color,
    fg=fg_color,
    troughcolor=bg_color,
    activebackground=fg_color,
    sliderrelief='flat',
    highlightthickness=0,
)
interval_slider.pack()

duration_label = tkinter.Label(text="Duration (seconds):", bg=bg_color, fg=fg_color)
duration_label.pack()

duration_slider = tkinter.Scale(
    window,
    from_=5,
    to=20,
    orient="horizontal",
    length=400,
    resolution=1,
    bg=bg_color,
    fg=fg_color,
    troughcolor=bg_color,
    activebackground=fg_color,
    sliderrelief='flat',
    highlightthickness=0,
)
duration_slider.pack()

start_button = tkinter.Button(window, text="Start", command=start_button_click, bg='#000000', fg='#FFFFFF', bd=0, highlightthickness=0, relief='flat', activebackground='#FFFFFF', activeforeground='#000000')
start_button.pack()

response = requests.get("https://raw.githubusercontent.com/BitFlippy/Euphoria.Reminder/main/MessageList.csv")
messages = []
for line in csv.reader(response.text.splitlines()):
    messages.append(line[0])

window.mainloop()