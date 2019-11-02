#给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
#输出: 3
#
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
#输出: 2
#
# Related Topics 位运算 数组 分治算法
from collections import Counter


#leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement1(self, nums: list) -> int:
        # 数学统计
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement2(self, nums: list) -> int:
        # 排序
        nums.sort()
        return nums[len(nums) // 2]


#leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement2([2,2,1,1,1,2,2]))