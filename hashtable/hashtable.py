class Entry(object):
    """
    单向链表
    """
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return "Entry<%r, %r>" % (self.key, self.value)


class HashTable(object):
    """
    基于链表法解决冲突问题的散列表
    """
    def __init__(self, capacity=16):
        """
        :param capacity: 桶个数
        """
        self._capacity = capacity
        self._buckets = [None] * self._capacity
        # key-value个数
        self._size = 0

    def has_key(self, key):
        """
        键值是否存在
        :param key:
        :return:
        """
        idx = self._hash(key)
        entry = self._buckets[idx]
        while entry:
            if entry.key == key:
                return True
            entry = entry.next
        return False

    def add(self, key, value):
        """
        添加
        :param key:
        :param value:
        :return:
        """
        if self._size >= self._capacity:
            self._resize()

        idx = self._hash(key)
        entry = self._buckets[idx]
        # idx对应的桶中没有数据
        if entry is None:
            self._buckets[idx] = Entry(key, value)
            self._size += 1
            return
        else:
            # 链表第一个键值对需要修改
            if entry.key == key:
                entry.value = value
                return
            while entry.next:
                entry = entry.next
                # 键值存在，更新值
                if entry.key == key:
                    entry.value = value
                    return
            # 键值不存在，添加到链表尾部
            entry.next = Entry(key, value)
            self._size += 1

    def remove(self, key):
        """
        删除
        :param key:
        :return:
        """
        if self.has_key(key):
            idx = self._hash(key)
            entry = self._buckets[idx]
            # 第一个节点就是要删除的节点
            if entry.key == key:
                self._buckets[idx] = entry.next
                self._size -= 1
                return entry.value
            # 删除节点为链表中间节点
            prev = entry
            entry = entry.next
            while entry:
                if entry.key == key:
                    prev.next = entry.next
                    self._size -= 1
                    return entry.value
                prve = entry
                entry = entry.next

    def get(self, key):
        """
        查找
        :param key:
        :return:
        """
        idx = self._hash(key)
        entry = self._buckets[idx]
        while entry:
            if entry.key == key:
                return entry.value
            entry = entry.next

    def _resize(self):
        """
        进行扩容: 当键值对数量超过容量大小时进行扩容
        :return:
        """
        # 扩容为原来的2倍
        old_capacity = self._capacity
        self._capacity = 2 * old_capacity
        new_buckets = [None] * self._capacity
        old_buckets = self._buckets
        self._transfer(old_buckets, new_buckets)
        self._buckets = new_buckets

    def _transfer(self, old_buckets, new_buckets):
        # 取桶中的链表
        for entry in old_buckets:
            # 取链表中的键值对
            while entry:
                idx = self._hash(entry.key)
                new_entry = new_buckets[idx]
                if new_entry is None:
                    new_buckets[idx] = Entry(entry.key, entry.value)
                else:
                    while new_entry.next:
                        new_entry = new_entry.next
                    new_entry.next = Entry(entry.key, entry.value)
                entry = entry.next

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

    def get_distribution(self):
        string = ''
        min_entries = None
        max_entries = 0
        total_entries = 0
        for entry in self._buckets:
            if entry is not None:
                count = 0
                while entry:
                    count += 1
                    entry = entry.next
                total_entries += count
                if count > max_entries:
                    max_entries = count
                if (min_entries is None) or (count < min_entries):
                    min_entries = count
        string += ("Largest Bucket has %d entries\n"
                   "Smallest Bucket has %d entries\n"
                   "Total entries: %d\n"
                   "Avg bucket size is %.1f" % (max_entries, min_entries, total_entries, (total_entries / self._capacity)))
        return string

    def __iter__(self):
        result = []
        for entry in self._buckets:
            if entry is not None:
                while entry:
                    yield entry
                    entry = entry.next
        return result

    def __str__(self):
        result = []
        for entry in self._buckets:
            if entry is not None:
                while entry:
                    result.append((entry.key, entry.value))
                    entry = entry.next
        return str(result)


if __name__ == '__main__':
    dictionary = HashTable()
    print("*************添加键值对********************")
    for key, value in enumerate(range(100, 140)):
        dictionary.add(key, value)
    print(dictionary)
    print(dictionary.get_distribution())

    print("*************获取键值********************")
    print(dictionary.get(10))

    print("*************修改键值********************")
    print(dictionary.add(11, 1000), dictionary.get(11))

    print("*************删除键值********************")
    for key in range(40):
        print(dictionary.remove(key), dictionary)
