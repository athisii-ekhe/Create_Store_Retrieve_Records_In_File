# Non-recursive method.
def binary_search(lst, key):
    """
    Objective: To search an element from the list.
    Input Parameter:
                lst: List of element.
    			key: Element to be searched.
    Return: -1
    """
    start = 0
    end = len(lst)-1
    while start <= end:
        mid = (start + end)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    x = 5
    result = binary_search(array, x)
    print(array, "\nSearching value: ", x)
    if result != -1:
        print("Element found at index: ", result)
    else:
        print("Element not found!")


# RECURSIVE APPROACH
'''
def binary_search(lst, start, end, key):
    """
    Objective: To search an element from the list.
    Input Parameter:
             lst: List of element.
	         start: Lowest index of list.
             end: Last index of list.
	         key: Element to be searched.
    Return: -1
    """
    while start <= end:
        mid = (start + end)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            return binary_search(lst, mid + 1, end, key)
        else:
            return binary_search(lst, start, mid - 1, key)
    return -1
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 10
    result = binary_search(array, 0, len(array) - 1,  x)
    print(array, "\nSearching value: ", x)
    if result != -1:
        print("Element found at index: ", result)
    else:
        print("Element not found!")
'''

