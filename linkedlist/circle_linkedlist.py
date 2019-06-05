class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class CircleLinkedList(object):
    """
    循环链表
    """
    def __init__(self):
        self.head = Node()
        self.tail = Node(next=self.head)