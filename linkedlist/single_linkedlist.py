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

# 单向链表的实现
# 节点类: 值域存放数据value,指针域存放下一个元素的指针next
# node.next = next_node指向下一个节点
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList(object):
    # 创建空链表
    # head节点永远指向第一个节点
    def __init__(self):
        self.head = Node()
        self._size = 0

    # 链表大小
    def size(self):
        return self._size

    # 判断链表是否为空
    def is_empty(self):
        return self._size == 0

    # 链表头部插入数据
    def add_first(self, data):
        self.head.next = Node(data, self.head.next)
        self._size += 1

    # 链表尾部插入数据
    def add_last(self, data):
        #头节点是空节点
        if not self.head.next:
            self.add_first(data)
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)
        self._size += 1

    def _check_index(self, index):
        if index < 0 or index > self.size():
            raise ValueError("Index out of linked list size!")

    # 插入
    def insert(self, index, data):
        self._check_index(index)

        if index == 0:
            self.add_first(data)
            return

        cur = self.head
        i = 1
        while i <= index:
            cur = cur.next
            i += 1
        cur.next = Node(data, cur.next)
        self._size += 1

    # 按索引删除
    def remove(self, index):
        if self.is_empty() or index >= self.size() or index < 0:
            raise ValueError("Index out of linked list size!")

        if index == 0:
            data = self.head.next.data
            self.head.next = self.head.next.next
            self._size -= 1
            return data

        cur = self.head
        i = 1
        while i <= index:
            cur = cur.next
            i += 1
        data = cur.next.data
        cur.next = cur.next.next
        self._size -= 1
        return data

    # 按数据删除
    def delete(self, data):
        if self.is_empty():
            raise ValueError("Linked list is empty!")
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                self._size -= 1
                return
            cur = cur.next
        raise ValueError("Data not exits in Linked list!")

    def __str__(self):
        result = 'HEAD'
        cur = self.head.next
        while cur:
            result += '--->%s' % str(cur.data)
            cur = cur.next
        return result


if __name__ == '__main__':
    ls = SingleLinkedList()
    ls.add_first(1)
    ls.add_last(2)
    ls.insert(1, 3)
    ls.insert(3, 8)
    ls.insert(2, 99)
    ls.insert(5, 66)
    print(ls, ls.size())
    rt = ls.remove(0)
    print(ls, ls.size(), rt)
    rt = ls.remove(2)
    print(ls, ls.size(), rt)
    rt = ls.remove(1)
    print(ls, ls.size(), rt)
    ls.delete(8)
    print(ls, ls.size())
    ls.delete(3)
    print(ls, ls.size())
