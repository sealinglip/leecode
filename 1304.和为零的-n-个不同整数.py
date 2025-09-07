#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的 N 个不同整数
#
# https://leetcode.cn/problems/find-n-unique-integers-sum-up-to-zero/description/
#
# algorithms
# Easy (70.48%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    42.8K
# Total Submissions: 59.2K
# Testcase Example:  '5'
#
# 给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。
# 
# 
# 示例 1：
# 输入：n = 5
# 输出：[-7,-1,1,3,4]
# 解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
# 
# 示例 2：
# 输入：n = 3
# 输出：[-1,0,1]
# 
# 示例 3：
# 输入：n = 1
# 输出：[0]
# 
# 
# 提示：
# 1 <= n <= 1000
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n & 1:
            # n 为奇数
            return list(range(-(n>>1), (n>>1)+1))
        else:
            return list(range(-(n>>1), 0)) + list(range(1, (n>>1)+1))
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumZero(5)) # [-2,-1,0,1,2]
    print(solution.sumZero(3)) # [-1,0,1]
    print(solution.sumZero(1)) # [0]
    print(solution.sumZero(2)) # [-1,1]
