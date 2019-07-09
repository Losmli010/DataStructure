class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return "Node<%r,%r,%r>" % (self.data, self.prev, self.next)


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

    # 按index添加
    def insert_by_index(self, index, data):
        pass

    # 按index删除
    def remove(self, index):
        pass

    # 删除节点
    def delete(self, data):
        pass

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
        print(alist)

    print("**********尾部添加**************")
    for data in [3, 5, 7]:
        alist.append(data)
        print(alist)