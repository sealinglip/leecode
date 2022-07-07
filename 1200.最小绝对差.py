#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#
# 给你个整数数组 arr，其中每个元素都 不相同。

# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。


# 示例 1：
# 输入：arr = [4, 2, 1, 3]
# 输出：[[1, 2], [2, 3], [3, 4]]

# 示例 2：
# 输入：arr = [1, 3, 6, 10, 15]
# 输出：[[1, 3]]

# 示例 3：
# 输入：arr = [3, 8, -10, 23, 19, -4, -14, 27]
# 输出：[[-14, -10], [19, 23], [23, 27]]


# 提示：
# 2 <= arr.length <= 10 ^ 5
# -10 ^ 6 <= arr[i] <= 10 ^ 6

from typing import List
# @lc code=start


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minAbsDiff = 10 ** 6
        prevN = None
        res = []
        for n in sorted(arr):
            if prevN is not None:
                absDiff = n - prevN
                if absDiff <= minAbsDiff:
                    if absDiff < minAbsDiff:
                        res.clear()
                        minAbsDiff = absDiff
                    res.append([prevN, n])

            prevN = n

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumAbsDifference([4, 2, 1, 3]))  # [[1,2],[2,3],[3,4]]
    print(solution.minimumAbsDifference(
        [1, 3, 6, 10, 15]))  # [[1,3]]
    print(solution.minimumAbsDifference(
        [3, 8, -10, 23, 19, -4, -14, 27]))  # [[-14,-10],[19,23],[23,27]]
