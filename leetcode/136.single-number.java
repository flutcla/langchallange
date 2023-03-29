/*
 * @lc app=leetcode id=136 lang=java
 *
 * [136] Single Number
 */

// @lc code=start
class Solution {
    public int singleNumber(int[] nums) {
        int m = (int) (4 * Math.pow(10, 4));
        int[] n = new int[m * 2];
        for (int i : nums) {
            n[m + i] ^= 1;
        }
        for(int i = 0; i < m * 2; i++){
            if (n[i] == 1) return i - m;
        }
        return 0;
    }
}
// @lc code=end

