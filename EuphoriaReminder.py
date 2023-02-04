import random
import requests
import time
import win10toast

def get_random_message():
    # Get the contents of the web source as a string
    response = requests.get("https://raw.githubusercontent.com/BitFlippy/Euphoria.Reminder/main/MessageList.csv")
    content = response.content.decode("utf-8")

    # Split the content into lines
    lines = content.split("\n")

    # Choose a random line and return it
    return random.choice(lines)

toaster = win10toast.ToastNotifier()

while True:
    # Get a random message and show it as a notification without an icon
    message = get_random_message()
    toaster.show_toast("Cute Reminder", message, duration=7)

    # Wait for 5 minutes
    time.sleep(5 * 60)
