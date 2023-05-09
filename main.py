# Given an unsorted array, return the kth largest element. It is the kth largest element in sorted order, not the kth disticnt element
# Quick sort algorithm implemented using the last element as the pivot.
# [5, 3, 1, 6, 4, 2] k = 2 -> [1, 2, 3, 4, |5|, 6] kth = 5
# [ 2, 3, 1, 2, 4, 2] k = 4 -> [1, 2, |2|, 2, 3, 4] kth is the second 2
# [3] k = 1 so kth is 3

def quickSort(array, begin, end):
    # If within bounds
    if begin < end:
        # i and j both start at the beginning of the array
        i = begin
        j = begin
        # For loop that skips the very last item in the array or the pivot (That's why it' not end + 1)
        for index in range(begin, end):
            # j moves forward as long as the current item is larger than the pivot
            if array[index] > array[end]:
                j += 1
            # If the current value is smaller than the pivot, swap i and j  and increment both of them
            elif array[index] <= array[end]:
                array[i], array[j] = array[j], array[i]
                i += 1
                j += 1

        # Once through the whole thing, swap i for the pivot value to put it in its right place
        array[end], array[i] = array[i], array[end]
        # Call quicksort function on both ends of the array excluding the pivot which moved to position i
        quickSort(array, begin, i - 1)
        quickSort(array, i + 1, end)
        return array
    else:
        return array


def kth_largest(array, k):
    arr_size = len(array)
    if k <= arr_size:
        print(array[arr_size - k])


list = [5, 3, 1, 6, 4, 2]
print(list)
list = quickSort(list, 0, 5)
print(list)
kth_largest(list, 3)
