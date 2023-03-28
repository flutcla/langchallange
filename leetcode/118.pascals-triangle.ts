/*
 * @lc app=leetcode id=118 lang=typescript
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
function generate(numRows: number): number[][] {
  var ret: number[][] = [[1]];
  for (let i=0; i<numRows-1; i++) {
    var tmp: number[] = [1];
    for (let j=0; j<ret[i].length-1; j++) {
      tmp.push(ret[i][j] + ret[i][j+1]);
    }
    tmp.push(1);
    ret.push(tmp);
  }
  return ret;
};
// @lc code=end

