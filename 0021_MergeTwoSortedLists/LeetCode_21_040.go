package main

import "fmt"

//将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
//
// 示例：
//
// 输入：1->2->4, 1->3->4
//输出：1->1->2->3->4->4
//
// Related Topics 链表

//leetcode submit region begin(Prohibit modification and deletion)
/**
* Definition for singly-linked list.

* }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	l3 := &ListNode{Val: -1}
	pre := l3
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			pre.Next = l1
			l1 = l1.Next
		} else {
			pre.Next = l2
			l2 = l2.Next
		}
		pre = pre.Next
		fmt.Println(pre.Val)
	}

	if l1 != nil {
		pre.Next = l1
	}

	if l2 != nil {
		pre.Next = l2
	}

	return l3.Next
}

//leetcode submit region end(Prohibit modification and deletion)
func main() {
	a1 := &ListNode{Val: 1}
	a2 := &ListNode{Val: 2}
	a3 := &ListNode{Val: 4}

	a1.Next = a2
	a2.Next = a3

	b1 := &ListNode{Val: 1}
	b2 := &ListNode{Val: 3}
	b3 := &ListNode{Val: 4}

	b1.Next = b2
	b2.Next = b3

	c1 := mergeTwoLists(a1, b1)

	fmt.Println("================")

	for c1 != nil {
		fmt.Println(c1.Val)
		c1 = c1.Next
	}

}
