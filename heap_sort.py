def heapify(lst, size, root):
    """
    Objective: To max heap a binary tree. i.e root node is greater than child nodes.
    Input Parameters:
            lst: List to be heapify.
            size: size of the list.
            root: Parent node.
    """
    largest = root
    left_node = 2 * root + 1
    right_node = 2 * root + 2
    if left_node < size and lst[left_node] > lst[root]:
        largest = left_node
    if right_node < size and lst[right_node] > lst[largest]:
        largest = right_node
    if largest != root:
        lst[root], lst[largest] = lst[largest], lst[root]
        heapify(lst, size, largest)


def heap_sort(lst):
    """
    Objective: To max heap a binary tree. i.e root node is greater than child nodes.
    Input Parameters:
            lst: List to be heapify.
    """
    length = len(lst)
    for i in range(length, -1, -1):
        heapify(lst, length, i)
    for i in range(length - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)


def print_list(lst):
    for el in lst:
        print(el, end=" ")


if __name__ == '__main__':
    lst = [3, 5, 7, 1, 6, 2, 4]
    print("Given list: ")
    print_list(lst)
    heap_sort(lst)
    print("\nSorted List: ")
    print_list(lst)
