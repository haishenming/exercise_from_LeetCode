# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return left if left > right else right


if __name__ == '__main__':
    root = TreeNode(3)
    t9 = TreeNode(9)
    t20 = TreeNode(20)
    t15 = TreeNode(15)
    t7 = TreeNode(7)
    t91 = TreeNode(91)
    t92 = TreeNode(92)

    root.right = t9
    root.left = t20
    t20.right = t15
    t20.left = t7
    t9.left = t91
    t9.right = t92

    s = Solution()

    print(s.maxDepth(root))
