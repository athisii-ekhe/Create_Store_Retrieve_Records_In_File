# Merge Sort
def merge_sort(lst):
    """
    Objective: To sort the  given unsorted list.
    Input Parameter:
                lst: Unsorted list.
    Return: None
    """
    if len(lst) > 1:
        mid = len(lst) // 2
        left_lst = lst[:mid]
        right_lst = lst[mid:]
        merge_sort(left_lst)
        merge_sort(right_lst)
        merge(lst, left_lst, right_lst)


def merge(lst, lst1, lst2):
    """
    Objective: To merge the  given unsorted list.
    Input Parameter:
                lst: Final sorted list.
               lst1: First Sorted List.
               lst2: Second sorted list.
    Return: None
    """
    i = j = k = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst[k] = lst1[i]
            i += 1
        else:
            lst[k] = lst2[j]
            j += 1
        k += 1
    while i < len(lst1):
        lst[k] = lst1[i]
        i += 1
        k += 1
    while j < len(lst2):
        lst[k] = lst2[j]
        j += 1
        k += 1


def print_list(lst):
    """
    Objective: To print the elements of list.
    Input Parameter:
            lst: list of element.
    Return: None
    """
    for el in lst:
        print(el, end=" ")


if __name__ == '__main__':
    lst_array = [8, 4, 1, 6, 2, 5, 7, 3]
    print("Given list: ", end='')
    print_list(lst_array)
    merge_sort(lst_array)
    print("\nSorted list: ", end='')
    print_list(lst_array)
