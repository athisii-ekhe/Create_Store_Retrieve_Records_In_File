class Stack:
    """
    DESCRIPTION: To represent the Stack entity.
    """
    def __init__(self):
        """
        Objective: To initialize the object of class Stack.
        Input parameters:
                self: Implicit object of the class Stack.
        Return: None
        """
        self.lst = []
        self.top_of_stack = -1

    def __str__(self):
        """
        Objective: To return the elements of stack object.
        Input parameters:
                self: Implicit object of the class Stack.
        Return: Elements of stack object.
        """
        if self.is_empty():
            return 'Empty Stack!'
        for i in range(len(self.lst)-1, -1, -1):
            print(f'|| {self.lst[i]} ||')
        return ''

    def is_empty(self):
        """
        Objective: To check if stack object is empty.
        Input parameters:
                self: Implicit object of the class Stack.
        Return: True if stack is empty.
        """
        if self.top_of_stack == -1:
            return True

    def push_ele(self, ele):
        """
        Objective: To push an element to the stack object.
        Input parameters:
                self: Implicit object of the class Stack.
                ele: Element to be pushed.
        Return: None
        """
        self.lst.append(ele)
        self.top_of_stack += 1

    def pop_ele(self):
        """
        Objective: To pop an element from the stack object.
        Input parameters:
                self: Implicit object of the class Stack.

        Return: Element which was popped from the stack object.
        """
        if self.is_empty():
            return 'Stack is empty!'
        ele = self.lst.pop(self.top_of_stack)
        self.top_of_stack -= 1
        return f'You have popped: {ele}'


def main():
    stack = Stack()
    while True:
        print("==" * 13, "STACK MENU", "==" * 13)
        print("""\t\t1. Push an element to the stack.
        2. Pop an element from the stack.
        3. Print all the elements of stack.
        4. Exit""")
        print("==" * 32)
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            ele = int(input("Enter any integer number: "))
            stack.push_ele(ele)
        elif user_choice == '2':
            print(stack.pop_ele())
        elif user_choice == '3':
            print(stack)
        elif user_choice == '4':
            return
        else:
            print("Wrong choice! Try again...")


if __name__ == '__main__':
    main()








