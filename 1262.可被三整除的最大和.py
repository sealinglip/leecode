#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。


# 示例 1：
# 输入：nums = [3, 6, 5, 1, 8]
# 输出：18
# 解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。

# 示例 2：
# 输入：nums = [4]
# 输出：0
# 解释：4 不能被 3 整除，所以无法选出数字，返回 0。

# 示例 3：
# 输入：nums = [1, 2, 3, 4, 4]
# 输出：12
# 解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。


# 提示：
# 1 <= nums.length <= 4 * 10 ^ 4
# 1 <= nums[i] <= 10 ^ 4

from math import inf
from typing import List
# @lc code=start


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res = 0
        stat = [[0, 0, inf, inf]
                for _ in range(2)]  # 分别记录余数为1和2的数的个数、总和、最小和次最小
        for num in nums:
            r = num % 3
            if r == 0:
                res += num
            else:
                r -= 1
                stat[r][0] += 1
                stat[r][1] += num
                if num <= stat[r][2]:
                    stat[r][3] = stat[r][2]
                    stat[r][2] = num
                elif num < stat[r][3]:
                    stat[r][3] = num

        res += stat[0][1] + stat[1][1]
        r = (stat[0][0] - stat[1][0]) % 3
        if r == 2:  # 余数为1的多俩或者少一个
            delta = stat[1][2] if stat[0][0] < 2 else min(
                stat[1][2], stat[0][2] + stat[0][3])
            res -= delta
        elif r == 1:  # 余数为1的多一个或者少俩
            delta = stat[0][2] if stat[1][0] < 2 else min(
                stat[0][2], stat[1][2] + stat[1][3])
            res -= delta

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumDivThree([3, 6, 5, 1, 8]))  # 18
    print(solution.maxSumDivThree([4]))  # 0
    print(solution.maxSumDivThree([1, 2, 3, 4, 4]))  # 12
