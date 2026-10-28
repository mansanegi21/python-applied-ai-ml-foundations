
# Searching and Sorting Algorithms

# 1. Linear Search
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


# 2. Binary Search
# The list must already be sorted.
def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# 3. Bubble Sort
def bubble_sort(numbers):
    arr = numbers.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Test the algorithms
numbers = [64, 25, 12, 22, 11]
target = 22

print("Original list:", numbers)

print("Linear search index:",
      linear_search(numbers, target))

sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)

print("Binary search index:",
      binary_search(sorted_numbers, target))
