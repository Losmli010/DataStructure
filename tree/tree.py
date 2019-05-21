#二叉树的实现
from collections import deque

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self):
        self.root = None

    #深度优先遍历:stack
    #先根
    def preorder(self, root):
        if not root:
            return []
        return [root.value] + self.preorder(root.left) + self.preorder(root.right)

    #中根
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.value] + self.inorder(root.right)

    #后根
    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.value]

    #广度优先遍历: queue
    def levelorder(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

root = TreeNode(10, TreeNode(9, TreeNode(7)), TreeNode(8, None, TreeNode(6)))
btree = BinaryTree()
print(btree.preorder(root))
print(btree.inorder(root))
print(btree.postorder(root))
print(btree.levelorder(root))