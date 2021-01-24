#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

from typing import List
# @lc code=start


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lcis = 0
        cis = 0
        prev = None
        for n in nums:
            if prev is None or n > prev:
                cis += 1
            else:
                if cis > lcis:
                    lcis = cis
                cis = 1
            prev = n

        return max(lcis, cis)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # print(solution.findLengthOfLCIS([1, 3, 5, 7]))
    print(solution.findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]))
    print(solution.findLengthOfLCIS([1, 3, 5, 4, 7]))
    print(solution.findLengthOfLCIS([2, 2, 2, 2, 2]))
