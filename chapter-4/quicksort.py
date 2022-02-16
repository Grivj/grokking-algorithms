def quicksort(array: list[int]):
    if len(array) < 2:
        return array
    pivot = array.pop(len(array) // 2)
    lesser = [i for i in array if i < pivot]
    greater = [i for i in array if i > pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    print(quicksort([9, 1, 3, 5, 4, 2, 8, 6, 7]))
