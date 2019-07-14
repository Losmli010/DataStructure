"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

LRU全称是Least Recently Used，即最近最久未使用
LRU算法的设计原则是：如果一个数据在最近一段时间没有被访问到，那么在将来它被访问的可能性也很小。

LRU Cache具备的操作：
1）set(key,value)：如果key在hashmap中存在，则先重置对应的value值，然后获取对应的节点cur，将cur节点从链表删除，并移动到链表的头部；
                   如果key在hashmap不存在，则新建一个节点，并将节点放到链表的头部。当Cache存满的时候，将链表最后一个节点删除即可。
2）get(key)：如果key在hashmap中存在，则把对应的节点放到链表头部，并返回对应的value值；如果不存在，则返回-1。
"""
import pickle



class Entry(object):
    """
    单向链表结合双向链表
    """
    def __init__(self, key, value, prev=None, next=None, hnext=None):
        self.key = key
        self.value = value
        # 双向链表
        self.prev = prev
        self.next = next
        # 单向链表
        self.hnext = hnext

    def copy(self):
        return pickle.loads(pickle.dumps(self, 4))

    def __str__(self):
        return "Entry<%r, %r, %r, %r, %r>" % (self.key, self.value, self.prev, self.next, self.hnext)


class LRUCache(object):
    def __init__(self, capacity=128):
        self._capacity = capacity
        self._buckets = [None] * self._capacity
        # key-value个数
        self._size = 0
        # 双向链表
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :param key:
        :return:
        """

    def set(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        idx = self._hash(key)
        # 双向链表中无数据
        if self.head is None:
            entry = Entry(key, value)
            self.head = entry
            self.tail = entry
            # 单向链表
            self._buckets[idx] = entry
            self._size += 1
            print('无数据')
        else:
            single = self._buckets[idx]
            # 单向链表中无数据
            if single is None:
                # 新数据添加到双向链表头部
                print('新数据添加到双向链表头部')
                self._move2head(key, value)
                self._buckets[idx] = self.head
                # print(self.head, self.tail.prev)
            else:
                print(single, single.prev, single.next)
                # 单向链表第一个节点
                if single.key == key:
                    print('单向链表第一个节点')
                    if single is self.head:
                        self.head.value = value
                    elif single is self.tail:
                        self._delete_tail()
                        self._move2head(key, value)
                    else:
                        print('删除节点')
                        # 删除节点
                        print(single, single.prev, single.next)
                        single.prev.next = single.next
                        self._size -= 1
                        self._move2head(key, value)
                    return
                else:
                    while single.hnext:
                        prev = single.copy()
                        single = single.hnext
                        # 单向链表第二个节点
                        if single.key == key:
                            # key已经存在，删除，添加到头部
                            prev.next = single.next
                            self._size -= 1
                            self._move2head(key, value)
                            prev.hnext = single.hnext
                            self._buckets[idx] = prev
                            return

                    # key不存在，添加到头部
                    # cache满了, 删除尾部
                    print(11111111)
                    if self._size == self._capacity:
                        self._delete_tail()
                    self._move2head(key, value)

    def _delete_node(self, node):
        if node is None:
            return 
        tail = self.tail.copy()
        self.tail = tail.prev
        self.tail.next = self.head
        self._size -= 1

    def _move2head(self, node):
        node = node.copy()
        head = self.head.copy()
        self.head = Entry(key, value, self.tail, head)
        self.tail.next = self.head
        self._size += 1

    def _hash(self, key):
        """
        哈希函数
        :param key:
        :return:
        """
        power = 0
        hashing = 0
        for char in str(key):
            hashing += (ord(char) - 32) * pow(95, power)
            power += 1
        index = hashing % self._capacity
        return index

    def __str__(self):
        result = 'HEAD'
        cur = self.head
        i = 0
        print(self._size)
        while i < self._size:
            result += '--><%r, %r>' % (cur.key, cur.value)
            cur = cur.next
            i += 1
        return result


if __name__ == '__main__':
    cache = LRUCache(4)
    cache.set(1, 1)
    print(cache)
    cache.set(2, 2)
    print(cache)
    cache.set(3, 3)
    print(cache)
    cache.set(4, 4)
    print(cache)
    cache.set(3, 8)
    print(cache)
