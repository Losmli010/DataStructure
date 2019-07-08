"""
数组特点和优缺点
数组在内存中是连续存储的
一旦被分配内存,数组大小固定,且不能更改
优点是支持索引的随机访问
缺点是改变数组长度的时候需要复制原有的所有元素, 删除或插入元素需要移动很多元素

数组的效率
插入: O(n)
删除: O(n)
搜索(线性): O(n)
访问(索引): O(1)
末尾插入和删除: O(1)
"""

"""
python列表的方法
list.append(x)       # 等价于 a[len(a):] = [x]
list.extend(L)       #等价于  a[len(a):] = L
list.insert(i, x)
list.remove(x)
list.pop(i)          #返回list[i]
list.index(x)
list.count(x)
list.sort(cmp=None, key=None, reverse=False)
list.reverse()
"""


class Array(object):
    """
    固定大小的数组，支持增删改查和遍历操作
    """
    def __init__(self, capacity=10):
        self.capacity = capacity
        self._length = 0
        self._arr = [None] * self.capacity

    def length(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def is_full(self):
        return self._length == self.capacity

    def append(self, item):
        if self.is_full():
            raise ValueError("Array is full.")
        self._arr[self._length] = item
        self._length += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Array is empty.")

        self._length -= 1
        item = self._arr[self._length]
        self._arr[self._length] = None
        return item

    def _check_range(self, idx):
        if idx < 0:
            raise IndexError("Index value out of range.")
        if idx > self._length:
            raise IndexError("Index value out of range.")

    def get(self, idx):
        self._check_range(idx)
        return self._arr[idx]

    def set(self, idx, item):
        self._check_range(idx)
        self._arr[idx] = item

    def __iter__(self):
        for item in self._arr[:self._length]:
            yield item

    def __str__(self):
        result = [] if self._length == 0 else self._arr[:self._length]
        return str(result)


if __name__ == '__main__':
    ls = Array()
    print(ls, ls.length())
    # ls.pop()
    ls.append("hello")
    print(ls)
    print(ls.get(0))
    for i in range(9):
        ls.append(i)
    print(ls, ls.length())
    # ls.append('world')
    print(ls.pop())
    print(ls)
    ls.set(1, "world")
    print(ls)
    for item in ls:
        print(item)
