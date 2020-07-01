"""
问题：
给出一个整数数组，请在数组中找出两个加起来等于目标值的数，
你给出的函数twoSum 需要返回这两个数字的下标（index1，index2），需要满足 index1 小于index2.。注意：下标是从1开始的
假设给出的数组中只存在唯一解
例如：
给出的数组为 {2, 7, 11, 15},目标值为9
输出 index1=1, index2=2
"""

"""
解决思路：
1、双重遍历，效率低下
2、可以把每次相减后的结果和索引放到map集合中去，数组移动下一个数时，判断是否存在，如果存在，那么说明找到了这两个数。
"""


class Solution:
    def two_sum(self, numbers, target):
        """
        :param numbers:
        :param target:
        :return:
        """
        mapping = dict()    # 保存余数和另一个数的索引
        for idx, item in enumerate(numbers):
            index = mapping.get(item)
            if index is None:
                remainder = target - item
                mapping[remainder] = idx
            else:
                return index + 1, idx + 1
        return "no result"


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    s = Solution()
    print(s.two_sum(nums, 9))