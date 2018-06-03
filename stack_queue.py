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
        return (self.top == -1)

    def is_full(self):
        return (self.top == len(self.elements) - 1)

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

#单向链表实现队列: 改进增加尾节点
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Queue(object):
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return (not self.head)

    def append(self, data):
        node = Node(data)
        #链表为空,头节点和尾节点为插入节点
        if self.is_empty():
            self.head = self.last = node
        else:
            self.last.next = node
            self.last = node

    def popleft(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")

        value = self.head.value
        self.head = self.head.next

        if self.is_empty():
            self.last = None
        return value

    def test(self):
        values = []
        cur = self.head
        while cur:
            values.append(cur.value)
            cur = cur.next
        return values

queue = Queue()
print(queue.test())
queue.append(1)
print(queue.test())
queue.append(2)
print(queue.test())
queue.append(3)
print(queue.test())
queue.popleft()
print(queue.test())
queue.popleft()
print(queue.test())
queue.popleft()
print(queue.last)
# queue.popleft()

#栈: 先进后出
#深度遍历
import os

def get_file_stack(path):
    all_files = []
    #创建空栈
    stack = []
    stack.append(path)
    while stack:
        #从栈中删除数据,后进先删除
        dir_path = stack.pop()
        file_names = os.listdir(dir_path)
        for name in file_names:
            file_path = os.path.join(dir_path, name)
            if os.path.isdir(file_path):
                stack.append(file_path)
            else:
                all_files.append(name)
    return all_files

#队列: 先进先出
#广度遍历
from collections import deque

def get_file_queue(path):
    all_files = []
    #创建空队列
    queue = deque()
    queue.append(path)
    while queue:
        #从队列中删除数据,先进先删除
        dir_path = queue.popleft()
        file_names = os.listdir(dir_path)
        for name in file_names:
            file_path = os.path.join(dir_path, name)
            if os.path.isdir(file_path):
                queue.append(file_path)
            else:
                all_files.append(name)
    return all_files

path = os.getcwd()
print(get_file_queue(path))