class Queue:
    """
    Objective: To represent the Queue entity.
    """

    def __init__(self):
        """
        Objective: To initialise the object of Queue class.
        Input Parameter:
                    self: Implicit object of class Queue.
        """
        self.queue = []
        self.front = -1
        self.rear = -1

    def __str__(self):
        """
        Objective: To return string of object of class Queue.
        Input Parameter:
                    self: Implicit object of class Queue.
        Return: Object of class Queue.
        """
        element = ''
        for ele in self.queue:
            element += str(ele) + " "
        return element

    def is_empty(self):
        """
        Objective: To check if queue is empty!
        Input Parameter:
                    self: Implicit object of class Queue.
        """
        if self.rear == -1 and self.front == -1 or (self.front == 0 and self.rear == -1):
            return True

    def peek(self):
        """
        Objective: To element of object of class Queue.
        Input Parameter:
                    self: Implicit object of class Queue.
        Return: The first element of queue.
        """
        if self.is_empty():
            return True
        return self.queue[self.front]

    def insert_data(self, data):
        """
        Objective: To add an element to the object of Queue.
        Input Parameter:
                    self: Implicit object of class Queue.
                    data: Element to be inserted.
        """
        if self.is_empty():
            self.front += 1
        self.queue.append(data)
        self.rear += 1

    def delete_data(self):
        """
        Objective: To remove an element of object of class Queue.
        Input Parameter:
                    self: Implicit object of class Queue.
        Return: Return the element which is removed.
        """
        if self.is_empty():
            return True
        ele = self.queue.pop(self.front)
        self.rear -= 1
        return ele

    def clear_queue(self):
        """
        Objective: To empty the element of object of class Queue.
        Input Parameter:
                    self: Implicit object of class Queue.
        """
        self.queue = []
        self.front = -1
        self.rear = -1


def main():
    """
    Objective: To perform queue operation.
        Input Parameter: None
    """
    queue_obj = Queue()
    while True:
        print("==" * 13, "QUEUE MENU", "==" * 13)
        print("""\t\t1. Insert an element to the queue.
        2. Delete an element from the queue.
        3. Print the first element of queue.
        4. Print all the elements of queue.
        5. Clear all the element of queue.
        6. Exit""")
        print("==" * 32)
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            data = int(input("Enter any integer number: "))
            queue_obj.insert_data(data)

        elif user_choice == '2':
            if queue_obj.is_empty():
                print("Queue is empty!")
                continue
            print(f'You have deleted: {queue_obj.delete_data()}')

        elif user_choice == '3':
            if queue_obj.is_empty():
                print("Queue is empty!")
                continue
            print(f'The first element in the Queue: {queue_obj.peek()}')

        elif user_choice == '4':
            if queue_obj.is_empty():
                print("Queue is empty!")
                continue
            print("Element(s) are: \n", queue_obj)

        elif user_choice == '5':
            choice = input("""Are you sure to clear the queue? Type:-
                1. Continue: Y
                2. Stop: N
                Enter your choice: """).lower()
            while choice != 'n' or choice != 'y':
                if choice == 'n':
                    break
                elif choice == 'y':
                    queue_obj.clear_queue()
                    print("Queue is emptied!")
                    break
                else:
                    choice = input("Enter only Y or N.\nEnter your choice: ").lower()
        elif user_choice == '6':
            print("Exiting....")
            return

        else:
            print("Invalid Choice! Try again...")


if __name__ == '__main__':
    main()
