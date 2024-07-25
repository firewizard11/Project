"""
This module contains functions relating to bubble sort on integer arrays
"""


def swap(index1: int, index2: int, array: list) -> None:
    """This function swaps the element at index1 with index2 in the given array"""
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def bubble_sort(array: list) -> None:
    n = len(array)
    swapped = True

    while swapped == True:
        swapped = False
        
        for i in range(1, n):
            if array[i - 1] > array[i]:
                swap(i - 1, i, array)
                swapped = True

if __name__ == '__main__':
    test_array1 = [5, 4, 100, 31, 1, 17, 29, 11]
    test_array2 = [11, 2, 420, 5920, 900, 100000, 100, 99, 24, 50, 11, 42014810248, 12010]
    
    print(test_array1)
    bubble_sort(test_array1)
    print(test_array1)
    print(test_array2)
    bubble_sort(test_array2)
    print(test_array2)
    