class Node:
    """
    DESCRIPTION: To represent the Node entity.
    """

    def __init__(self, data):
        """
        Objective: To initialise the object of class Node.
        Input Parameters:
                    self: Implicit object of class Node.
                    data: Value to be assigned to the data of object.
                    next: It holds the address of the next object.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    DESCRIPTION: To represent the LinkedList.
    """

    def __init__(self):
        """
        Objective: To initialize the object of class LinkedList.
        Input Parameters:
                    self: Implicit object of class LinkedList.
        """
        self.head = None

    def __str__(self):
        """
        Objective: To print all the elements of the linked list
        Input Parameter:
            self: Implicit object of class LinkedList.
        """
        elements = ''
        total = 1
        if self.head is None:
            return "\t\tEmpty List!"
        else:
            current = self.head
            while current.next is not None:
                elements += f'|{current.data}|next|-->'
                current = current.next
                total += 1
            elements += f'|{current.data}|next|-->None'
            return f'\t\tTotal node(s): {total} \n\t\tNode(s) in Linked List are:\n\n\t\t{elements}'

    def add_node(self, data):
        """
        Objective: To add new node at the beginning of the linked list.
        Input Parameters:
                    self: Implicit object of class LinkedList
                    data: Value to be assigned to the object of class Node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append_node(self, data):
        """
        Objective: To append node at the end of the linked list.
        Input Parameter(s):
                    self: Implicit object of class LinkedList.
                    data: Value to be assigned to the object of class Node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_node(self):
        """
        Objective: To remove node from the beginning of the Linked List.
        Input Parameter:
                self: Implicit object of the class LinkedList.
        """
        if self.head is None:
            return '\t\tEmpty List!'
        else:
            current = self.head
            self.head = current.next
            return f'\t\tYou have removed: {current.data}'

    def delete_specific_node(self, data):
        flag = False
        if self.head is None:
            return '\t\tEmpty List! '
        elif self.head.data == data:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
            return f'\t\tYou have deleted: {data}'
        else:
            current_node = self.head
            while current_node.next is not None:
                last_node = current_node
                current_node = current_node.next
                if current_node.data == data:
                    current_node = current_node.next
                    last_node.next = current_node
                    flag = True
                    return f'\t\tYou have deleted: {data}'
            if flag is not True:
                if current_node.data == data:
                    return f'\t\tYou have removed: data'
                else:
                    return f'\t\tNode with value: {data} not found!'


def main():
    linkedlist = LinkedList()
    while True:
        print("\n\t", "==" * 20, "Linked List", "==" * 20)
        print("""\t\t1. Add new node at the beginning of linked list.
                2. Remove the first node of linked list.
                3. Remove a specific node from the linked list.
                4. Display all node(s) of the linked list.
                5. Exit """)
        print("\t", "==" * 20, "Linked List", "==" * 20)
        user_choice = input("\t\tEnter your choice: ")
        if user_choice == '1':
            data = int(input("\t\tEnter any integer number: "))
            linkedlist.add_node(data)
        elif user_choice == '2':
            print(linkedlist.remove_node())
        elif user_choice == '3':
            data = int(input("\t\tEnter the element to be deleted: "))
            print(linkedlist.delete_specific_node(data))
        elif user_choice == '4':
            print(linkedlist)
        elif user_choice == '5':
            break
        else:
            print("\t\tWrong Choice! Try again....")


if __name__ == '__main__':
    main()
