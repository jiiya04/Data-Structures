
# Part A: Stack ADT


class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Part B: Factorial (Recursive)


def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)



# Fibonacci (Naive Recursion)

naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


# Fibonacci (Memoization)


memo_calls = 0

def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]



# Part C: Tower of Hanoi

def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return

    hanoi(n-1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)

    hanoi(n-1, auxiliary, source, destination, stack)


# Part D: Recursive Binary Search


def binary_search(arr, key, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)

    else:
        return binary_search(arr, key, mid + 1, high)


# Main Testing Function


def main():

    print(" AERT TOOLKIT OUTPUT ")

    # Factorial Tests
    print("\nFactorial Test Cases")
    test_values = [0, 1, 5, 10]

    for n in test_values:
        print(f"factorial({n}) =", factorial(n))


    # Fibonacci Tests
    print("\nFibonacci Test Cases")

    fib_tests = [5, 10, 20, 30]

    global naive_calls, memo_calls

    for n in fib_tests:

        naive_calls = 0
        memo_calls = 0

        naive_result = fib_naive(n)
        naive_count = naive_calls

        memo_result = fib_memo(n, {})
        memo_count = memo_calls

        print(f"\nFibonacci({n})")
        print("Naive Result:", naive_result)
        print("Naive Calls:", naive_count)

        print("Memoized Result:", memo_result)
        print("Memoized Calls:", memo_count)


    # Tower of Hanoi
    print("\nTower of Hanoi (N = 3)")

    move_stack = StackADT()

    hanoi(3, 'A', 'B', 'C', move_stack)

    print("\nTotal Moves Stored in Stack:", move_stack.size())


    # Binary Search Tests
    print("\nBinary Search Test Cases")

    arr = [1,3,5,7,9,11,13]

    keys = [7, 1, 13, 2]

    for key in keys:
        result = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key} -> Index:", result)

    # empty array test
    arr2 = []
    print("Search in empty array ->", binary_search(arr2, 5, 0, -1))

if __name__ == "__main__":
    main()