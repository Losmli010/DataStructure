"""
堆是一个完全二叉树：完全二叉树要求，除了最后一层，其他层的节点个数都是满的，最后一层的节点都靠左排列。
堆中每一个节点的值都必须大于等于（或小于等于）其子树中每个节点的值
"""


class Heap(object):
    def __init__(self, capacity=64):
        self._capacity = capacity
        self._data = []
        self._size = 0      # 元素个数

    def headpush(self, value):
        """

        :return:
        """
        if self._size >= self._capacity:
            return

        self._data.append(value)
        self._size += 1

        self._siftup()

    def heappop(self):
        """
        返回堆顶元素
        自上往下堆化
        :return:
        """
        if self._size == 0:
            return -1
        if self._size == 1:
            value = self._data[0]
            self._data = []
            self._size = 0
            return value

        value = self._data[0]
        print(value, self._size)
        self._data[0] = self._data[self._size - 1]
        self._data.pop()
        self._size -= 1

        self._siftdown()
        return value

    def _siftup(self):
        """
        自下往上堆化
        保证节点值大于等于子树节点值
        :return:
        """
        child = self._size - 1
        parent = (child - 1) // 2
        while (parent >= 0) and (self._data[parent] < self._data[child]):
            temp = self._data[parent]
            self._data[parent] = self._data[child]
            self._data[child] = temp
            child = parent
            parent = (child - 1) // 2

    def _siftdown(self):
        """
        自上往下堆化
        保证节点值大于等于子树节点值
        :return:
        """
        parent = 0
        while True:
            child = parent * 2 + 1
            if (child < self._size) and (self._data[parent] < self._data[child]):
                temp = self._data[parent]
                self._data[parent] = self._data[child]
                self._data[child] = temp
                parent = child
            else:
                break

    def __str__(self):
        return "%r" % self._data


if __name__ == '__main__':
    heap = Heap()
    for val in [10, 2, 66, 8, 5, 28, 45, 99]:
        heap.headpush(val)
    print(heap)

    value = heap.heappop()
    print(value, heap)
