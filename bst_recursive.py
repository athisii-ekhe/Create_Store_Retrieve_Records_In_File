class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is not None:
            return self.display_all_nodes()
        else:
            return "None"

    def display_all_nodes(self):
        return self._display_all_nodes(self.root)

    def _display_all_nodes(self, cur_node, nodes=''):
        if cur_node.left is not None:
            nodes = self._display_all_nodes(cur_node.left, nodes)
        nodes += str(cur_node.data) + " "
        if cur_node.right is not None:
            nodes = self._display_all_nodes(cur_node.right, nodes)
        return nodes

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def count_nodes(self):
        if self.root is not None:
            return self._count_nodes(self.root)
        else:
            return 0

    def _count_nodes(self, cur_node):
        if cur_node is None:
            return 0
        return self._count_nodes(cur_node.left) + 1 + self._count_nodes(cur_node.right)

    def search(self, value):
        if self.root is not None:
            return self._search(self.root, value)
        else:
            return False

    def _search(self, cur_node, value):
        if cur_node is not None:
            if value == cur_node.data:
                return True
        elif value < cur_node.data:
            return self._search(cur_node.left, value)
        elif value > cur_node.data:
            return self._search(cur_node.right, value)
        return False

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            return self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                return self._insert(value, cur_node.left)
        elif value > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                return self._insert(value, cur_node.right)
        else:
            print("Value already in tree!")


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    print(bst)
    print(bst.height())
    print(bst.count_nodes())
    print(bst.search(2))
    print(bst.search(6))
