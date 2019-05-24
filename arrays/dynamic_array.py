from arrays.array import Array


class DynamicArray(Array):
    """
    动态扩容数组，支持增删改查和遍历以及合并操作
    """
    def _resize(self):
        old_capacity = self.capacity
        self.capacity = (old_capacity * 3) // 2 + 1
        old_arr = self._arr
        self._arr = [None] * self.capacity
        for idx, item in enumerate(old_arr):
            self._arr[idx] = item

    def append(self, item):
        if self.is_full():
            self._resize()
        self._arr[self._length] = item
        self._length += 1

    def extend(self, arr):
        for item in arr:
            self.append(item)

if __name__ == '__main__':
    ls = DynamicArray()
    for i in range(20):
        ls.append(i)
    print(ls)
    print(ls.get(10))
    for _ in range(5):
        print(ls.pop())
    print(ls)
    arr = [i for i in range(100, 228)]
    ls.extend(arr)
    print(ls)
