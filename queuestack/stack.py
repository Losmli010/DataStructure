#单向链表实现栈
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack(object):
    def __init__(self):
        self.head = None

    def pop(self):
        if not self.head:
            raise ValueError("Stack is empty!")

        value = self.head.value
        self.head = self.head.next
        return value

    def append(self, value):
        if not value:
            raise ValueError("Invalid value!")
        self.head = Node(value, self.head)

    def test(self):
        values = []
        cur = self.head
        while cur:
            values.append(cur.value)
            cur = cur.next
        return values


#固定大小的数组实现栈
class StackArray(object):
    def __init__(self, capacity=10):
        self.elements = [None] * capacity
        self.top = -1

    def append(self, value):
        if self.is_full():
            raise ValueError("Stack is full!")
        self.top += 1
        self.elements[self.top] = value

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty!")
        value = self.elements[self.top]
        self.elements[self.top] = None
        self.top -= 1
        return value

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (len(self.elements) - 1)


if __name__ == '__main__':
    stack = Stack()
    print(stack.test())
    stack.append(1)
    print(stack.test())
    stack.append(2)
    print(stack.test())
    stack.append(3)
    print(stack.test())
    stack.pop()
    print(stack.test())
    stack.pop()
    print(stack.test())
    stack.pop()
    print(stack.test())
    # stack.pop()

    arr = StackArray()
    print(arr.elements)
    arr.append(1)
    print(arr.elements)
    arr.append(2)
    print(arr.elements)
    arr.append(3)
    print(arr.elements)
    arr.pop()
    print(arr.elements)
    arr.pop()
    print(arr.elements)
    arr.pop()
    print(arr.elements)
    # arr.pop()
