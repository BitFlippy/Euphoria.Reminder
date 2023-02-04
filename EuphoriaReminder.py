import tkinter
import random
import time
import requests
import csv
from win10toast import ToastNotifier

def show_notification(title, message, duration):
    toaster = ToastNotifier()
    return toaster.show_toast(
        title=title,
        msg=message,
        duration=duration,
        threaded=True
    )

def start_button_click():
    window.withdraw()
    interval = int(interval_slider.get() * 60)
    duration = int(duration_slider.get())
    notification_name = name_entry.get()
    while True:
        message = random.choice(messages)
        result = show_notification(notification_name, message, duration)
        if result:
            time.sleep(interval)
        else:
            break

window = tkinter.Tk()
window.title("Reminder")

name_label = tkinter.Label(text="Notification Name:")
name_label.pack()

name_entry = tkinter.Entry()
name_entry.pack()

interval_label = tkinter.Label(text="Interval (minutes):")
interval_label.pack()

interval_slider = tkinter.Scale(
    window,
    from_=1,
    to=60,
    orient="horizontal",
    length=200,
    resolution=1
)
interval_slider.pack()

duration_label = tkinter.Label(text="Duration (seconds):")
duration_label.pack()

duration_slider = tkinter.Scale(
    window,
    from_=10,
    to=20,
    orient="horizontal",
    length=200,
    resolution=1
)
duration_slider.pack()

start_button = tkinter.Button(window, text="Start", command=start_button_click)
start_button.pack()

response = requests.get("https://raw.githubusercontent.com/BitFlippy/Euphoria.Reminder/main/MessageList.csv")
messages = []
for line in csv.reader(response.text.splitlines()):
    messages.append(line[0])

window.mainloop()

