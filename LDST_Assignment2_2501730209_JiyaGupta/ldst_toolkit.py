# ldst_toolkit.py
# Task 1: Dynamic Array

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = value
        self.size += 1

    def resize(self):
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            return "Array is empty"
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def __str__(self):
        return str([self.arr[i] for i in range(self.size)])


# Node Class (Used in Linked List)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


#Task 2: Singly Linked List

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, value):
        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if not temp:
            print("Value not found")
            return

        prev.next = temp.next

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)


# Doubly Linked List

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_after_node(self, target, value):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node(value)
                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return
            temp = temp.next

        print("Target not found")

    def delete_at_position(self, pos):
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)


# Task 3: Stack (Using SLL)

class Stack:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def push(self, value):
        self.sll.insert_at_beginning(value)

    def pop(self):
        if not self.sll.head:
            return "Stack Underflow"

        val = self.sll.head.data
        self.sll.head = self.sll.head.next
        return val

    def peek(self):
        if not self.sll.head:
            return "Empty Stack"
        return self.sll.head.data


# Queue (Using SLL)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if not self.tail:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return "Queue Underflow"

        val = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return val

    def front(self):
        if not self.head:
            return "Empty Queue"
        return self.head.data


# Task 4: Balanced Parentheses

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            top = stack.pop()
            if top != pairs[char]:
                return False

    return stack.peek() == "Empty Stack"


# MAIN TEST RUNNER

if __name__ == "__main__":

    print("\n Dynamic Array")
    arr = DynamicArray(2)
    for i in range(10):
        arr.append(i)
        print(arr)

    print("Pop:", arr.pop())
    print("Pop:", arr.pop())
    print("Pop:", arr.pop())
    print(arr)

    print("\n Singly Linked List")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(10)
    sll.insert_at_beginning(20)
    sll.insert_at_end(30)
    sll.insert_at_end(40)
    sll.traverse()

    sll.delete_by_value(20)
    sll.traverse()

    print("\n Doubly Linked List")
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_after_node(2, 99)
    dll.traverse()

    dll.delete_at_position(1)
    dll.traverse()

    print("\nStack")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())

    print("\nQueue")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Dequeue:", q.dequeue())
    print("Front:", q.front())

    print("\n Parentheses Checker")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", is_balanced(t))