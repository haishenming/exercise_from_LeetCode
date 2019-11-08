#给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
#给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#   / \
#  9  20
#    /  \
#   15   7
#
#
# 返回其层次遍历结果：
#
# [
#  [3],
#  [9,20],
#  [15,7]
#]
#
# Related Topics 树 广度优先搜索



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder1(self, root: TreeNode) -> list:
        # DFS
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

    def levelOrder2(self, root: TreeNode) -> list:
        # BFS
        from collections import deque

        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root,])
        while queue:
            levels.append([])
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return levels









#leetcode submit region end(Prohibit modification and deletion)

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
    print(s.levelOrder2(root))
