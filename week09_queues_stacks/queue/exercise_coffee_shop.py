# Either of these implementations will work the same.
# Comment out one or the other.
# from queue_linked_list import Queue
from queue_python_list import Queue


coffee_queue = Queue()

while True:
    to_do = input("What do you want to do?\n")
    if to_do == "order":
        user_info = input("Enter your name: ")
        coffee_queue.enqueue(user_info)

    elif to_do == "collect":
        if coffee_queue.is_empty():
            print("No more orders coming")
        else:
            print("Coffee is ready for {}".format(coffee_queue.dequeue()))
    
    elif to_do == "check queue":
        for each in (coffee_queue.items):
            print(each)
    # TODO:
    # Write the coffee shop code here.
    # Prompt the user with "What do you want to do?"
    # User can input "order", "collect", or "check queue"
    # If the user says "order", prompt the user for their name and put
    # their name in the queue.
    # If the user says "collect", print
    # "Coffee is ready for " and the next customer's name in the queue.
    # If the queue is empty, print "No more orders coming"
    # If the user enters "check queue" print the queue.