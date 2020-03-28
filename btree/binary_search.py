def binary_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1

    return -1


def bisect_left(sorted_collection, item, lo=0, hi=None):
    if hi is None:
        hi = len(sorted_collection)

    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_collection[mid] < item:
            lo = mid + 1
        else:
            hi = mid

    return lo


def bisect_right(sorted_collection, item, lo=0, hi=None):
    if hi is None:
        hi = len(sorted_collection)

    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_collection[mid] <= item:
            lo = mid + 1
        else:
            hi = mid

    return lo
