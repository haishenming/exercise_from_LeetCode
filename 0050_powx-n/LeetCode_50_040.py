# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
#
#
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
#
#
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
#
# 说明:
#
#
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
#
# Related Topics 数学 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    rdata = 1

    def myPow1(self, x: float, n: int) -> float:
        # 暴力
        rdata = 1

        if n > 0:
            for i in range(n):
                rdata *= x

        else:
            n = -n
            for i in range(n):
                rdata *= 1 / x

        return rdata

    def pow(self, x:float, n:int):
        if n == 0:
            return 1.0

        half = self.pow(x, n // 2)

        if n % 2 == 0:

            return half * half
        else:
            return half * half * x

    def myPow2(self, x: float, n: int) -> float:
        # 分治
        N = n
        if n < 0:
            x = 1 / x
            N = -N

        return self.pow(x, N)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print(s.myPow2(2.0, 10))
