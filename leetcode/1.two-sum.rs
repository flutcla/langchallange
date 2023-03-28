/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 */
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hm = HashMap::new();
        for (ind, val) in nums.iter().enumerate() {
            hm.insert(val, ind);
        }
        for (ind, val) in nums.iter().enumerate() {
            match hm.get(&(target-val)) {
                None => (),
                Some(x) => if ind != *x {return Vec::from([ind as i32, *x as i32])}
            }
        }
        panic!();
    }
}
// @lc code=end

