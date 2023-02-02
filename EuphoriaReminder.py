# import win10toast 
from win10toast import ToastNotifier
import random
import time

MessageList = [
"You are enough.",
"You can be proud of who you are.",
"You are more than worthy of love.",
"You don't have to compare yourself to others.",
"You get better every day.",
"You are worthy of all things wonderful.",
"Your body deserves to be taken care of.",
"You are so beautiful, inside and out.",
"You're not weak when I ask for help.",
"Your true friends love and support You.",
"You deserve good things.",
"Only you can decide who you are.",
"You can reach your goals if you keep at them.",
"You're am not alone in your journey.",
"You belong just as much as everyone else.",
"You are valid and valued.",
"You are beautifull",
"WOW you're actually kinda cute",
"Time for water!",
]


while (True):
    # random item from list
    Message=(random.choice(MessageList))

    # create an object to ToastNotifier class
    n = ToastNotifier()
    n.show_toast(Message, "<3", duration = 5,
    icon_path ="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")
    time.sleep(300)
