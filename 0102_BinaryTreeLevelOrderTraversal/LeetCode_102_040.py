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
    def levelOrder(self, root: TreeNode) -> list:
        # BFS
        q = []
        levels = []
        if not root:
            return []

        q.append(root)
        level = 0

        while q:
            levels.append([])
            level_length = len(q)
            for i in range(level_length):
                node = q.pop()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
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
    print(s.levelOrder(root))
