#
# @lc app=leetcode id=1 lang=ruby
#
# [1] Two Sum
#

# @lc code=start
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  # brute-force exceeds time limits, use Hash.
  h = {}
  for i in 0..nums.length-1 do
    h[nums[i].to_s] = i
  end

  for i in 0..nums.length-1 do
    rest = target - nums[i]
    j = h[rest.to_s]
    if j != nil && i != j then
      return [i, j]
    end
  end
end
# @lc code=end

