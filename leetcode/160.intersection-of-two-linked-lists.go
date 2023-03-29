/*
 * @lc app=leetcode id=160 lang=golang
 *
 * [160] Intersection of Two Linked Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	m := map[*ListNode]bool{}
	for headA != nil {
		m[headA] = true
		headA = headA.Next
	}
	for headB != nil {
		if m[headB] {
			return headB
		}
		headB = headB.Next
	}
	return nil
}

// @lc code=end

