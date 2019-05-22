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
        return not self.head

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

if __name__ == '__main__':
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
