# 单向链表实现队列: 改进增加尾节点
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "Node<%s>" % self.data


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        node = Node(data)
        # 链表为空,头节点和尾节点为插入节点
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def popleft(self):
        if self.is_empty():
            return 

        node = self.head
        self.head = self.head.next

        if self.is_empty():
            self.tail = None
        return node

    def __str__(self):
        result = 'HEAD'
        cur = self.head
        while cur:
            result += '-->%s' % cur.data
            cur = cur.next
        return result


if __name__ == '__main__':
    queue = Queue()
    print(queue)
    queue.append(1)
    print(queue)
    queue.append(2)
    print(queue)
    queue.append(3)
    print(queue)
    queue.popleft()
    print(queue)
    queue.popleft()
    print(queue)
    queue.popleft()
    print(queue)
    # queue.popleft()
