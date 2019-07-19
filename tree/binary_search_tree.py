"""
在二叉查找树中：
(01) 若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值
(02) 任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值
(03) 任意节点的左、右子树也分别为二叉查找树
(04) 没有键值相等的节点（no duplicate nodes）
"""
import pickle

copy = lambda obj: pickle.loads(pickle.dumps(obj, 4))

class TreeNode(object):
    def __init__(self, key, left, right, parent):
        self.key = key          # 节点值
        self.left = left        # 左节点
        self.right = right      # 右节点
        self.parent = parent    # 父节点

    def __str__(self):
        return "TreeNode<%r>" % self.key


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        插入
        :param key:
        :return:
        """
        if self.root is None:
            # 空树
            self.root = TreeNode(key, None, None, None)
            return

        cur = self.root
        while cur:
            if key > cur.key:
                # 添加到右子树
                if cur.right is None:
                    cur.right = TreeNode(key, None, None, cur)
                else:
                    cur = cur.right
            elif key < cur.key:
                # 添加到左子树
                if cur.left is None:
                    cur.left = TreeNode(key, None, None, cur)
                else:
                    cur = cur.left
            else:
                return

    def remove(self, key):
        """
        删除
        :param key:
        :return:
        """
        cur = self.root
        while cur:
            if key > cur.key:
                # 右子树查找
                cur = cur.right
            elif key < cur.key:
                # 左子树查找
                cur = cur.left
            elif key == cur.key:
                # cur为叶子
                if (cur.left is None) and (cur.right is None):
                    if cur.parent is None:      # 删除节点为根节点
                        self.root = None
                    elif cur.parent.key > key:    # 删除节点为左叶子节点
                        cur.parent.left = None
                    else:
                        cur.parent.right = None
                    return
                # cur有左子树无右子树
                elif (cur.left is not None) and (cur.right is None):
                    if cur.parent is None:      # 删除节点为根节点
                        self.root = self.root.left
                    elif cur.parent.key > key:  # 删除节点为左子树节点
                        cur.parent.left = cur.left
                    else:
                        cur.parent.right = cur.left
                    return
                # cur有右子树无左子树
                elif (cur.left is None) and (cur.right is not None):
                    if cur.parent is None:  # 删除节点为根节点
                        self.root = self.root.right
                    elif cur.parent.left.key == key:  # 删除节点为左子树节点
                        cur.parent.left = cur.right
                    else:
                        cur.parent.right = cur.right
                    return
                # cur有左右子树
                elif (cur.left is not None) and (cur.right is not None):
                    # 找到右子树中的最小节点并交换key
                    temp = cur.right
                    while temp.left:
                        temp = temp.left
                    cur.key = temp.key
                    temp.key = key
                    cur = temp

    def get(self, key):
        """
        查找
        :param key:
        :return: 存在，返回节点；不存在返回None
        """
        cur = self.root
        while cur:
            if key == cur.key:
                return cur
            elif key > cur.key:
                # 右子树中查找
                cur = cur.right
            else:
                # 左子树中查找
                cur = cur.left

    def get_min(self):
        """
        查找最小节点
        :return:
        """
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur

    def get_max(self):
        """
        查找最大节点
        :return:
        """
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur

    def preorder(self):
        """
        前序遍历：根节点->左子树->右子树
        :return:
        """
        if self.root is None:
            return []

        result = []
        stack = [self.root]

        cur = self.root
        while stack:
            result.append(cur.key)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)

            cur = stack.pop()
        return result

    def inorder(self):
        """
        中序遍历：左子树->根节点->右子树
        :return:
        """
        if self.root is None:
            return []

        result = []
        stack = []

        cur = self.root
        while cur or stack:
            if cur is None:
                cur = stack.pop()
                result.append(cur.key)
                cur = cur.right
            else:
                stack.append(cur)
                cur = cur.left
        return result

    def postorder(self):
        """
        后序遍历：左子树->右子树->根节点
        :return:
        """
        if self.root is None:
            return []

        stack = [self.root]
        stack2 = []
        result = []
        while stack:
            cur = stack.pop()
            stack2.append(cur)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        while stack2:
            node = stack2.pop()
            result.append(node.key)
        return result

    def __str__(self):
        preorder = self.preorder()
        inorder = self.inorder()
        postorder = self.postorder()
        return "Pre-order: %r\n" \
               "In-order: %r\n" \
               "Post-order: %r" % (preorder, inorder, postorder)

if __name__ == '__main__':
    tree = BinarySearchTree()
    print("****************插入*********************")
    for i in [10, 22, 4, 6, 36, 75, 79, 64, 14, 33]:
        tree.insert(i)
    print(tree)

    print("****************获取/删除*********************")
    for i in [6, 33, 79, 22, 10]:
        t = tree.get(i)
        print(t)
        tree.remove(i)
        print(tree)
