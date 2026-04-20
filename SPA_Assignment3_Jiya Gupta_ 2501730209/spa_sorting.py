import random
import time
import sys

sys.setrecursionlimit(20000)


# Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Merge Sort

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Quick Sort

def partition(arr, low, high):
    # Random pivot to avoid worst case
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr

# Timing Function

def measure_time(sort_func, arr):
    copy_arr = arr.copy()

    start = time.perf_counter()

    if sort_func == quick_sort:
        sort_func(copy_arr, 0, len(copy_arr) - 1)
    else:
        sort_func(copy_arr)

    end = time.perf_counter()

    return round((end - start) * 1000, 3)

# Dataset Generator

def generate_random(size):
    return random.sample(range(1, 100000), size)


def generate_sorted(size):
    return list(range(1, size + 1))


def generate_reverse(size):
    return list(range(size, 0, -1))



# Main Program

def main():
    random.seed(42)

    # Correctness Check
    test = [5, 2, 9, 1, 5, 6]

    print("Correctness Check:")
    print("Original :", test)
    print("Insertion:", insertion_sort(test.copy()))
    print("Merge    :", merge_sort(test.copy()))
    print("Quick    :", quick_sort(test.copy(), 0, len(test) - 1))

    print("\nSorting Performance Table (ms)")
    print("-" * 85)

    sizes = [1000, 5000, 10000]

    for size in sizes:

        datasets = {
            "Random": generate_random(size),
            "Sorted": generate_sorted(size),
            "Reverse": generate_reverse(size)
        }

        for dtype, data in datasets.items():

            t1 = measure_time(insertion_sort, data)
            t2 = measure_time(merge_sort, data)
            t3 = measure_time(quick_sort, data)

            print(
                f"Size={size:<5} "
                f"Type={dtype:<8} "
                f"Insertion={t1:<10} "
                f"Merge={t2:<10} "
                f"Quick={t3:<10}"
            )

if __name__ == "__main__":
    main()