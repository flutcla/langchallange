/*
 * @lc app=leetcode id=1 lang=scala
 *
 * [1] Two Sum
 */

// @lc code=start
object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val map = nums.zipWithIndex.foldLeft(Map[Int, Int]()) { case (acc, (v, i)) => acc + (v -> i)}
        for ((v, i) <- nums.zipWithIndex) {
            map.get(target - v) match {
                case None => ();
                case Some(x) => if (i != x) return Array(i, x) else ();
            }
        }
        return nums;
    }
}
// @lc code=end

