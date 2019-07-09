"""
链表的特点和优缺点
链表在内存中非连续分配
链表中除了第一个和最后一个元素之外,其它数据元素首尾相连
链表在生存期可以自如伸缩
优点是插入和删除元素简单方便
缺点是不允许随机访问元素

链表的效率
插入和删除: O(1)
访问: O(n)
"""


class Node(object):
    """
    单向链表的实现
    节点类: 值域存放数据value,指针域存放下一个元素的指针next
    node.next = next_node指向下一个节点
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "Node<%s>" % self.data


class SingleLinkedList(object):
    # 创建空链表
    # head节点永远指向第一个节点
    def __init__(self):
        self.head = None
        self._size = 0

    # 链表大小
    def size(self):
        return self._size

    # 判断链表是否为空
    def is_empty(self):
        return self._size == 0

    # 链表头部插入数据
    def append_left(self, data):
        self.head = Node(data, self.head)
        self._size += 1

    # 链表尾部插入数据
    def append(self, data):
        # 头节点是空节点
        if not self.head:
            self.append_left(data)
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)
        self._size += 1

    def _check_index(self, index):
        if index < 0 or index > self._size:
            raise ValueError("Index out of linked list size!")

    # 插入
    def insert_by_index(self, index, data):
        self._check_index(index)

        if index == 0:
            self.append_left(data)
            return

        cur = self.head
        idx = 0
        while idx < index:
            cur = cur.next
            idx += 1
        cur.next = Node(data, cur.next)
        self._size += 1

    # 按索引删除
    def remove(self, index):
        if self.is_empty() or index >= self._size or index < 0:
            raise ValueError("Index out of linked list size!")

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

    # 返回中间节点
    def get_mid_node(self):
        slow, fast = self.head, self.head
        fast = fast.next if fast else None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow

    # 反转链表
    def reverse(self):
        if (self.head is None) or (self.head.next is None):
            return self

        reversed_head = None
        cur = self.head
        while cur:
            reversed_head, reversed_head.next, cur = cur, reversed_head, cur.next
        return reversed_head

    # 循环
    def __iter__(self):
        cur = self.head
        while cur.next:
            yield cur.data
            cur = cur.next

    # 打印
    def __str__(self):
        result = 'HEAD'
        cur = self.head
        while cur:
            result += '-->%s' % cur.data
            cur = cur.next
        return result


if __name__ == '__main__':
    ls = SingleLinkedList()
    for data in [1, 3, 5, 7]:
        ls.append(data)
    print(ls, ls.size(), ls.get_mid_node())
    ls.append_left(9)
    print(ls, ls.size(), ls.get_mid_node())

    ls.insert_by_index(2, 99)
    ls.insert_by_index(5, 66)
    print(ls, ls.size(), ls.get_mid_node())

    rt = ls.remove(0)
    print(ls, ls.size(), rt, ls.get_mid_node())
    rt = ls.remove(2)
    print(ls, ls.size(), rt, ls.get_mid_node())

    res = ls.reverse()
