#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# 给定一个二进制数组， 计算其中最大连续1的个数。

# 示例 1:
# 输入: [1, 1, 0, 1, 1, 1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

# 注意：
# 输入的数组只包含 0 和 1。
# 输入数组的长度是正整数，且不超过 10, 000。

from typing import List
# @lc code=start


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCo = co = 0
        for num in nums:
            if num:
                co += 1
            else:
                if co > maxCo:
                    maxCo = co
                co = 0
        if co > maxCo:
            maxCo = co
        return maxCo

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
