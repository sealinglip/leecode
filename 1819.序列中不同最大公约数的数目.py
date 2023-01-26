#
# @lc app=leetcode.cn id=1819 lang=python3
#
# [1819] 序列中不同最大公约数的数目
#
# 给你一个由正整数组成的数组 nums 。

# 数字序列的 最大公约数 定义为序列中所有整数的共有约数中的最大整数。

# 例如，序列[4, 6, 16] 的最大公约数是 2 。
# 数组的一个 子序列 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。

# 例如，[2, 5, 10] 是[1, 2, 1, 2, 4, 1, 5, 10] 的一个子序列。
# 计算并返回 nums 的所有 非空 子序列中 不同 最大公约数的 数目 。


# 示例 1：
# 输入：nums = [6, 10, 3]
# 输出：5
# 解释：上图显示了所有的非空子序列与各自的最大公约数。
# 不同的最大公约数为 6 、10 、3 、2 和 1 。

# 示例 2：
# 输入：nums = [5, 15, 40, 5, 6]
# 输出：7


# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 2 * 10^5

# Hard
# 复习

from math import gcd
from typing import List
# @lc code=start


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # 枚举
        ub = max(nums)
        numSet = set(nums)
        res = 0
        for i in range(1, ub + 1):
            curGcd = 0
            for j in range(i, ub + 1, i):
                if j in numSet:
                    if curGcd == 0:
                        curGcd = j
                    else:
                        curGcd = gcd(curGcd, j)
                    if curGcd == i:
                        res += 1
                        break

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countDifferentSubsequenceGCDs([6, 10, 3]))  # 5
    print(solution.countDifferentSubsequenceGCDs([5, 15, 40, 5, 6]))  # 7
