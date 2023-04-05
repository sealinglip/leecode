#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#
# 给你一个正整数数组 arr（可能存在重复的元素），请你返回可在 一次交换（交换两数字 arr[i] 和 arr[j] 的位置）后得到的、按字典序排列小于 arr 的最大排列。

# 如果无法这么操作，就请返回原数组。


# 示例 1：
# 输入：arr = [3, 2, 1]
# 输出：[3, 1, 2]
# 解释：交换 2 和 1

# 示例 2：
# 输入：arr = [1, 1, 5]
# 输出：[1, 1, 5]
# 解释：已经是最小排列

# 示例 3：
# 输入：arr = [1, 9, 4, 6, 7]
# 输出：[1, 7, 4, 6, 9]
# 解释：交换 9 和 7


# 提示：
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^4

from typing import List
# @lc code=start
from bisect import bisect_left
from math import inf


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # 从后往前找，找到第一个逆序的地方，如果有，交换该位置和后续小于该位置的最大数所在位置
        # 如果没有，返回原数组
        cur = inf
        i = len(arr) - 1
        while i >= 0 and cur >= arr[i]:
            cur = arr[i]
            i -= 1

        if i >= 0:
            # 交换arr[i] 和 i之后小于arr[i]的最大值所在位置
            j = bisect_left(arr, arr[i], lo=i+1) - 1
            while j > 0 and arr[j] == arr[j-1]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        return arr


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.prevPermOpt1([3, 1, 1, 3]))  # [1,3,1,3]
    print(solution.prevPermOpt1([3, 2, 1]))  # [3,1,2]
    print(solution.prevPermOpt1([1, 1, 5]))  # [1,1,5]
    print(solution.prevPermOpt1([1, 9, 4, 6, 7]))  # [1,7,4,6,9]
