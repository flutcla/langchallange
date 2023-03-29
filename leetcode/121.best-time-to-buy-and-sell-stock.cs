/*
 * @lc app=leetcode id=121 lang=csharp
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
public class Solution {
    public int MaxProfit(int[] prices) {
        int min_index = 0;
        int max_index = 1;
        int max_profit = 0;
        while (max_index < prices.Length) {
            if (prices[min_index] > prices[max_index]) {
                min_index = max_index;
                max_index++;
                continue;
            }
            int profit = prices[max_index] - prices[min_index];
            if (profit > max_profit){
                max_profit = profit;
            }
            max_index++;
        }
        return max_profit;
    }
}
// @lc code=end

