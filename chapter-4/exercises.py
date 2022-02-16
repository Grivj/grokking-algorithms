"""
Exercises page 59.
- 4.1 Write out the code for the earlier sum function. (sum_array)
- 4.2 Write a recursive function to count the number of items in a list. (len_array)
- 4.3 Find the maximum number in a list. (maximum_array)
- 4.4 Remember binary search from chapter 1?
It's a divide-and-conquer algorithm, too.
Can you come up with the base case and recursive case for binary search?
(binary_search)
"""


from numpy import rec


def sum_array(a: list[int]):
    return 0 if not a else a[0] + sum_array(a[1:])


def len_array(a: list[int]):
    return 0 if not a else 1 + len_array(a[1:])


def maximum_array(a: list[int]):
    return 0 if not a else max(a[0], maximum_array(a[1:]))


def binary_search(a: list[int], target: int):
    def recursive(a: list[int], low: int, high: int, target: int):
        if low <= high:
            mid = (high + low) // 2

            if a[mid] == target:
                return mid

            if a[mid] > target:
                return recursive(a, low, mid - 1, target)
            return recursive(a, mid + 1, high, target)
        return -1

    return recursive(a, 0, len(a) - 1, target)


if __name__ == "__main__":
    print(sum_array([1, 2, 3, 4, 5]))
    print(len_array([1, 2, 3, 4, 5]))
    print(maximum_array([1, 2, 3, 4, 5]))
    print(binary_search([1, 2, 3, 4, 5], 5))
