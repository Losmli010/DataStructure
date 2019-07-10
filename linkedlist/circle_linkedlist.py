from linkedlist.double_linkedlist import Node, DoubleLinkedList


class CircleLinkedList(DoubleLinkedList):
    """
    循环链表
    """
    def __init__(self):
        super().__init__()
        self.tail = None

    # 头部添加
    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = self.head
            self.head = Node(data, self.tail, self.head)
            temp.prev = self.head
            self.tail.next = self.head
        self._size += 1

    # 尾部添加
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail = Node(data, self.tail, self.head)
            self.head.prev = self.tail
        self._size += 1

    # 尾部删除
    def pop(self):
        pass

    # 头部添加
    def prepop(self):
        pass

    def __str__(self):
        result = 'HEAD'
        cur = self.head
        i = 0
        while i < self._size:
            result += '-->%s' % cur.data
            cur = cur.next
            i += 1
        result += '-->TAIL'
        return result


if __name__ == '__main__':
    alist = CircleLinkedList()
    print("**********头部添加**************")
    for data in [1, 3, 5, 7]:
        alist.prepend(data)
        print(alist, alist.size(), alist.head, alist.tail)

    print("**********尾部添加**************")
    for data in [3, 5, 7]:
        alist.append(data)
        print(alist, alist.size(), alist.head, alist.tail)
