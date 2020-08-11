def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        # Middle element of list.
        mid = int((low + high) / 2)
        guess = list[mid]

        # Found!
        if guess == item:
            return mid
        if guess > item:  # More ...
            high = mid - 1
        else:  # Few ...
            low = mid + 1
    return None


my_list = [1, 5, 7, 9, 10, 13, 25]

print(binary_search(my_list, 9))
