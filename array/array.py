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