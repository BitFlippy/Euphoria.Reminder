# import win10toast 
from win10toast import ToastNotifier
import random
import time



with open("MessageList.csv", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        # Process line and create table item
        print(lines)


while (True):
    # random item from list
    Message=(random.choice(lines))

    # create an object to ToastNotifier class
    n = ToastNotifier()
    n.show_toast(Message, "<3", duration = 10,
    icon_path ="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")
    time.sleep(300)
