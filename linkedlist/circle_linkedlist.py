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
            # 原始头节点
            temp = self.head
            # 新插入节点指向头节点
            self.head = Node(data, self.tail, self.head)
            # 原始头节点的前驱节点指向新的头节点
            temp.prev = self.head
            self.tail.next = self.head
        self._size += 1

    # 尾部添加
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            # 原始尾节点
            temp = self.tail
            # 新节点指向尾节点
            self.tail = Node(data, self.tail, self.head)
            # 原始尾节点的后驱节点指向新尾节点
            temp.next = self.tail
            self.head.prev = self.tail
        self._size += 1

    # 尾部删除
    def pop(self):
        if self.is_empty():
            return

        node = self.tail
        self.tail = self.tail.prev
        self.head.prev = self.tail
        self._size -= 1
        return node

    # 头部删除
    def prepop(self):
        if self.is_empty():
            return

        node = self.head
        self.tail.next = self.head.next
        self.head = self.head.next
        self._size -= 1
        return node

    def __str__(self):
        result = 'HEAD'
        cur = self.head
        i = 0
        while i < self._size:
            result += '-->%s' % cur.data
            cur = cur.next
            i += 1
        return result


if __name__ == '__main__':
    alist = CircleLinkedList()
    print("**********头部添加**************")
    for data in [1, 3, 5, 7]:
        alist.prepend(data)
        print(alist, alist.size(), alist.head, alist.tail)

    print("**********尾部添加**************")
    for data in [30, 50, 70]:
        alist.append(data)
        print(alist, alist.size(), alist.head, alist.tail)

    print("**********尾部删除**************")
    for _ in range(alist.size()):
        print(alist.pop(), alist)