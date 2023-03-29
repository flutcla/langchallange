/*
 * @lc app=leetcode id=141 lang=javascript
 *
 * [141] Linked List Cycle
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
  while (head != null) {
    if (head.val === false) {
      return true;
    } else {
      head.val = false;
      head = head.next;
    }
  }
  return false;
};
// @lc code=end

