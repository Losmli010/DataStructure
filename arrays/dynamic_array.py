from arrays.array import Array


class DynamicArray(Array):
    """
    动态扩容数组，支持增删改查和遍历以及合并操作
    """
    def resize(self):
        self.capacity *= 2
        old_arr = self._arr
        self._arr = [None] * self.capacity
        for idx, item in enumerate(old_arr):
            self._arr[idx] = item

    def append(self, item):
        if self.is_full():
            self.resize()
        self._arr[self._length] = item
        self._length += 1

    def extend(self, arr):
        for item in arr:
            self.append(item)

if __name__ == '__main__':
    ls = DynamicArray()
    for i in range(15):
        ls.append(i)
    print(ls)
    print(ls.index(10))
    for _ in range(5):
        print(ls.pop())
    print(ls)
    arr = [i for i in range(100, 200)]
    ls.extend(arr)
    print(ls)
