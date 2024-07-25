"""
This module contains selection sort functions for integer arrays
"""


def selection_sort(unsorted_array: list) -> list:
    n = len(unsorted_array)
    sorted_array = []

    while len(sorted_array) <= n:
        lowest_number = 10000000000
        m = len(unsorted_array)

        if m == 1:       
            sorted_array.append(unsorted_array[0])
        else:     
            for i in range(m - 1):
                if unsorted_array[i] < lowest_number:
                    lowest_number = unsorted_array[i] 

            sorted_array.append(lowest_number)
            sorted_array.remove(lowest_number)

    return sorted_array

if __name__ == '__main__':
    test_array1 = [5, 4, 100]

    print(test_array1)
    sorted_array = selection_sort(test_array1)
    print(sorted_array)