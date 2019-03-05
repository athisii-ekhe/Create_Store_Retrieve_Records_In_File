class Node:
    """
    Objective: To create a Node object which has three attributes data, left, right.
    """
    def __init__(self, data):
        """
        Objective: To initialise the object of class Node.
        Input Parameters:
                   self: Implicit object of class Node.
                   data: Value of the node object.
        """
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    Objective: To represent the Binary Search Tree data structure.
    """
    def __init__(self):
        """
        Objective: To initialise the object of class BST.
        Input Parameters:
                    self: Implicit object of class BST.

        """
        self.root = None

    def __str__(self):
        """
        Objective: To print the object of class BST.
        Input Parameters:
                    self: Implicit object of class BST.

        """
        return self.insert_wrapper()

    def insert_wrapper(self):
        """
        Objective: To call traverse method.
        Input Parameters:
                    self: Implicit object of class BST.

        """
        return self.traverse(self.root)

    def count_wrapper(self):
        """
        Objective: To call count method.
        Input Parameters:
                    self: Implicit object of class BST.

        """
        return self.count_node(self.root)

    def insert_node(self, data):
        """
        Objective: To insert node in BST data structure.
        Input Parameters:
                    self: Implicit object of class BST.
                    data: Value to be pass to the object of class Node.
        """
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            cur_node = self.root
            done = False
            while done is not True:
                if cur_node.data < new_node.data:
                    if cur_node.right is None:
                        cur_node.right = new_node
                        done = True
                    else:
                        cur_node = cur_node.right
                elif cur_node.data > new_node.data:
                    if cur_node.left is None:
                        cur_node.left = new_node
                        done = True
                    else:
                        cur_node = cur_node.left
                else:
                    print("Same value already exist!")
                    break

    def traverse(self, cur_node=None, string=''):
        """
        Objective: To traverse the nodes of BST data structure.
        Input Parameters:
                self: Implicit object of class BST.
                cur_node: Current node.
                string: string of nodes.
        """
        if cur_node.left is not None:
            string = self.traverse(cur_node.left, string)
        string += str(cur_node.data) + " "
        if cur_node.right is not None:
            string = self.traverse(cur_node.right, string)
        return string

    def count_node(self,current):
        """
        Objective: To count the number of nodes in BST data structure.
        """
        if current is None:
            return 0
        return self.count_node(current.left)+ 1 + self.count_node(current.right)


def main():
    bst = BST()
    bst.insert_node(5)
    bst.insert_node(3)
    bst.insert_node(7)
    bst.insert_node(2)
    bst.insert_node(4)
    bst.insert_node(6)
    bst.insert_node(8)

    print(bst)
    print(bst.count_wrapper())


if __name__ == '__main__':
    main()

