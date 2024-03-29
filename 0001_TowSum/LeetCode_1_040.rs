//给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
//
// 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
//
// 示例:
//
// 给定 nums = [2, 7, 11, 15], target = 9
//
//因为 nums[0] + nums[1] = 2 + 7 = 9
//所以返回 [0, 1]
//
// Related Topics 数组 哈希表


//leetcode submit region begin(Prohibit modification and deletion)
// todo

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_hash: HashMap<i32, i32> = HashMap::new();
        let mut j: i32;

        for (i, x) in nums.iter().enumerate() {
            num_hash.insert(*x as i32, i as i32);
        }

        for (i, x) in nums.iter().enumerate() {
            match num_hash.get(&(target - (*x))) {
                Some(v) => {
                    j = *v;
                }
                None => continue,
            };
            if j != i as i32 {
                return vec![i as i32, j as i32];
            }
        }


        return Vec::new();
    }
}

//leetcode submit region end(Prohibit modification and deletion)
fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;

    let rdata = Solution::two_sum(nums, target);
    println!("{} {}", rdata[0], rdata[1]);
}