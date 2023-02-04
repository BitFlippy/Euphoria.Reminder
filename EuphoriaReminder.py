import random
import requests
import time
import win10toast

def get_random_message():
    response = requests.get("https://raw.githubusercontent.com/BitFlippy/Euphoria.Reminder/main/MessageList.csv")
    content = response.content.decode("utf-8")
    lines = content.split("\n")
    return random.choice(lines)


toaster = win10toast.ToastNotifier()

while True:
    message = get_random_message()
    toaster.show_toast("Cute Reminder", message, duration=7)
    time.sleep(5 * 60)