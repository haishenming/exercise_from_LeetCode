# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
# ]
#
# Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def __init__(self):
        self.rdata = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.generate(0, 0, n, "")
        return self.rdata

    def generate(self, left: int, right: int, n: int, s: str):
        if left == n and right == n:
            self.rdata.append(s)
            return

        if left < n:
            self.generate(left + 1, right, n, s + "(")

        if right < n and right < left:
            self.generate(left, right + 1, n, s + ")")

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
