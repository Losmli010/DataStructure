# 单向链表实现栈
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "Node<%s>" % self.data


class Stack(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.is_empty():
            return

        node = self.head
        self.head = self.head.next
        return node

    def append(self, data):
        self.head = Node(data, self.head)

    def __str__(self):
        result = 'HEAD'
        cur = self.head
        while cur:
            result += '-->%s' % cur.data
            cur = cur.next
        return result


# 固定大小的数组实现栈
class ArrayStack(object):
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
            return
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
    print(stack)
    stack.append(1)
    print(stack)
    stack.append(2)
    print(stack)
    stack.append(3)
    print(stack)
    node = stack.pop()
    print(stack, node)
    node = stack.pop()
    print(stack, node)
    node = stack.pop()
    print(stack, node)
    node = stack.pop()
    print(stack, node)

    arr = ArrayStack()
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
