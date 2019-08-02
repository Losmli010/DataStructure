def fib(n):
    """
    斐波那契数列: f(n) = f(n-1) + f(n-2)
    :param n:
    :return:
    """
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


def factorial(n):
    """
    阶乘: n!
    :param n:
    :return:
    """
    if n < 2:
        return 1
    return n * factorial(n - 1)


def permutation(array, begin, end, result=[]):
    """
    数据集合的全排列
    :param array:
    :return:
    """
    if begin == end:
        result.append(tuple(array))
    else:
        for idx in range(begin, end):
            # 将当前元素和第一位元素交换位置
            array[idx], array[begin] = array[begin], array[idx]
            # 排列除第一位的元素
            permutation(array, begin + 1, end)
            array[idx], array[begin] = array[begin], array[idx]
    return result


if __name__ == '__main__':
    fib_list = [fib(n) for n in range(1, 10)]
    print('斐波拉契数列：%r' % fib_list)

    factorial_list = [factorial(n) for n in range(10)]
    print('阶乘集合：%r' % factorial_list)

    permutation_list = permutation([1, 2, 3, 4], 0, 4)
    print('全排列：%r' % permutation_list)
