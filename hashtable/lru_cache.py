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



class LRUCache(object):
    def __init__(self, capacity=64):
        self._capacity = capacity
        self._buckets = [None] * self._capacity
        # key-value个数
        self._size = 0

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
