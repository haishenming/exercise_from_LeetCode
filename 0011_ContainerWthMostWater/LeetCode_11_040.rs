// todo 第三遍 2019年10月17日

//给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
//
// 说明：你不能倾斜容器，且 n 的值至少为 2。
//
//
//
// 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
//
//
//
// 示例:
//
// 输入: [1,8,6,2,5,4,8,3,7]
//输出: 49
// Related Topics 数组 双指针

struct Solution {}

//leetcode submit region begin(Prohibit modification and deletion)
impl Solution {
    pub fn max_area1(height: Vec<i32>) -> i32 {
        // 暴力法

        let mut max_area: i32 = 0;
        for i in 0..height.len() {
            for j in i..height.len() {
                let mut length:i32 = height[j];
                if height[i] < height[j] {
                    length = height[i]
                }

                let area:i32 = length * (j as i32-i as i32);
                if area > max_area {
                    max_area = area;
                }
            }
        }

        return max_area;
    }

    pub fn max_area2(height: Vec<i32>) -> i32 {
        // 双指针
    }

//leetcode submit region end(Prohibit modification and deletion)
fn main() {
    println!("{}", Solution::max_area1(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]));
}