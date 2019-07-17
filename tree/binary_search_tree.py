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
                        return
                    elif cur.parent.left.key == key:    # 删除节点为左叶子节点
                        cur.parent.left = None
                    else:
                        cur.parent.right = None
                # cur有左子树无右子树
                elif (cur.left is not None) and (cur.right is None):
                    if cur.parent is None:      # 删除节点为根节点
                        self.root = self.root.left
                    elif cur.parent.left.key == key:  # 删除节点为左子树节点
                        cur.parent.left = cur.left
                    else:
                        cur.parent.right = cur.left
                # cur有右子树无左子树
                elif (cur.left is None) and (cur.right is not None):
                    if cur.parent is None:  # 删除节点为根节点
                        self.root = self.root.right
                    elif cur.parent.left.key == key:  # 删除节点为左子树节点
                        cur.parent.left = cur.right
                    else:
                        cur.parent.right = cur.right
                # cur有左右子树
                elif (cur.left is not None) and (cur.right is not None):
                    # 找到右子树中的最小节点并交换key
                    val = copy(cur.key)
                    temp = copy(cur.right)
                    while temp.left:
                        temp = temp.left
                    cur.key = temp.key
                    cur = temp
                    cur.key = val

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

    def preorder(self, node):
        """
        前序遍历：根节点->左子树->右子树
        :return:
        """
        if node is not None:
            yield node.key
            yield self.preorder(node.left)
            yield self.preorder(node.right)

    def inorder(self, node):
        """
        中序遍历：左子树->根节点->右子树
        :return:
        """
        if node is not None:
            yield self.inorder(node.left)
            yield node.key
            yield self.inorder(node.right)

    def postorder(self, node):
        """
        后序遍历：左子树->右子树->根节点
        :return:
        """
        if node is not None:
            yield self.postorder(node.left)
            yield self.postorder(node.right)
            yield node.key

    def __str__(self):
        result = ""
        cur = self.root
        while cur:
            result += "-->%s" % cur.key
            left = cur.left
            while left:
                left = left.left

        return result

if __name__ == '__main__':
    tree = BinarySearchTree()
    for i in range(10):
        tree.insert(i)
        print(tree.get(i))
        print(tree.remove(i))
