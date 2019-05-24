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

#单向链表的实现
#节点类: 值域存放数据value,指针域存放下一个元素的指针next
#node.next = next_node指向下一个节点
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList(object):
    #创建空链表
    #head节点永远指向第一个节点
    def __init__(self):
        self.head = Node()
        self._size = 0

    #链表大小
    def size(self):
        return self._size

    #判断链表是否为空
    def is_empty(self):
        return self._size == 0

    #链表头部插入数据
    def add_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self._size += 1

    #链表尾部插入数据
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



    #插入
    def insert(self, index, data):
        if index < 0 or index > self.size():
            raise ValueError("Index out of linked list size!")

        if index == 0:
            self.add_first(data)
            return

        cur = self.head
        i = 1
        while i != index:
            cur = cur.next
            i += 1
        cur.next = Node(data, cur.next)

    #删除
    def remove(self, data):
        if not self.head:
            raise ValueError("Linked list is empty!")

        if self.head.value == data:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next:
            if cur.next.value == data:
                cur.next = cur.next.next
                return
            else:
                cur = cur.next
        raise ValueError("Data not in linked list!")

    def search(self, data):
        cur = self.head
        while cur and cur.value != data:
            cur = cur.next
        return cur

    def test(self):
        values = []
        cur = self.head
        while cur:
            values.append(cur.value)
            cur = cur.next
        return values


if __name__ == '__main__':
    lists = SingleLinkedList()
    print(lists.test())
    lists.append(12)
    print(lists.test())
    lists.add_first(1)
    print(lists.test())
    lists.insert(1, 0)
    print(lists.test())
    lists.append(2)
    print(lists.test())
    lists.remove(0)
    print(lists.test())
