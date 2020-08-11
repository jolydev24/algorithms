def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        # Pivot of array.
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]  # All before pivot.
        greater = [i for i in arr[1:] if i > pivot]  # All after pivot.

        return qsort(less) + [pivot] + qsort(greater)


print(qsort([10, 5, 2, 8, 12]))
