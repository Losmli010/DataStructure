class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        prev = self.prev.data if self.prev else None
        next = self.next.data if self.next else None
        return "Node<%s, %s, %s>" % (self.data, prev, next)


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self._size = 0

    # 链表大小
    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # 头部添加
    def prepend(self, data):
        self.head = Node(data, next=self.head)
        self._size += 1

    # 尾部添加
    def append(self, data):
        if self.head is None:
            self.prepend(data)

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data, cur)
        self._size += 1

    def _check_index(self, index):
        if index < 0 or index > self._size:
            raise ValueError("Index out of linked list size!")

    # 按index添加
    def insert_by_index(self, index, data):
        self._check_index(index)

        if index == 0:
            self.prepend(data)
            return

        cur = self.head
        idx = 1
        while idx < index:
            cur = cur.next
            idx += 1
        cur.next = Node(data, cur, cur.next)
        self._size += 1

    # 按index删除
    def remove(self, index):
        if self.is_empty():
            raise ValueError("Index out of linked list size!")
        self._check_index(index)

        if index == 0:
            node = self.head
            self.head = self.head.next
            self._size -= 1
            return node

        cur = self.head
        idx = 1
        while idx < index:
            cur = cur.next
            idx += 1
        node = cur.next
        cur.next = cur.next.next
        self._size -= 1
        return node

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        result = 'HEAD'
        cur = self.head
        while cur:
            result += '-->%s' % cur.data
            cur = cur.next
        return result


if __name__ == '__main__':
    alist = DoubleLinkedList()
    print("**********头部添加**************")
    for data in [1, 3, 5, 7]:
        alist.prepend(data)
        print(alist, alist.size())

    print("**********尾部添加**************")
    for data in [3, 5, 7]:
        alist.append(data)
        print(alist, alist.size())

    print("**********按索引添加************")
    alist.insert_by_index(0, 22)
    alist.insert_by_index(2, 44)
    alist.insert_by_index(9, 66)
    print(alist, alist.size())

    print("**********按索引删除************")
    rs = alist.remove(0)
    print(alist, alist.size(), rs)
    rs = alist.remove(1)
    print(alist, alist.size(), rs)
    rs = alist.remove(7)
    print(alist, alist.size(), rs)
