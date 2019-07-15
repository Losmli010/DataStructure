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

        entry = self._search(key)
        if entry is not None:
            self._delete(entry)
            return
        self._add2head(key, value)

        # key不存在，添加到头部
        # cache满了, 删除尾部
        if self._size > self._capacity:
            self._delete_tail()
            self._add2head(key, value)

    def _search(self, key):
        # 找到单链表中键值为key的节点并返回
        idx = self._hash(key)
        entry = self._buckets[idx]
        while entry:
            if entry.key == key:
                return entry
            entry = entry.hnext
        return

    def _delete(self, entry):
        if self.head is None:
            return

        # 双向链表删除操作
        entry.prev.next = entry.next
        self._size -= 1
        idx = self._hash(entry.key)
        single = self._buckets[idx]
        # 单向链表第一个节点
        if entry is single:
            self._buckets[idx] = single.hnext
        else:
            while single:
                prev = single.copy()
                single = single.hnext
                if entry is single:
                    prev.hnext = single.hnext
                    self._buckets[idx] = prev
                    return

    def _delete_tail(self):
        if self.head is None:
            return
        tail = self.tail.copy()
        self.tail = tail.prev
        self.head.prev = self.tail
        self._size -= 1

    def _add2head(self, key, value):
        if self.head is None:
            self.head = Entry(key, value)
            self.tail = self.head
        else:
            temp = self.head
            self.head = Entry(key, value, self.tail, self.head)
            temp.prev = self.head
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
