# http://www.cnblogs.com/eniac12/p/5329396.html
"""
冒泡排序: 从左向右每次循环找出当前数列中的最大值
时间复杂度: O(n^2)
冒泡排序算法：
1.比较相邻的元素，如果前一个比后一个大，调换位置。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对,最后的元素会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):               # 每次最大元素就像气泡一样"浮"到数组的最后
        for j in range(length - 1 - i):       # 依次比较相邻的两个元素,使较大的那个向后移
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    return arr


"""
鸡尾酒排序:从左向右循环找出最大值,从右向左循环找出最小值
时间复杂度: O(n^2)
鸡尾酒排序算法：
1.从左向右比较相邻的元素，如果前一个比后一个大，调换位置;
  从右向左比较相邻的元素，如果后一个比前一个小，调换位置。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对,最后的元素会是最大的数，第一个元素是最小的数。
3.针对所有的元素重复以上的步骤，除了最后一个和第一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def cocktail_sort(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        for i in range(left, right):                # 从左向右,较大数值向后移动
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
        right -= 1
        for j in range(right, left, -1):            # 从右向左,较小数值先前移动
            if arr[j - 1] > arr[j]:
                swap(arr, j - 1, j)
        left += 1
    return arr


"""
选择排序: 从左向右循环找出最小值保存到固定位置
时间复杂度: O(n^2)
选择排序算法:
1.从左向右依次比较第一个元素和后面的元素，如果第一个比后一个大，调换位置，第一个元素会是最小的数。
2.针对所有的元素重复以上的步骤，除了最后一个。
"""


def select_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(i + 1, length):         # 将左边的第一个数和后面的数分别比较,将最小的数交换到最左边
            if arr[i] > arr[j]:
                swap(arr, i, j)
    return arr


"""
插入排序: 左手已经拿到一张牌,将右手每次拿到的牌按升序插入正确的位置
时间复杂度: O(n^2)
插入排序算法:
1.从第二个元素开始，在已经排序的元素序列中从后向前扫描
2.如果后一个元素小于前面的元素，将该元素向前移动,直到找到已排序的元素小于或者等于该元素的位置
3.将新元素插入到该位置后
4.重复步骤1~3
"""


def insert_sort(arr):
    length = len(arr)
    for i in range(1, length):                 # 右手拿到一张牌拿在手里
        j = i - 1
        temp = arr[i]
        while arr[j] > temp and j >= 0:        # 从右现在,将右手的牌和前面的牌依次比较
            arr[j + 1] = arr[j]                # 右手的牌较小,向后移动前面的牌
            j -= 1
        arr[j + 1] = temp                      # 将右手的牌插入此位置
    return arr


"""
希尔排序: 一次将较小的数据向前移动h位
时间复杂度: O(n^2)
"""


def shell_sort(arr):
    length = len(arr)
    h = length // 2                                   # 初始步长
    while h >= 1:
        for i in range(h, length):
            j = i - h
            temp = arr[i]
            while arr[j] > temp and j >= 0:
                arr[j + h] = arr[j]
                j -= h
            arr[j + h] = temp
        h = h // 2                                    # 递减步长
    return arr


"""
归并排序
时间复杂度: O(nlogn)
"""


def merge(left, right):
    i, j = 0, 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp += left[i:]
    temp += right[j:]
    return temp


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


"""
快速排序
时间复杂度: O(nlogn)
快速排序算法:
1.从序列中挑出一个元素，作为"基准"(pivot)
2.把所有比基准值小的元素放在基准前面，所有比基准值大的元素放在基准的后面（相同的数可以到任一边）
3.对每个分区递归地进行步骤1~2，递归的结束条件是序列的大小是0或1
"""


def quick_sort(arr, left, right):
    if left >= right:
        return arr

    pivot = arr[left]
    low = left
    high = right
    while low < high:
        while low < high and arr[high] > pivot:
            high -= 1
        arr[low] = arr[high]

        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot

    quick_sort(arr, left, low - 1)
    quick_sort(arr, low + 1, right)
    return arr


"""
二分法查找
假设: 数据已经经过排序,且为升序
"""


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] > target:
            right = middle -1
        elif arr[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1
