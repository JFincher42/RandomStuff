def selection_sort(data):
    unsorted = 0

    while unsorted < len(data) - 1:
        lowest = unsorted
        for i in range(unsorted, len(data)):
            if data[i] < data[lowest]:
                lowest = i

        temp = data[lowest]
        data[lowest] = data[unsorted]
        data[unsorted] = temp

        unsorted += 1


def binary_search(data, item):
    first = 0
    last = len(data)-1
    mid = (first + last) // 2

    while first <= last:
        if item == data[mid]:
            return True

        if item < data[mid]:
            last = mid - 1
        else:
            first = mid + 1

        mid = (first + last) // 2
    return False


numbers = [5, 2, 6, 12, 43, 3, 11]

print(f"numbers = {numbers}")
selection_sort(numbers)
print(f"sorted = {numbers}")

print(f"Found 10 in numbers: {binary_search(numbers, 10)}")
print(f"Found 12 in numbers: {binary_search(numbers, 12)}")