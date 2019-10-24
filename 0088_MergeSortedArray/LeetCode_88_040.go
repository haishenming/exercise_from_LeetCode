package main

import "fmt"

//给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
//
// 说明:
//
//
// 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
// 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
//
//
// 示例:
//
// 输入:
//nums1 = [1,2,3,0,0,0], m = 3
//nums2 = [2,5,6],       n = 3
//
//输出: [1,2,2,3,5,6]
// Related Topics 数组 双指针

//leetcode submit region begin(Prohibit modification and deletion)
func merge(nums1 []int, m int, nums2 []int, n int) {
	nums3 := make([]int, m, m) // 这里需要注意golang中切片类型的拷贝
	copy(nums3, nums1)
	nums1 = nums1[:0]

	var i1, i2 int
	for i1 < m && i2 < n {
		if nums3[i1] < nums2[i2] {
			nums1 = append(nums1, nums3[i1])
			i1++
		} else {
			nums1 = append(nums1, nums2[i2])
			i2++
		}
	}

	if i1 < m {
		nums1 = append(nums1, nums3[i1:]...)
	}

	if i2 < n {
		nums1 = append(nums1, nums2[i2:]...)
	}

}

//leetcode submit region end(Prohibit modification and deletion)
func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	m := 3
	nums2 := []int{2, 5, 6}
	n := 3

	merge(nums1, m, nums2, n)

	fmt.Println(nums1)

}
