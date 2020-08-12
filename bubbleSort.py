def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


nums = [4, 7, 1, 6, 3, 9, 12, 19]
print(bubble_sort(nums))
