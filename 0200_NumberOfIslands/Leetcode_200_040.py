#给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
#
# 输入:
#11110
#11010
#11000
#00000
#
#输出: 1
#
#
# 示例 2:
#
# 输入:
#11000
#11000
#00100
#00011
#
#输出: 3
#
# Related Topics 深度优先搜索 广度优先搜索 并查集



#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: list) -> int:
        # todo
        pass


#leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1],
    ]

    print(s.numIslands(grid))