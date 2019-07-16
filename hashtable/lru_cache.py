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

"""
存在bug
"""


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
        entry = self.has_key(key)
        if entry:
            self._delete(key)
            self._move2head(key, entry.value)
            return entry.value
        return -1

    def set(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        if self.has_key(key):
            self._delete(key)
            self._move2head(key, value)
        elif self._size == self._capacity:
            # 键值不存在
            # cache满了, 删除尾部，添加到头部
            self._delete(self.tail.key)
            self._move2head(key, value)
        else:
            # cache未满， 添加到头部
            self._move2head(key, value)

    def has_key(self, key):
        # 判断单链表中是否有键值为key的节点
        idx = self._hash(key)
        entry = self._buckets[idx]
        while entry:
            if entry.key == key:
                return entry
            entry = entry.hnext

    def _delete(self, key):
        if self.head.key == key:
            return

        idx = self._hash(key)
        single = self._buckets[idx]
        # 单向链表第一个节点
        if single.key == key:
            # 双向链表删除操作
            single.prev.next = single.next
            self._size -= 1
            self._buckets[idx] = single.hnext
        else:
            while single:
                prev = single.copy()
                single = single.hnext
                if single.key == key:
                    single.prev.next = single.next
                    prev.hnext = single.hnext
                    self._size -= 1
                    self._buckets[idx] = prev
                    return

    def _move2head(self, key, value):
        if (self.head is not None) and (self.head.key == key):
            self.head.value = value
            return

        idx = self._hash(key)
        if self.head is None:
            # 双向链表为空
            self.head = Entry(key, value)
            self.tail = self.head
            self._buckets[idx] = self.head
        else:
            # key值不存在
            temp = self.head
            self.head = Entry(key, value, self.tail, self.head)
            temp.prev = self.head
            self.tail.next = self.head
            self._buckets[idx] = self.head
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
    cache.set(5, 5)
    print(cache)
    cache.set(5, 9)
    print(cache)

    print(cache.get(10), cache)
    print(cache.get(3), cache)
    print(cache.get(5), cache)
    print(cache.get(4), cache)
