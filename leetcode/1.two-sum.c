/*
 * @lc app=leetcode id=1 lang=c
 *
 * [1] Two Sum
 */

// @lc code=start
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
  int i, j;
  int* ret;
  ret = (int*)malloc(sizeof(int) * 2);
  *returnSize = 2;
  for(i=0; i<numsSize; i++){
    for(j=i+1; j<numsSize; j++){
      if(nums[i] + nums[j] == target){
        ret[0] = i;
        ret[1] = j;
        return ret;
      }
    }
  }
  return ret;
}
// @lc code=end

